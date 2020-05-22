# Project Euler Problem 4: Largest Palindrome Product of 3 Digits Multiples
# U5W3
# Grade 11 Solution

# Step 1 --> Create a list of 3 digit numbers
data = list(range(100,1000))

# Step 2 --> Double for loop through data and multiply each number combos
# Step 3 --> if that product is a palindrome add it to a palindrome list
# Step 4 --> find the largest value in that list

palindromes = []

for num1 in data:
    for num2 in data:
        # Product Finder
        product = num1 * num2

        # Palindrome Check
        str_product = str(product)
        if str_product == str_product[::-1]:
            palindromes.append(product)
# end of palindromes list maker

print(max(palindromes))
