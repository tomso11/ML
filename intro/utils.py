import numpy as np
import pandas as pd
import math

# Method for splitting arrays in test and train arrays
def split_array(array, testsize=0.25, trainsize=0.75):
    if( testsize + trainsize != 1.0 ):
        testsize = 0.25
        trainsize = 0.75
    samples = len(array)
    ntrain = math.ceil(samples*trainsize)
    ntest = math.floor(samples*testsize)
    train = array[:ntrain]
    test = array[(samples-ntest):]

    return train, test

# test

# ary = [0, 1, 2, 3, 4, 5]
# a, b = split_array(ary, testsize=0.4, trainsize=0.6)
# print(a)
# print(b)

# Method for splitting dataframes in test and train dataframes
def split_df(df, testsize=0.25, trainsize=0.75):
    if( testsize + trainsize != 1.0 ):
        testsize = 0.25
        trainsize = 0.75
    samples = df.shape[0]
    ntrain = math.floor(samples*trainsize)
    ntest = samples - ntrain;
    train = df.loc[:(ntrain-1), :]
    test = df.loc[(samples-ntest):, :]

    return train, test

# test

# df = pd.DataFrame(np.random.randn(100, 4), columns=list('ABCD'))
# c, d = split_df(df, testsize=0.5,trainsize=0.5)
# print(c.shape[0])
# print(d.shape[0])
