import numpy as np
import pandas as pd
import os

os.chdir(r"/Users/seiyanishikawa/Documents/python_scripts")
df = pd.read_csv('sample2.csv')

df['Total'] = df.sum(axis = 1)
print(df)

print(df.describe())