# List of common values
# U5W2
# Solution

# Set Lists for testing
array1 = list(range(3,100,3)) # these lists are interchangeable
array2 = list(range(2,100,2)) # these lists are interchangeable

# IPO
common_array = [] # initialization

for n in array1:
    if n in array2:
        common_array.append(n)

print('Common Values: %s' % common_array)
