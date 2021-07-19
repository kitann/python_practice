# my_dict = {x: x * 2 for x in range(20)}
# print(my_dict)
#
# my_values = [x * 2 for x in range(10)]
# print(my_values)
# for x in my_values:
#     print(x)
#
# tuple_value =  (x ** 2 for x in range(30))
# print(tuple_value)

from sys import getsizeof
gen_object = (x + 5 for x in range(20000000))
gen_object_two = (x + 5 for x in range(100000000))
list_object = [x + 5 for x in range(20000000)]
print(getsizeof(list_object))
print(gen_object)
print(getsizeof(gen_object))
print(getsizeof(gen_object_two))