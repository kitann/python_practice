sentence = "this is a common interview question"

char_repeated = {}

for char in sentence:
    if char in char_repeated:
        char_repeated[char] += 1
    else:
        char_repeated[char] = 1

char_repeated_sorted = sorted(char_repeated.items(), key=lambda value: value[1], reverse=True)

# SORTED result
print(char_repeated_sorted)
print("Most occurred character is:>>> ", char_repeated_sorted[0])
print(type(char_repeated_sorted))

# DICTIONARY result
char_frequency = dict(char_repeated_sorted)
print(type(char_frequency))

new_char = dict(char_repeated_sorted)
print(type(char))
print(type(new_char))