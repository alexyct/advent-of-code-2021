import numpy as np
import pandas as pd

df = pd.read_csv('day1.csv', names=["col1"])  
df['col2'] = df['col1'].shift()
df['col3'] = df['col2'].shift()
df['col4'] = df['col1'] + df['col2'] + df['col3']

def countIncrease(df,column):
    print(sum(df[column].pct_change().fillna(0) > 0))

countIncrease(df, 'col1')
countIncrease(df, 'col4')