from timeit import timeit

the_code = """
try:

    def get_squared_list(numbers):
        squared_list = []
        for num in numbers:
            squared_list.append(num ** num)
        return squared_list


    numbers = list(range(1, 10))
    result = get_squared_list(numbers)
    print(result)

    result_dict = dict(result)
    print(type(result_dict))
except TypeError as the_error:
    print("ERROR Occurred")
    print("Error Description:>>> ", the_error)"""

print("Time to run = ", timeit(the_code, number=1))