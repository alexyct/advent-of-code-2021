import numpy as np
import pandas as pd
from os import path

with open(path.join(path.dirname(__file__), "day3.txt")) as f:
    data = list(x.strip() for x in f)

# Part 1

df = pd.read_csv('day3.csv',dtype=str, names=["col1"])  
df = df['col1'].apply(lambda x: pd.Series(list(x)))

gamma = ""
epsilon = ""
counts = df[df == "0" ].count()

for i in range(len(counts)):
	if counts[i] > 500:
		gamma += "0"
		epsilon += "1"
	else:
		gamma += "1"
		epsilon += "0"

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)

print(gamma*epsilon)

# Part 2

df = pd.read_csv('day3.csv',dtype=str, names=["col1"])  
df = df['col1'].apply(lambda x: pd.Series(list(x)))

df_ogr = df
df_csr = df

for i in range(df.shape[1]-1):
	if df_ogr.shape[0] == 1:
		break
	if df_ogr[i].value_counts()["0"] > df_ogr[i].value_counts()["1"]:
		df_ogr = df_ogr[df_ogr[i] != "1"]
	else:
		df_ogr=df_ogr[df_ogr[i] != "0"]


for i in range(df.shape[1]-1):
	if df_csr.shape[0] == 1:
		break
	if df_csr[i].value_counts()["0"] > df_csr[i].value_counts()["1"]:
		df_csr = df_csr[df_csr[i] != "0"]
	else:
		df_csr = df_csr[df_csr[i] != "1"]

ogr = int(''.join(df_ogr.values.flatten().tolist()),2)
csr = int(''.join(df_csr.values.flatten().tolist()),2)

print(ogr*csr)
