my_dict = {'Anna:': 18 , 'Daniel:': 22}
print(my_dict)
print(my_dict.get('Anna:'), my_dict.get('Amy'))
my_dict.update({'Amy:': 19 , 'Rachel:': 21})
my_dict.pop('Daniel:')
print(my_dict)

my_set = {'apples', 1,2,3,4, True, 'awesome'}
print(my_set)
my_set.add('Pie')
my_set.add('Banana')
my_set.remove('apples')
print(my_set)