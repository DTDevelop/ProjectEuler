"""
Multiples of 3 and 5
Problem 1
"""

# If we list all natural numbers below 10

def natural_numbers(max_value):
    """
    given maximum value
    returns list of natural numbers below that value
    """
    natural_nums = []
    for wanted_num in range(1,max_value):
        natural_nums.append(wanted_num)

    return natural_nums

natural_number_list = natural_numbers(10)
print('\n')
print('all natural numbers below 10')
print(natural_number_list)
print('\n')

# that are multiples of 3 or 5
# creating a new list while checking existing list

def multiples_check(number_list, constraint_one, constraint_two):
    """
    given a number list and multiple constraint
    returns new list
    """

    new_nums = []
    for number in number_list:
        if number % constraint_one == 0 or number % constraint_two == 0:
            new_nums.append(number)

    return new_nums

short_num_list = multiples_check(natural_number_list, 3, 5)
print('all natural numbers below 10 that are multiples of 3 or 5')
print(short_num_list)
print('\n')

# we get 3, 5, 6, 9
# the sum of these multiples is 23

def sum_of_list(my_list):
    """
    calculates the sum of the given list
    returns sum
    """

    # using built-in function
    sum_of_list = sum(my_list)

    # or own loop
    # sum = 0
    # for num in my_list:
    #   sum += num
    return sum_of_list


print('sum of the multiples for all natural numbers below 10 that are multiples of 3 or 5')
print(sum_of_list(short_num_list))



## QUESTION:
# find the sum of all multiplpes of 3 or 5 below 1000






























#
