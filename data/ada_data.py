import numpy as np

ada_trial1 = np.array([
    [0.26,	0.26,	0.27,  	0.26,	0.26],
    [0.68,	0.61,	0.64, 	0.76,	0.75],
    [0.75,	0.76, 	0.97, 	2.51,	2.93],
    [0.71,	0.78,	1.95,	3.91,	9.33]
])

ada_trial2 = np.array([
    [0.33,	0.32,	0.29,	0.30,	0.30],
    [0.69,	0.62,	0.71,	0.71,	0.76],
    [0.77,	0.63,	1.34,	1.34,	2.61],
    [0.78,	0.68,	1.83,	1.83,	8.78]
])

trials = [ada_trial1, ada_trial2]


def ada_avg(trials):
    num_trials = len(trials)
    summed_trials = np.sum(trials, axis=0)
    averaged_array = summed_trials / num_trials
    averaged_list = averaged_array.tolist()
    return averaged_list


averaged_ada_data = ada_avg(trials)
