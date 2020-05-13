# List of Random Numbers
# U5W2
# Solution

from random import randrange as randRange

# IPO
lower = int(input('Enter the lower bound: '))
upper = int(input('Enter the upper bound: '))
size = int(input('Enter how many random values you would like: '))

rand_list = [] # empty list initialization
for i in range(size):
    rand_list.append(randRange(lower,upper))

print('Random List: %s' % rand_list)
