any_expression = list(input("Enter a word: "))

number_repeated = {}

for num in any_expression:
    if num in number_repeated:
        number_repeated[num] += 1
    else:
        number_repeated[num] = 1

number_repeated_sorted = sorted(number_repeated.items(), key=lambda value: value[1], reverse=True)

print(number_repeated_sorted[0])