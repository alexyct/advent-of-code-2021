import numpy as np
import pandas as pd
from os import path

with open(path.join(path.dirname(__file__), "day5.txt")) as f:
    data = list(x.strip() for x in f)

# Part 1

# floor = [[0]*1000 for _ in range(1000)]

# for lines in data:
# 	coords_start = lines.split(' ')[0]
# 	x1 = int(coords_start.split(',')[0])
# 	y1 = int(coords_start.split(',')[1])
# 	coords_end = lines.split(' ')[2]
# 	x2 = int(coords_end.split(',')[0])
# 	y2 = int(coords_end.split(',')[1])


# 	if x1 == x2:
# 		for y in range(min(y1,y2), max(y1,y2)+1):
# 			floor[x1][y] +=1 

# 	if y1 == y2:
# 		for x in range(min(x1,x2), max(x1,x2)+1):
# 			floor[x][y1] += 1 

# result = 0
# for row in floor:
# 	result += sum(i > 1 for i in row)

# print(result)

# Part 2

floor = [[0]*1000 for _ in range(1000)]

for lines in data:
	coords_start = lines.split(' ')[0]
	x1 = int(coords_start.split(',')[0])
	y1 = int(coords_start.split(',')[1])
	coords_end = lines.split(' ')[2]
	x2 = int(coords_end.split(',')[0])
	y2 = int(coords_end.split(',')[1])


	if x1 == x2:
		for y in range(min(y1,y2), max(y1,y2)+1):
			floor[x1][y] +=1 

	elif y1 == y2:
		for x in range(min(x1,x2), max(x1,x2)+1):
			floor[x][y1] += 1 

	else:
		for i in range(max(x1,x2)-min(x1,x2)+1):
			if x1 > x2:
				if y1 > y2:
					floor[x1-i][y1-i] += 1
				else:
					floor[x1-i][y1+i] += 1
			else:
				if y1 > y2:
					floor[x1+i][y1-i] += 1
				else:
					floor[x1+i][y1+i] += 1


result = 0
for row in floor:
	result += sum(i > 1 for i in row)

print(result)