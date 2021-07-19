numbers = [1, 2 ,1, 3, 4, 5, 5, 7, 7, 7]

for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers[j]:
            print(numbers[i], " is a duplicate")
            break
