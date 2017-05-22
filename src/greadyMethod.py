import numpy as np

def selectMove(grid):
	move = np.random.randint(4)
	reward = 0
	for i in range(4):
		a = computeReward(grid, i)
		if a > reward:
			reward = a
			move = i
	return move
		
def computeReward(grid, move):
	"""
	Simulates the given move on the given grid and returns the
	expected reward.
	"""
	reward = 0
	tmp = -1
	if move == 0:
		for i in range(4):
			reward += computeRowReward(grid[:,i])
	elif move == 1:
		for i in range(4):
			reward += computeRowReward(grid[i,::-1])
	elif move == 2:
		for i in range(4):
			reward += computeRowReward(grid[::-1,i])
	else:
		for i in range(4):
			reward += computeRowReward(grid[i,:])
	return reward

def computeRowReward(row):
	"""
	Computes the reward that is returned for the given row, when the
	numbers collapes to the left of the given row
	"""
	# Delete all empty cells
	row2 = []
	for i in row:
		if (i != -1):
			row2.append(i)
	
	# Explicitely compute the reward for the different cases
	# According to the rules a number can only be merged once per move!
	reward = 0
	if (len(row2) > 1 and row2[0] == row2[1]):
		reward += 2*row2[0]
		if (len(row) == 4 and row2[2] == row2[3]):
			reward += 2*row2[2]
	elif (len(row2) > 2 and row2[1] == row2[2]):
		reward += 2*row2[1]
	elif (len(row2) == 4 and row2[2] == row2[3]):
		reward += 2*row2[2]
	return reward
