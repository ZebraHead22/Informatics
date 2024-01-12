import os
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

file = "./files/Mall_Customers.csv"

df = pd.DataFrame()

df = pd.read_csv(file, delimiter=",", index_col=None)
# df = df.set_index('Genre')
df = df[df['Genre'] == "Male"]
df.insert(1,'TEST', df['Age']*30)

print(df.where(df['Age'] >= 40).unique().dropna().head())

