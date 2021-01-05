"""
10001st prime
Problem 7
"""

# HELPER FUNCTIONS

def is_prime(num):
    """
    given number, checks if prime number
    returns boolean
    """
    if num < 0:
        is_prime = False # if negeative number, return False
        return is_prime

    is_prime = True

    divide_list = range(2,num) # divides against all values except for 1 and itself
    for check in divide_list:
        if num % check == 0:
            is_prime = False # if composite number, return False
            break

    return is_prime

# test case
# known prime numbers from question: 2, 3, 5, 7, 11, 13
# are the following prime numbers or not? [2, 3, 5, 7, 11, 13], [4, 6, 8, 9, 10, 12]
# print(is_prime(2), is_prime(3), is_prime(5), is_prime(7), is_prime(11), is_prime(13))
# print(is_prime(4), is_prime(6), is_prime(8), is_prime(9), is_prime(10), is_prime(12))

# expected output:
# True True True True True True
# False False False False False False

# actual output:
# True True True True True True
# False False False False False False

def prime_list(length, num):
    """
    given length
    calculating from num and incrementing
    returns list of prime numbers of desired length
    """

    prime_list = []
    current_check = num

    while len(prime_list) < length:
        if is_prime(current_check):
            prime_list.append(current_check)
        current_check += 1

    return prime_list

# test case
# known prime numbers from question: 2, 3, 5, 7, 11, 13
# return a list of prime numbers up to length 6, starting at 2
print(prime_list(6,2))

# expected output:
# [2, 3, 5, 7, 11, 13]

# actual output:
# [2, 3, 5, 7, 11, 13]

def return_prime_v1(ind):
    """
    given index
    returns prime number at index
    """

    return prime_number

"""
QUESTIONS / SOLUTIONS
"""

# by listing the first six prime numbers:
# 2, 3, 5, 7, 11, and 13, we can see the 6th prime is 13

print('\n')
print('what is the 13th prime number')
our_index = 6
print(return_prime_v1(our_index))

# what is the 10 0001st prime number?

print('\n')
print('what is the 10 001st prime number')
our_index = 10001
print(return_prime_v1(our_index))
