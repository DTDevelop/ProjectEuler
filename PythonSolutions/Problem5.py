"""
Smalest multiple
Problem 5
"""

# HELPER FUNCTIONS

def smallest_multiple(min, max):
    """
    takes min / max
    returns smallest positive num evenly divisible by all numbers in range
    """

    smallest_multiple = None
    current_check = max # begins at max value, ensures divisibility of atleast largest value

    while smallest_multiple == None:

        for num in range(min, max+1): # up to, but not including, so add 1

            if current_check % num > 0: # if check not evenly divisible
                current_check += 1 # increment for next positive num
                break
            if num == max:
                smallest_multiple = current_check # number is evenly divisible by all numbers in range, breaks loop

        if current_check >= 500000000:
            break # run time safety net

    return smallest_multiple



"""
QUESTIONS / SOLUTIONS
"""
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder

print('\n')
print('smallest number that can be divided by each of the numbers from 1 to 10 without any remainder')
answer = smallest_multiple(1, 10)
print(answer)
print('\n')

# what is the smallest positive number that is evenly divisible by all the numbers from 1 to 20

print('smallest positive number that is evenly divisible by all the numbers from 1 to 20')
answer = smallest_multiple(1, 20)
print(answer)
print('\n')




















#
