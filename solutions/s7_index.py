# Searching for a value in a List
# U5W2
# Solution

# IPO
array = list('hello world') # our testing list
target = 'o' # our testing target
###################################

i = 0 # our indexing variable
not_found = True # our looping flag
location = 0

while not_found and i < len(array):
    if array[i] == target:
        not_found = False
        location = i

    i += 1

if not not_found:
    print('%s is found at index of %d.' %( target, location))
else:
    print('%s is not found' % target)
