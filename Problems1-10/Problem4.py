"""
Largest palindrome product
Problem 4
"""

# HELPER FUNCTIONS

def is_palindrome(num):
    """
    checks if number is palindrome
    returns boolean
    """
    our_number = str(num)
    num_len = len(our_number)

    is_palindrome = True
    for check in range(num_len//2): #checking number at index
        if our_number[check] != our_number[-(check+1)]:
            is_palindrome = False
            break

    return is_palindrome

def largest_palindrome(min, max):
    """
    given min and max
    calculate products of all those values
    returns largest palindrome
    """

    largest_palindrome = 0

    for x_num in range(min, max):
        for y_num in range(min, max):
            product = x_num*y_num
            if is_palindrome(product) and product > largest_palindrome:
                largest_palindrome = product

    return largest_palindrome



"""
QUESTIONS / SOLUTIONS
"""

# a palindromic number reads the same both ways
# the largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99

print("\n")
print('largest palindrome made from product of two 2-digit numbers')
print(largest_palindrome(10, 100))
print('\n')

# find the largest palindrome made from the product of two 3-digit numbers

# looking for the largest 3 digit palindrome

print('largest palindrome made from product of two 3-digit numbers')
print(largest_palindrome(100, 1000))
print('\n')

























#
