import numpy as np

# inputs
X = []
d = []
W = []
c = 1
high = 1
low = -1

print('[INPUT SECTION]')
no_of_inputs = int(input('Enter the number of Inputs: '))

for i in range(no_of_inputs):
    x_i = np.array(list(map(float, input(f'Enter the value of X{i + 1}: ').split())))
    d_i = int(input(f'Enter the value of d{i + 1}: '))
    if d_i == 0:
        low = 0
    X.append(x_i)
    d.append(d_i)

W = np.array(list(map(float, input('Enter the Weights: ').split())))
c = float(input('Enter the Value of constant: '))

epochs = int(input('Enter the No. of Epochs: '))

# Logic of the program
print('\n[PROCESSING / INTERMEDIATE OUTPUTS]')
for epoch in range(epochs):
    print('\nOn Epoch:', epoch + 1)
    for i in range(no_of_inputs):
        print('\n\tSTEP:', i + 1)
        x_i = X[i]
        d_i = d[i]
        print(f'\tX{i + 1}: {x_i}\n\td{i + 1}: {d_i}')
        net = round(np.sum(np.dot(W, x_i.T)), 2)
        O = low if net < 0 else high
        print(f'\tNet is {net} thus O is {O}')
        delta_w = 0
        if d_i != O:
            print(f"\tSince {d_i} != {O} hence change weights")
            delta_w = c * (d_i - O) * x_i
        else:
            print(f"\tSince {d_i} = {O} hence same weights")
        print('\tDelta(W) is', delta_w)
        print(f'\tUpdated Weights i.e. {W} + {delta_w} = ', end='')
        W += delta_w
        print(W)

# Final output
print('\n[OUTPUT]\nFinal Weights:', W)

