# BIG o NOTATION
# O(n)
try:
    def get_squared_list(numbers):
        squared_list = []
        for num in numbers:
            squared_list.append(num ** num)
        return squared_list

    numbers = range(1, 10)
    result = get_squared_list(numbers)
    print(result)

except TypeError as the_error:
    print("ERROR Occurred")
    print("Error Description:>>> ", the_error)
