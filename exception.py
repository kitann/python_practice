# EXCEPTION terminates the execution of a program
try:
    numb = float(input('What Year is it?: '))
    the_divide = 10 / numb
    print(the_divide)

# Different EXCEPTIONS CAN BE MERGED IN PARENTHESIS
except (ValueError, ZeroDivisionError):

    # The error message to be printed if error is encountered during execution
    print("Invalid entry, Try Again!!!")
else:

    # Message to be printed after a successful execution
    print("Valid year entered!!")

