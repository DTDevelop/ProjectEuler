"""
Largest prime factor
Problem 3
"""

import sympy
#utilize Python library, SymPy, for symbolic mathematics


# HELPER FUNCTIONS

# sympy.isprime(n)
"""
if n is prime number, returns boolean
"""

# sympy.primerange(a,b)
"""
generates list of all prime numbers in range [a, b)
notation: including a, not including b
"""

# sympy.primefactors(n)
"""
returns list of prime factors of given integer
"""

"""
QUESTIONS / SOLUTIONS
"""
# the prime factors of 13195 are 5, 7, 13, and 29

print('\n')
print('prime factors of 13195')
print(sympy.primefactors(13195))
print('\n')

# what is the largest prime factor of the number 600851475143 ?

print('largest prime factor of 600851475143')
print(sympy.primefactors(600851475143).pop())
