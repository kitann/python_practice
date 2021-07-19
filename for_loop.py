# THIS IS A SIMPLE FOR LOOP EXAMPLE IN PYTHON
# THE CODE IS DESIGNED TO SEND EMAIL TO A RECIPIENT'S EMAIL ADDRESS
# IF THERE WAS A SUCCESSFUL ATTEMPT, WE WILL TERMINATE THE LOOP
# IF NOT WE WILL EXECUTE THE ELSE STATEMENT AND PRINT THE COMMENT
# ENJOY!!!!! :D

successful = True

# I WILL DEFINE NUMBER OF ATTEMPTS HERE
# LET'S MAKE IT FUN BY ASKING USER TO ENTER EMAIL ADDRESS AND HOW MANY TIMES WE WANT IT TO BE SENT

email_address = input("Enter recipient's email address: ")

# THIS WILL BE AN INTEGER SO I WILL INDICATE HERE IN A SECOND
trials = int(input("Enter the amount of time you want to try the email: "))

for number in range(trials):
    # WE WANT A LITTLE SPACE BETWEEN INPUTS AND OUTPUT HENCE THE \n
    print(f"\nAttempting to send email to {email_address}")
    # THIS LINE WILL CHECK THE CONDITION FOR SUCCESS
    if successful:
        print("\n============================================")
        print(f"Email SUCCESSFULLY sent to {email_address}")
        print("\n============================================")
        break

# IF THE ATTEMPT TO SEND THE EMAIL WAS UNSUCCESSFUL, WE DO THIS LINE
else:
    # LETS'S MAKE IT A LITTLE INVITING ;)
    print("\n=======================================")
    print(f"Email delivery to {email_address} FAILED after {trials} attempts")

# WE WILL RUN THE CODE NOW, THANKS FOR WATCHING, MORE TO COME!!!!
# THE EXAMPLE IS ABOUT A FAILED ATTEMPT, I WILL ADJUST THE BOOLEAN AND EXECUTE FOR SUCCESS

