word = list(input("Enter a word to mess with: "))
print(word)
jason_repeated = {}
for char in word:
    if char in jason_repeated:
        jason_repeated[char] += 1
    else:
        jason_repeated[char] = 1

jason_repeated_sorted = sorted(jason_repeated.items(), key=lambda val: val[1], reverse=True)
print(jason_repeated_sorted[0])
