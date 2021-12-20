import numpy as np
import pandas as pd
from os import path

with open(path.join(path.dirname(__file__), "day2.txt")) as f:
    data = list(x.strip() for x in f)

# Part 1

df = pd.read_csv('day2.csv', names=["col1"])  

df[["direction","magnitude"]] = df["col1"].str.split(" ", 1, expand=True)
df['magnitude'] = df['magnitude'].astype(int)

forward = df.groupby('direction')['magnitude'].sum()['forward']
depth = df.groupby('direction')['magnitude'].sum()['down']-df.groupby('direction')['magnitude'].sum()['up']

print(forward*depth)

# Part 2

horizontal = 0
aim = 0
depth = 0
for command in data:
	direction = command.split(' ')[0]
	magnitude = int(command.split(' ')[1])
	if direction == 'forward':
		horizontal += magnitude
		depth += (magnitude * aim)
	elif direction == 'down':
		aim += magnitude
	elif direction == 'up':
		aim -= magnitude
print(horizontal*depth)