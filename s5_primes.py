# List of Primes under N
# U5W2
# Solution

# IPO
upper = int(input('Enter the value of N: '))

''' Solution Thoughts:
We will be iterating throught 2 to upper,
If any of those numbers are a prime then we add it to a list.
'''

primes = [2,3] # initialization w/ first 2 Primes
# this is to make our life a little easier...

for num in range(4, upper+1):

    # prime checker
    isPrime = True
    divider = 2
    while isPrime and divider < num:
        if num % divider == 0:
            isPrime = False
        divider += 1
    # end of prime checker

    if isPrime:
        primes.append(num)
    # if after the prime checker, num did not change the prime flag
    # then it is prime
# end of for loop

print('Primes:')
for i in primes:
    print(i)
