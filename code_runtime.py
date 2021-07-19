from timeit import  timeit

#========================CODE 1===================================#
code_one = """
try:
    file = open("closing_file_exception.py")
    first_num = float(input('Enter a value:>>> '))
    second_num = float(input('Enter a second value:>>> '))
    entry = first_num / second_num
    print("Answer is:>>> ", entry)
# when operation FAILS, this error is thrown
except (ValueError, ZeroDivisionError) as the_error:
    print("WRONG ENTRY!!!")
    print("Error Type:>>> ", the_error)
# ELSE is executed when the condition FAILS to throw exception
else:
    print("Operation was SUCCESSFUL")
# FINALLY release external resources
finally:
    file.close()
    print("File is closed")
"""

#======================CODE 2=========================================#
code_two = """
def age_calc(age):
    if age <= 0:
        raise ValueError("Age can not be ZERO")
    return 10/age

try:
    age_calc(-8)
except ValueError as error:
    print(error)
"""

print("Code 1 time to run =", timeit(code_one, number=3))
print("Code 2 time to run =", timeit(code_two, number=10000))

from timeit import timeit

the_code = """
def integer_calc(first_integer, second_integer):
    first_integer = int(input('Enter any WHOLE number:~$ '))
    second_integer = int(input('Enter another WHOLE number:~$ '))
    if first_integer <= 0:
        print("Check your INPUT!!!")
        raise ZeroDivisionError("Division by ZERO not allowed")

    integer_addition = first_integer / second_integer
    return integer_addition


try:
    integer_calc(first_integer=True, second_integer=True)
except (ValueError, ZeroDivisionError) as the_error:
    print("Error Description:>>> ", the_error)
    print("INTEGER expected!!!")
"""

print("Time to run: ", timeit(the_code, number=1))
