import pandas as pd
import numpy as np
import datetime as dt

# import file
df = pd.read_csv("../marambio_2007.dat",
                 sep="\s+")
# create new stats df
stats = pd.DataFrame(index=['Prom', 'Max', 'Min', 'Med'], columns=df.columns)
# fill new df for each climate model
for col in df:
    stats[col][0] = df[col].mean()
    stats[col][1] = df[col].max()
    stats[col][2] = df[col].min()
    stats[col][3] = df[col].median()

print(list(stats.columns))
print(stats)
