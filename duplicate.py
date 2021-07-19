numbers = [3, 6, 2, 4, 3, 6, 8, 9]
duplicate = None

for i in range(len(numbers)):           # n^2 operation
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            duplicate = numbers[i]
            break

for i in range(len(numbers)):           # n operation
    if numbers[i] == duplicate:
        print(i)


for i in range(len(numbers)):
    if numbers[i] == 9:
        print(f"The index is {i}")


big_number = list(range(1, 1000))
print(big_number)