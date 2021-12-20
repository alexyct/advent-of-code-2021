import numpy as np
import pandas as pd
from os import path

with open(path.join(path.dirname(__file__), "day4.txt")) as f:
    data = list(x.strip() for x in f)
    # data = f.readlines()

# Part 1

WINNING_PATTERNS = [
[0,1,2,3,4],
[5,6,7,8,9],
[10,11,12,13,14],
[15,16,17,18,19],
[20,21,22,23,24],
[0,5,10,15,20],
[1,6,11,16,21],
[2,7,12,17,22],
[3,8,13,18,23],
[4,9,14,19,24]
]


data = [string for string in data if string != ""]
sequence = data[0].split(',')
boards = [data[x:x+5] for x in range(1, len(data),5)]

final_boards = []
for board in boards:
	new_board = []
	for row in board:
		new_row = row.split(' ')
		new_board.append(new_row)
	new_board = [item for row in new_board for item in row]
	final_board = [string for string in new_board if string != ""]
	final_boards.append(final_board)


scores = [WINNING_PATTERNS] * len(final_boards)
finished = False
winning_board = []
winning_number = 0
winning_index = 0

# for number in sequence:
# 	for i in range(len(final_boards)):
# 		if number in final_boards[i]:
# 			scores[i] = [[ele for ele in sub_list if ele != final_boards[i].index(number)] for sub_list in scores[i]]
# 			if not all(v for v in scores[i]):
# 				winning_board = final_boards[i]
# 				winning_number = number
# 				finished = True
# 				break
# 	if finished:
# 		winning_index = sequence.index(number)
# 		break

# for number in sequence[:winning_index+1]:
# 	if number in winning_board:
# 		winning_board.remove(number)


winning_board = list(map(int, winning_board))
print(sum(winning_board)*int(winning_number))

# Part 2

won = [0] * len(final_boards)
finding = True
for number in sequence:
	print('-----------')
	print(number)
	for i in range(len(final_boards)):
		if number in final_boards[i]:
			scores[i] = [[ele for ele in sub_list if ele != final_boards[i].index(number)] for sub_list in scores[i]]
			if not all(v for v in scores[i]):
				won[i] = 1
	print(won)
	if finding:
		if sum(won) == 99:
			losing_board = final_boards[won.index(0)]
			finding = False
	if sum(won) == 100:
		losing_number = number
		losing_index = sequence.index(number)
		break 

for number in sequence[:losing_index+1]:
	if number in losing_board:
		losing_board.remove(number)

losing_board = list(map(int, losing_board))
print(losing_number)
print(losing_board)
print(sum(losing_board)*int(losing_number))

