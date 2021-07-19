try:
    file = open("closing_file_exception.py")
    first_num = float(input('Enter a value:>>> '))
    second_num = float(input('Enter a second value:>>> '))
    entry = first_num / second_num
    print("=======================================")
    print("               SOLUTION")
    print("=======================================")
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

