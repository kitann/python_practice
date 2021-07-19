from pprint import pprint
array_expense = {
    "January": 2200,
    "February": 2350,
    "March": 2600,
    "April": 2130,
    "May": 2190,
    "September": 2000
}

#===================================================QUESTION 1==========================================================
# In Feb, how many dollars extra did you spend compared to january

print(type(array_expense))
print(
    "1. Difference between JANUARY and FEBRUARY expenses is: $",
      array_expense["February"] - array_expense["January"]
      )

#===================================================QUESTION 2==========================================================
# Find out your total expense in first quarter (first 3 months ) of the year

first_quarter = array_expense["January"] + array_expense["February"] + array_expense["March"]
print("2. Amount spent first quarter is $",first_quarter)

#===================================================QUESTION 3==========================================================
# find out if you spent exactly 2000 in any month

exact_amount = 2000
for expense in range(len(array_expense)):
    if expense == exact_amount:
        print(expense)
    else:
        print(f"3. There is no ${exact_amount} expense during any month")
        break

#===================================================QUESTION 4==========================================================
# June just finished and your expense is 1980 dollars, add this item to our monthly expense list

array_expense["June"] = 1980
print("4. June expense ADDED: ", array_expense)

#===================================================QUESTION 5==========================================================
# You returned an item you bought in April and got a refund of $200, correct the expense list based on this

array_expense["April"] = 2130 + 200
print("5. April expense after refund is received is: $",array_expense["April"])

#===================================================QUESTION 6==========================================================
# Print all DIVISIONS between any given range

first_num = int(input('Enter lower boundary:>>> '))
second_num = int(input('Enter upper boundary:>>> '))
divisor = float(input('Enter DIVISOR:>>> '))
divisions = [i for i in range(first_num, second_num) if i % divisor == 0]
pprint(f"6. The result of {first_num} and {second_num}, divided by {divisor} is: {divisions}")

if 55 in range(len(divisions)):
    the_index = divisions.index(55)
    print(the_index)