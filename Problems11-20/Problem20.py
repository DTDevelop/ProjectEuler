"""
Factorial digit sum
Problem 20
"""

import math # using factorial function

# or

# HELPER FUNCTIONS

def calc_factorial(number):
    """
    given number
    returns factorial
    """
    fact_num = 1
    current_num = 1

    while current_num < number:
        fact_num *= current_num
        current_num += 1

    return fact_num

# MAIN FUNCTIONS

def sum_of_digits(number):
    """
    given number
    returns sum of digits
    """
    num_str = str(number)
    current_ind = 0
    sum = 0

    while current_ind < len(num_str):
        sum += int(num_str[current_ind])
        current_ind += 1

    return sum



"""
QUESTIONS / SOLUTIONS
"""

# n! means n * (n - 1) * ... * 3 * 2 * 1

# eg. 10! == 10 * 9 * ... * 3 * 2 * 1 = 3628800
# sum of the digits in the number 10! == 27

our_num = calc_factorial(10)
print(our_num)
print(sum_of_digits(our_num))

#find the sum of the digits in the number 100!

our_num = calc_factorial(100)
print(our_num)
print(sum_of_digits(our_num))
