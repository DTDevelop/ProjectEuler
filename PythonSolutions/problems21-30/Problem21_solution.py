"""
Amicable numbers
Problem 21
"""

import math
# output still wrong
# removing prime numbers outputs, remove duplicates, remove items == self
# ensure f(n) = a and f(a) = n
# not sure where to go next..


# HELPER FUNCTIONS

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

def amicable_pair(num):
    """
    given number
    returns the amicable pairing if possible
    else returns None
    """
    if is_prime(num): # no amicable pair
        return

    amicable_pair = 0
    current_divisor = 0

    while current_divisor <= num/2:
        current_divisor += 1
        if num % current_divisor == 0:
            amicable_pair += current_divisor

    # if amicable pair = itself
    if amicable_pair != num:
        return amicable_pair
    else:
        return

# test case
# we know, d(220) = 284
# print(amicable_pair(284))

# expected output:
# 284
# actual output:
# 284

# num = [5, 1184, 2620, 5020, 6232, 10744, 12285]
#
# for i in num:
#     print(amicable_pair(i))

# expected output:
# None, 1210, 2924, 5564, 6368, 10856, 14595
# actual output:
# None, 1210, 2924, 5564, 6368, 10856, 14595

# MAIN FUNCTIONS

def sum_of_amicable_numbers(max):
    """
    given maximum
    returns sum of amicable numbers below
    """
    # amicable_numbers_check = set([]) # checking all amicable pairs
    #

    checked_values = set([])
    current_check = 0
    sum_of_numbers = 0
    while current_check < max:
        current_check += 1

        if current_check in checked_values: #skip value if already used
            continue

        pairing = amicable_pair(current_check)
        if pairing == None or pairing < current_check:
            # no value or pairing doesn't result in f(n) = a, f(a) = n
            continue

        if pairing > current_check:
            checked_values.add(pairing)
        # amicable_numbers_check.add(current_check)# checking all amicable pairs
        # amicable_numbers_check.add(pairing)# checking all amicable pairs
        sum_of_numbers += (current_check + pairing)
    #
    # print(amicable_numbers_check)
    return sum_of_numbers

"""
QUESTIONS / SOLUTIONS
"""

# let d(n) be defined as the sum of proper divisors of n
# ( numbers less than n which divide evenly into n )

# if d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair
# each of a and b are called amicable numbers

# eg.
# proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110
# therefore d(220) = 284
# proper divisors of 284 are 1, 2, 4, 71 and 142
# therefore d(284) = 220

# evaluate the sum of all the amicable numbers under 10000

print('')
print('the sum of all the amicable numbers under 10000')
print(sum_of_amicable_numbers(10000))
print('')

"""
Notes
"""

# find proper divisors of given number
# calculate sum of proper divisors
# == amicable pair / number

# decision to use either set or dict over list
# https://stackoverflow.com/questions/513882/python-list-vs-dict-for-look-up-table

# ccareful checking amicable pairs of prime numbers
# make sure able to find amicable pair ( ensure f(n) = a and f(a) = n )
# test whether all amicable numbers may be found before adding
