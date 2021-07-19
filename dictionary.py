# Instructor: SAHEED
# Data Structure: DICTIONARY
# Other methods: FUNCTION

# i will begin by defining the data structure and variable to hold the information
# i will define the function here.
# Now that we have defined the function
# set the variable and invoked the condition, let's run the code

def human_profile():
    my_names = input("Enter FIRST and LAST names, separated by a comma: ")
    my_address = input("Enter your ADDRESS: ")
    my_number = input("Enter PHONE NUMBER: ")
    my_city = input("Enter CITY: ")
    my_state = input("Enter STATE: ")
    my_zipcode = int(input("Enter 5 digits ZIP CODE: "))

    # This code will print the two lines to give a little space between USER_INPUT and the ACTUAL_OUTPUT
    # Let's run the code now
    print("=============================================")
    print("=============================================")

    profile = dict(names=my_names,
                   address=my_address,
                   phone_number=my_number,
                   city=my_city,
                   state=my_state,
                   zip_code=my_zipcode)

    for key, value in profile.items():
        print(key, ":", value)

# it did what we want but I will wrap it in function and just make it a little pretty
# This should print all KEYS and VALUES in the profile
# I will call the function here

# that is not the output I expected, I will look at the code and fix it,
# it is an important skill to be able to make a mistake and fix it
# professionally
# That's exactly what we want to see but we can modify this like i said earlier.
# thanks for watching!!! :D
# This is the power of Dictionary, Function and User Input


human_profile()

