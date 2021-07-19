student_first = input("First Name: ")
student_last = input("Last Name: ")
student_full = f"{student_first}, {student_last}"
eligibility_age = 18
choice_college = input("Specify College: ")
student_dob = int(input("Year of Birth: "))
accepted_dob = 2021 - student_dob
message_reject = f"Hey {student_full.capitalize()},\n We regret to inform you that you are INELIGIBLE to APPLY to  " \
                 f"{choice_college} \n on the ground of AGE, you are currently {accepted_dob} years old," \
                 f" you have to be {eligibility_age} \n old to QUALIFY"
message = f"Hey {student_first.capitalize()}, \n CONGRATULATIONS, You are ELIGIBLE to APPLY for the 2021 ADMISSION at" \
          f"{choice_college}, you met the AGE requirement" \
    else:
        f"{message_reject}"
print(message)
