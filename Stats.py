import numpy as np
import math
from collections import Counter

def mean(x):
    """calculate and return the mean of a numpy array"""
    sum = 0
    for i in range(len(x)):
        sum += x[i]
    return round(sum/len(x), 2)

def median(x):
    """return the 'middle value' of the array x after sorting"""
    tmp = sorted(x)
    # use // for integer division (i.e. round down)
    return tmp[len(x) // 2] if len(x) % 2 == 1 else (tmp[len(x) // 2] + tmp[(len(x) // 2)-1]) / 2

def mode(xs):
    counts = Counter(xs)
    return np.array([x[0] for x in counts.items() if x[1] == max(counts.values())])

def quantile(xs, q):
    """generalize the median to the q-percent quantile -- q is a float in range (0,1)"""
    tmp = sorted(xs)
    return tmp[ int(len(tmp) * q) ]

def interquartile_range(xs):
    """return difference of the 25% quantile and 75% quantile"""
    return quantile(xs, 0.75) - quantile(xs, 0.25)

def spread(x):
    """one way to measure the spread of data"""
    return max(x) - min(x)

def center(xs):
    return np.array([x - mean(xs) for x in xs])

def var(xs):
    """return variance of x -- the average squared distance from the mean"""
    return mean([x**2 for x in center(xs)])
    # return sum([x**2 for x in center(xs)])/(len(xs) - 1)

def std(xs):
    return math.sqrt(var(xs))

def cov(xs, ys):
    """Take two lists of observations and compute their covariance"""
    assert len(xs) == len(ys)
    cx = center(xs)
    cy = center(ys)
    return mean([cx[i]*cy[i] for i in range(len(cx))])

def correlation(xs, ys):
    """Calculate the (Pearson) correlation coefficient"""
    return cov(xs,ys)/(std(xs)*std(ys))

# something you will see...
# we can make this do the print, but *only* when this
# file is run as a standalone program, not through an import.
# when a python program runs, it sets the dunder __name__ 
# variable to be its context in the greater program.
# So the program that got ran through python is __main__
# typically used if you want have some tests here but 
# don't run the tests when you import into other programs
if __name__ == '__main__':
    print('testing stats.py...')
    
    print(f'the mean of [1,2,3,4,5] is {mean(np.array([1,2,3,4,5]))}')
    # assert(mean(np.array([1,2,3,4,5])) == 3.5)
    print(f'the median of [2,5,4,3,1] is {median([2,5,4,3,1])}')
    print(f'the median of [2,5,4,3] is {median([2,5,4,3])}')
    print(f'the variance of [2,5,4,3] is {var([2,5,4,3])}')
    print(f'the standard deviation of [2,5,4,3] is {std([2,5,4,3])}')
    print(f'the mode of {[1,2,3,4,3,2,3,1,2,1,1,2,3,2]} is {mode([1,2,3,4,3,2,3,1,2,1,1,2,3,2])}')
    print(f'the 20th percentile of {[1,2,3,4,3,2,3,1,2,1,1,2,3,2]} is {quantile([1,2,3,4,3,2,3,1,2,1,1,2,3,2], 0.2)}')
    print(f'the IQR of {[1,2,3,4,3,2,3,1,2,1,1,2,3,2]} is {interquartile_range([1,2,3,4,3,2,3,1,2,1,1,2,3,2])}')