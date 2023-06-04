"""
Created on Tue Apr  4 23:49:26 2023

@author: thfosk
"""

import os
import numpy as np
import pandas as pd

# import the data
features = pd.read_csv('Validation_call.txt', delimiter='\t', header=None)

# convert to dataframes
df = pd.DataFrame(features)

# Drop chromosome column and Nclone
df = df.drop(df.columns[[0, 3]], axis=1)

# join  start end columns with "-"
df[1] = df[[1, 2]].apply(lambda x: '-'.join(map(str, x)), axis=1)

# drop column 2
df = df.drop(2, axis=1)

# # Transpose the data
predict_df = df.T
predict_df.set_index(0, inplace=True)



predict_df.to_csv('Validation_clear.csv', index=True, header= False)

#%%
