# Family Names
names = [
    "Saheed Adeoye",
    "Azeezat Animashaun",
    "Amirat Bamgboye",
    "Tayibat Animashaun",
    "Adl Adeoye",
    "Adam Adeoye"
]
# Birth Place
birth_place = [
    "Osogbo",
    "Surulere",
    "Brooklyn",
    "Ilorin",
    "Kansas City",
    "Liberty"
]
# Family Age
age = [
    "01/11/1983",
    "04/18/1986",
    "09/17/2009",
    "01/20/1970",
    "04/14/2017",
    "05/08/2020"
]
# Using zip() function
family_data = list(zip(names, birth_place, age, "MFFFMM"))
father = family_data[0]
mother = family_data[1]
grandma = family_data[2]
daughter = family_data[3]
first_son = family_data[4]
second_son = family_data[5]
# print(family_data[0] + family_data[1])
# print(family_data)
# print(family_data[::-1])

def male_in_family():
    print("================================================")
    print("             MALE FAMILY MEMBER")
    print("================================================")
    for char in family_data:
        if 'M' in char:
            print(char)
        # else:
        #     print(char)


male_in_family()
# ===========================================================

# FUNCTION TO RETRIEVE FEMALE MEMBERS


def female_in_family():
    print("================================================")
    print("             FEMALE FAMILY MEMBER")
    print("================================================")
    for char in family_data:
        if 'F' in char:
            print(char)
        # else:
        #     print(char)


female_in_family()
