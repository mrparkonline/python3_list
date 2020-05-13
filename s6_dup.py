# Removing duplicate values
# U5W2
# Solution

''' Solution Thoughts:
Iterate through the list,
add each item to the new list if we have not added it to the list yet
'''

array = list('hello world, this is my testing value')

# IPO
clean_array = [] # initialization

for item in array:
    if item not in clean_array:
        clean_array.append(item)

print('Original ... size: %d\n%s\n' % (len(array), array))
print('Cleaned ... size: %d\n%s' % (len(clean_array), clean_array))
