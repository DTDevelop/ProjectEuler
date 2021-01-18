"""
Lattice paths
Problem 15
"""

# RUN TIME TOO HIGH WITH BRUTE FORCE
# HELPER FUNCTIONS
def container(dim_x, dim_y):
    """
    given x and y dimensions for a grid
    while restricting movements to right/down
    return number of possible paths to the bottom right corner
    """
    found_paths = 0

    def paths(x, y):

        nonlocal found_paths
        # base case
        if x == 0 or y == 0: # end of path ( reaching any 'wall' indicates so )
            found_paths += 1
            print(found_paths, 'PATHS FOUND !! ~~~~~~ !! ~~~~~~ !!')
            return

        # recursive case
        paths(x-1,y)
        paths(x,y-1)

        return

    paths(dim_x, dim_y)
    return found_paths

# USING PASCALS TRIANGLES
# reference: http://blog.functionalfun.net/2008/07/project-euler-problem-15-city-grids-and.html

# to calculate the current index, multiply value in previous list at [current_index] * [index-1]
# try: current_index, index-1
# else: value_1 || value_2 == 1

def pascal_triangle_paths(dimensions):
    """
    returns number of paths given even dimensions of grid
    """
    current_dimension = 0.5

    current_layer = [1,1]

    # using try /
    while current_dimension < dimensions:
        # calculate each new layer element with previous layer elements
        new_layer = []

        for ind in range(len(current_layer)+1): # add current index + previous index
            if ind - 1 == -1:
                x = 0
            else:
                x = current_layer[ind-1]
            try:
                y = current_layer[ind]
            except:
                y = 0
            new_value = x + y
            new_layer.append(new_value)
        current_layer = new_layer



        current_dimension += 0.5

    return (current_layer[(len(current_layer)//2)]) # half index mark

# TEST CASE
print(pascal_triangle_paths(2))
# expected output:
# 6

# actual output:
# 6


"""
QUESTIONS / SOLUTIONS
"""

# starting from the top left corner of a 2x2 grid
# only being able to move right and down
# there are exactly 6 routes to the bottom right corner

# TEST CASE

print('')
print('number of paths for a 2x2 grid')
possible_paths = container(2,2)
print(possible_paths)

# expected output:
# 6

# actual output:
# 6

# how many such routes are there through a 20x20 grid?

print('')
print('number of paths for a 20x20 grid') # takes too long, 'brute force'
possible_paths = pascal_triangle_paths(20)
print(possible_paths)

# """
# NOTES
# """

# use recursion
# dynamic programming: solves once, bottom up
# memoization: solves once, top down
# essentially want to count leaf nodes
