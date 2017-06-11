# Write your calc_stats function here.
import numpy as np


def calc_stats(path):
    data = np.loadtxt(path, delimiter=',')
    data = np.asarray(data, float)
    mean = np.mean(data)
    median = np.median(data)
    mean, median = np.round([mean, median], 1)
    return (mean, median)


# You can use this to test your function.
# Any code inside this `if` statement will be ignored by the automarker.
if __name__ == '__main__':
    # Run your `calc_stats` function with examples:

    print(calc_stats('data.csv'))
    print(calc_stats('data2.csv'))
    print(calc_stats('data3.csv'))
