# Mean Median Mode
# U5W3
# Solution

# Since we can't easily input lists
# we will have a testing list
test = [3, 8, 3, 2, 1, 5, 8, 6, 5, 9]
test = [7, 1, 10, 7, 7, 2, 6, 7, 6, 2] # uncomment this line to try a different list

# Mean
# Total sum / number of items
mean = sum(test) / len(test)

# Median
# Sorted ... middle most value
# Depends on the number of items
median = 0 # initilization
test_sorted = sorted(test) # sorted function returns the list sorted
i = len(test_sorted) // 2 # middle index i

if len(test_sorted) % 2 == 0:
    # even number of items
    median = (test_sorted[i] + test_sorted[i-1]) / 2
else:
    median = test_sorted[i]

# Mode
# Most occurring value
# Our definition: if there are more than 1 value that occurs the "most"
# there are no Mode

mode = 0 # initialization
max_count = 0
mode_status = True # will turn False if there are ties
tested = [] # a list that tracks the numbers that were tested

for item in test:
    if item not in tested:
        tested.append(item)
        current_count = test.count(item)

        if current_count > max_count:
            mode_status = True # reupdate incase it turned false
            mode = item
            max_count = current_count
        elif current_count == max_count:
            mode_status = False
# end of mode check

print('Our list: %s' % test)
print('Mean: %f' % mean)
print('Median: %f' % median)

if mode_status:
    print('Mode: %s' % mode)
else:
    print('No Mode')
