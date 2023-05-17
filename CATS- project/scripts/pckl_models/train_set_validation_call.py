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

# Get the features that we want
selected_columns = ['69274433-70345552', '196908262-196937230', '19049822-20716660', '131304839-132036965',
                    '70574871-71644041', '97852156-98629015', '67314736-68371045', '35076296-35282086',
                    '41062669-41447005', '194755-763411'
                    ]  # List of column names to select
# to ekana xeirokinita na paei na gamithei
#predict_df.to_csv('Validation_clear.csv', index=True, header= False)

#%%
