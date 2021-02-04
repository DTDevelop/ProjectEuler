"""
Power digit sum
Problem 16
"""

def sum_of_digits(number):
    """
    given number
    return sum of digits
    """
    our_number = str(number)
    sum = 0
    current_ind = 0
    # convert to string, for every element, convert to int, add

    for value in our_number:
        sum += int(value)

    return sum


"""
QUESTIONS / SOLUTIONS
"""

# 2**15 = 322768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26

# test case
# we know, sum of digits for 2**15 == 26
print('\n')
print(sum_of_digits(2**15))

# expected output:
# 26

# actual output:
# 26

# what is the sum of the digits of the number 2**1000

print('\n')
print('what is the sum of the digits of the number 2**1000')
print(sum_of_digits(2**1000))
print('\n')
