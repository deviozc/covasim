'''
Set the defaults across each of the different files.
'''

import numpy as np
import sciris as sc

# Specify all externally visible functions this file defines
__all__ = ['person_props', 'person_states', 'person_dates', 'person_durs', 'all_person_states',
           'contact_props', 'result_stocks', 'result_flows', 'default_age_data',
           'default_colors', 'default_sim_plots', 'default_scen_plots']

# Set the properties of a person
person_props = [
    'uid',         # Any (int or str, usually)
    'age',         # Float
    'sex',         # Int
    'symp_prob',   # Float
    'severe_prob', # Float
    'crit_prob',   # Float
    'death_prob',  # Float
]

# Set the states that a person can be in: these are all booleans per person -- used in people.py
person_states = [
    'susceptible',
    'exposed',
    'infectious',
    'symptomatic',
    'severe',
    'critical',
    'tested',
    'diagnosed',
    'recovered',
    'dead',
    'known_contact',
    'quarantined',
]

# Set the dates various events took place: these are floats per person -- used in people.py
person_dates = [f'date_{state}' for state in person_states]
person_dates.append('date_quarantined_end')

# Duration of different states: these are floats per person -- used in people.py
person_durs = [
    'dur_exp2inf',
    'dur_inf2sym',
    'dur_sym2sev',
    'dur_sev2crit',
    'dur_disease',
]

all_person_states = person_props + person_states + person_dates + person_durs

# Properties of contacts
contact_props = {
    'p1':      np.int32, # Person 1
    'p2':      np.int32,  # Person 2
    'layer':   str, # The layer by which the people are connected
    'beta':    np.float32, # Default transmissibility for this contact type
    'dynamic': bool, # Whether or not this contact is dynamic
}

# A subset of the above states are used for results
result_stocks = {
        'susceptible': 'Number susceptible',
        'exposed':     'Number exposed',
        'infectious':  'Number infectious',
        'symptomatic': 'Number symptomatic',
        'severe':      'Number of severe cases',
        'critical':    'Number of critical cases',
        'diagnosed':   'Number of confirmed cases',
        'quarantined': 'Number in quarantine',
}

# The types of result that are counted as flows -- used in sim.py; value is the label suffix
result_flows = {'infections':  'infections',
                'tests':       'tests',
                'diagnoses':   'diagnoses',
                'recoveries':  'recoveries',
                'symptomatic': 'symptomatic cases',
                'severe':      'severe cases',
                'critical':    'critical cases',
                'deaths':      'deaths',
                'quarantined': 'quarantined people',
}

# Default age data, based on Seattle 2018 census data -- used in population.py
default_age_data = np.array([
            [ 0,  4, 0.0605],
            [ 5,  9, 0.0607],
            [10, 14, 0.0566],
            [15, 19, 0.0557],
            [20, 24, 0.0612],
            [25, 29, 0.0843],
            [30, 34, 0.0848],
            [35, 39, 0.0764],
            [40, 44, 0.0697],
            [45, 49, 0.0701],
            [50, 54, 0.0681],
            [55, 59, 0.0653],
            [60, 64, 0.0591],
            [65, 69, 0.0453],
            [70, 74, 0.0312],
            [75, 79, 0.02016], # Calculated based on 0.0504 total for >=75
            [80, 84, 0.01344],
            [85, 89, 0.01008],
            [90, 99, 0.00672],
            ])


# Specify plot colors -- used in sim.py -- NB, includes duplicates since stocks and flows are named differently
default_colors = sc.objdict(
    susceptible = '#5e7544',
    infectious  = '#c78f65',
    infections  = '#c75649',
    exposed     = '#c75649', # Duplicate
    tests       = '#aaa8ff',
    diagnoses   = '#8886cc',
    diagnosed   = '#8886cc', # Duplicate
    recoveries  = '#799956',
    recovered   = '#799956', # Duplicate
    symptomatic = '#c1ad71',
    severe      = '#c1981d',
    quarantined = '#5f1914',
    critical    = '#b86113',
    deaths      = '#000000',
    dead        = '#000000', # Duplicate
    )


# Specify which quantities to plot -- note, these can be turned on and off by commenting/uncommenting lines; used in sim.py
default_sim_plots = sc.odict({
        'Total counts': [
            'cum_infections',
            'cum_diagnoses',
            'cum_recoveries',
            # 'cum_tests',
            # 'n_susceptible',
            # 'n_infectious',
        ],
        'Daily counts': [
            'new_infections',
            'new_diagnoses',
            'new_recoveries',
            'new_deaths',
            # 'tests',
        ],
        'Health outcomes': [
            'cum_severe',
            'cum_critical',
            'cum_deaths',
            # 'n_severe',
            # 'n_critical',
        ]
})


# Default scenario plots -- used in run.py
default_scen_plots = [
            'cum_infections',
            'n_infectious',
            'n_severe',
]