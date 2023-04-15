import numpy as np

curie_trial1 = np.array([
    [0.34,  0.34,   0.31,   0.35,   0.35],
    [0.64,  0.76,   0.71,   0.89,   1.08],
    [0.66,  0.63,   0.88,   1.59,   2.65],
    [0.70,  0.61,   0.78,   2.33,   6.16]
])


trials = [curie_trial1]

def curie_avg(trials):
    num_trials = len(trials)
    summed_trials = np.sum(trials, axis=0)
    averaged_array = summed_trials / num_trials
    averaged_list = averaged_array.tolist()
    return averaged_list


averaged_curie_data = curie_avg(trials)