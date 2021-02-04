"""
Even Fibonacci numbers
Problem 2
"""

# HELPER FUNCTIONS

def fibonacci_sequence_gen_one(desired_len, start_list):
    """
    given desired length and starting list
    returns list of fibonacci seq. numbers
    """

    my_numbers = start_list
    while len(my_numbers) < desired_len:
        new_value = my_numbers[-1] + my_numbers[-2]
        my_numbers.append(new_value)

    return my_numbers

def fibonacci_sequence_gen_two(num_ceiling, start_list):
    """
    given max value and starting list
    returns fibonacci sequence up to that maximum
    **
    current max value: 573147844013817084101
    configure while loop for higher values
    """

    my_numbers = start_list
    while len(my_numbers) < 100: #timeout safeguard, max value: 573147844013817084101
        new_value = my_numbers[-1] + my_numbers[-2]
        if new_value > num_ceiling:
            break
        my_numbers.append(new_value)

    return my_numbers

def sum_of_even(my_list):
    """
    given a list of int
    returns sum of even valued terms
    """

    sum = 0
    for num in my_list:
        if num % 2 == 0:
            sum += num

    return sum



"""
QUESTIONS / SOLUTIONS
"""

# each new term in fibonacci sequence is generated by adding the previous two terms.
# by starting with 1 and 2, the first 10 terms will be

print('\n')
print('first 10 terms of fibonacci sequence starting with 1 and 2')
print(fibonacci_sequence_gen_one(10, [1,2]))


# by considering the terms in fobnacci sequence whose values do not exceed four million
# find the sum of even-valued terms

print('\n')
print('sum of even-valued terms in Fibonacci sequence whose values do not exceed four million')
print(sum_of_even(fibonacci_sequence_gen_two(4000000, [1,2])))
print('\n')























#