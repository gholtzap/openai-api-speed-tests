import numpy as np

davinci_trial1 = np.array([
    [0.74,	1.14,	0.85,	0.87,	0.79],
    [1.45,	1.41,	1.88,	1.89,	2.43],
    [1.97,	1.66,	1.61,	3.76,	9.26],
    [1.53,	1.35,	1.86,	8.80,	20.67]
])


trials = [davinci_trial1]

def davinci_avg(trials):
    num_trials = len(trials)
    summed_trials = np.sum(trials, axis=0)
    averaged_array = summed_trials / num_trials
    averaged_list = averaged_array.tolist()
    return averaged_list


averaged_davinci_data = davinci_avg(trials)