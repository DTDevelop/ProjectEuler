"""
Sum square difference
Problem 6
"""

# HELPER FUNCTIONS

def sum_of_squares(num_list):
    """
    input number list
    returns sum of squares
    """

    return sum_of_squares

def square_of_sum(num_list):
    """
    input number list
    returns square of sum
    """

    return square_of_sum


"""
QUESTIONS / SOLUTIONS
"""

# the sum of the squares of the first ten natural numbers is,
# 1**2 + 2**2 + .. + 10**2 = 385

print('\n')
print('the sum of the squares of the first ten natural numbers')
my_list = range(1,11)
q1_answer = sum_of_squares(my_list)
print(q1_answer))
print('\n')

# the square of the sum of the first ten natural numbers is,
# (1 + 2 + .. + 10)**2 = 55**2 = 3025

print('the square of the sum of the first ten natural numbers')
q2_answer = square_of_sum(my_list)
print(q2_answer))
print('\n')

# hence the difference between the sum of the squares
# of the first ten natural numbers and the square of the
# sum is 3025 - 385 = 2640

print('difference between sum of squares of first ten natural numbers and the square of the sum')
print(q2_answer - q1_answer)
print('\n')

# find the difference between the sum of
# the squares of the first one hundred natural numbers
# and the square of the sum

print('difference between sum of squares of the first one hundred natural numbers and square of the sum')
my_list = range(1,101)
sum_of_squares = sum_of_squares(my_list)
square_of_sum = square_of_sum(my_list)
print(square_of_sum - sum_of_squares)
print('\n')
