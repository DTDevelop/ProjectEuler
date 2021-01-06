"""
Summation of primes
Problem 10
"""

import math
# use sqrt function

# HELPER FUNCTION

def is_prime(num):
    """
    given a positive natural number above 2, checks if prime number
    returns boolean
    """

    current_check = 2
    while current_check <= math.sqrt(num): # loops check for all required values
        if num % current_check == 0:
            return False # if composite, return false
        current_check += 1

    return True

# MAIN FUNCTION

def prime_sum(max):
    """
    given maximum
    return sum of the primes up to maximum
    """
    prime_sum = 0
    current_check = 2
    while current_check < max:
        if is_prime(current_check):
            prime_sum += current_check
        current_check += 1

    return prime_sum

# solutions no longer need to store values
# use values as they are calculated

"""
QUESTIONS / SOLUTIONS
"""

# test case
# the sum of the primes below 10 is 2 + 3 + 5 + 7 = 17

print('\n')
print('sum of the primes below 10')
print(prime_sum(10))

# expected output:
# 17

# find the sum of all the primes below two million

print('\n')
print('the sum of the primes below two million')
print(prime_sum(2000000))
