# importing libraries
import pandas as pd
import numpy as np

# setting the seed for random variables
np.random.seed(4)

# read the data
data_set = pd.read_csv('mp_inputs.csv')
cols = data_set.shape[1]

# Initialize the variables
w = np.random.randint(0, 4, (cols - 1))
theta = 0

# initialize the wis'
w_s = [f'w{i + 1}' for i in range(cols)]

# loop that does the logical part
for i in range(data_set.shape[0]):
	row = data_set.iloc[i, :].values
	x = np.array(row[:-1])
	y = row[-1]
	eqn = x * w
	eqn_sum = np.sum(eqn)

	# below if prints the equations
	if eqn_sum == 0:
		print('0', end=' ')
	else:
		[print(w_s[idx], end=' ') for idx in range(cols - 1) if eqn[idx] != 0]
	print('< theta ------', i + 1) if y == 0 else print('>= theta ------', i + 1)

	# this if is basically the logic
	if y == 0 and eqn_sum >= theta:  # eqn < theta
		theta = eqn_sum + 1
	elif y == 1 and eqn_sum < theta:  # eqn >= theta
		theta = eqn_sum

print()
# printing the values of weights and theta
[print(f'W{i + 1} = {v}') for i, v in enumerate(w)]
print(f'Theta = {theta}')
