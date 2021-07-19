people_weight = {'saheed': 123,
                 'james': 200,
                 'fruits': ['banana', 'mango', {'amirat': 100}],
                 'tuple': (2, 4, 6, 8)}
my_tuple = people_weight['tuple']

tuple_removed = people_weight.pop('tuple')
print(people_weight)