"""
Created on Tue Apr  4 23:49:26 2023

@author: thfosk
"""

import os
import numpy as np
import pandas as pd

#import the data
features = pd.read_csv('features.txt', delimiter='\t', header=None)
labels = pd.read_csv('labels.txt', delimiter='\t', header=0)
# convert to dataframes
df = pd.DataFrame(features)
labels_df = pd.DataFrame(labels)

# index sample col
labels_df.set_index('Sample', inplace=True)

# Drop chromosome column and Nclone
df = df.drop(df.columns[[0, 3]], axis=1)

# join  start end columns with ":"
df[1] = df[[1, 2]].apply(lambda x: ':'.join(map(str, x)), axis=1)

# drop column 2
df = df.drop(2, axis=1)

# # Transpose the data
train_df = df.T

# index sample col
train_df.set_index(0, inplace=True)

# merge labels and
Training_set = pd.merge(train_df, labels_df, left_index=True, right_index=True)


