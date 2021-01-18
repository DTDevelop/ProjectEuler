"""
Lattice paths
Problem 15
"""

def paths(x, y):
    """
    given x and y dimensions for a grid
    while restricting movements to right/down
    return number of possible paths to the bottom right corner
    """

    return number_of_paths

"""
QUESTIONS / SOLUTIONS
"""

# starting from the top left corner of a 2x2 grid
# only being able to move right and down
# there are exactly 6 routes to the bottom right corner

# TEST CASE

print('')
print('number of paths for a 2x2 grid')
possible_paths = paths(2,2)
print(possible_paths)

# expected output:
# 6

# how many such routes are there through a 20x20 grid?

print('')
print('number of paths for a 20x20 grid')
possible_paths = paths(20,20)
print(possible_paths)

"""
NOTES
"""

# use recursion
# dynamic programming: solves once, bottom up
# memoization: solves once, top down
