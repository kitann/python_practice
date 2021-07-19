
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


