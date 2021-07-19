# HERE IS AN EXAMPLE OF HOW TO FIND THE TIME IT TAKES TO RUN YOUR CODE
# THIS IS GOING TO BE VERY USEFUL IF YOU HAVE A SET OF PROGRAMS TO RUN AND WANT TO HAVE AN IDEA OF THE RUN TIME
# I WILL WRITE TWO PROGRAMS HERE AND GET THE TIME TO RUN BOTH

from timeit import timeit

this_code = """
numbers = list(range(35))

# USING LIST COMPREHENSION,  SAVE THE ANSWER IN THE VARIABLE <result>
result = [num ** 2 for num in numbers]
print(result)

# NOW LET'S ADD A LITTLE WORKLOAD ON THE CODE
for num in result:
    if num % 3 == 0:
        print(num, "is divisible by 3")
    elif num % 10 == 0:
        print(num, "is divisible by 10")
    else:
        print(num)
"""

# print("Time to Execute Code = ", timeit(this_code, number=20000))

# SEE IT TOOK 11 SECOND TO RUN THE CODE, SO BE CAREFUL OF THE TYPE OF LOOPS OR RUNTIME YOU WILL PUT ON YOUR PROCESSORS
# THOUGH THIS CODE WILL NOT HAVE ADVERSE EFFECT IF YOU HAVE JUST FEW USERS, WHEN IT RUNS INTO A MILLION, THERE
# WILL SURELY BE PERFORMANCE ISSUES AND THIS IS JUST A SIMPLE PROGRAM, THERE CAN BE RELATIVELY LARGER
# MORE COMPLEX CODES.
# THANKS FOR WATCHING!!!

import timeit

setup = """
import pydash
list_of_objs = [
    {},
    {'a': 1, 'b': 2, 0: 0},
    {'a': 1, 'c': 1, 'p': lambda x: x}
]
"""
print(timeit.timeit("pydash.filter_(list_of_objs, {'a': 1})", setup=setup))