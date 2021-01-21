# Basic Comma-Separated-Values to Numeric List
# U5W3
# Solution

# input
csv_input = input('Enter your comma-separated-values: ')

# processing & output

# 1. remove all whitespaces
# 2. split string to list by comma
data = csv_input.replace(' ','').split(',') # data is now a list of numeric strings

numeric_array = []

for item in data:
    numeric_array.append(int(item))

print('Original data: %s' % csv_input)
print('New List: %s' % numeric_array)

# in grade 12, this gets MUCH easier :)
