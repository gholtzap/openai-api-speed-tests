import numpy as np


babbage_trial1 = np.array([
    [0.32,	0.33,	0.31,	0.30,	0.33],
    [0.57,	0.60,	0.63,	0.75,	0.93],
    [0.60,	0.63,	0.65,	1.57,	2.41],
    [0.68,	0.52,	0.81,	1.75,	4.00]
])

trials = [babbage_trial1]

def babbage_avg(trials):
    num_trials = len(trials)
    summed_trials = np.sum(trials, axis=0)
    averaged_array = summed_trials / num_trials
    averaged_list = averaged_array.tolist()
    return averaged_list


averaged_babbage_data = babbage_avg(trials)
