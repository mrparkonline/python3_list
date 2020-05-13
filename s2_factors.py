# Most Factors
# U5W2
# Solution

# input
num = int(input('Enter an upper limit: '))

# processing & output
''' Solution Process
We will be storing each number's list of factors in a List.

Therefore,
-- loop through from 1 to Num inclusively
-- Determine each number's factor List
-- Then re loop through the database to find the longest one
'''

factor_list = [] # empty initialization

for current_num in range(1,num+1):
    current_factors = []

    # The for loop on line 24 help us find the factors of current_num
    for i in range(1, current_num+1):
        if current_num % i == 0:
            # i is now a factor of current_num
            # so we append it to current_factors
            current_factors.append(i)
    # end of inner for
    # now we add the current_factor list to factor_list
    factor_list.append(current_factors)

    # after this iteration, current_factors will reset to empty while
    # maintaining the list inside the factor_list
# end of outer for

# Now we loop through each factor lists to see which is the longest
longest_length = 0
longest_factor = 0

for array in factor_list:
    temp = len(array)
    if temp > longest_length:
        longest_factor = array[-1] # the last value in that list generated the longest list
        longest_length = temp

print('%s generated the longest list of factors' % longest_factor)
print('%d: %s' % (longest_factor, factor_list[longest_factor-1]))
