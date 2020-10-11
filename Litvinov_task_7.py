################ 1)
from random import randint
# my_list = [randint(1, 100) for _ in range(20)]
# print(my_list)
#
# my_list = []
# for _ in range(20):
#     my_list.append(randint(1, 100))
# print(my_list)
#
# ##################### 2)
# triangle = {'A': (),
#             'B': (),
#             'C': ()}
# for key in triangle:
#     triangle[key] = tuple([randint(1, 10) for _ in range(3)])
#
# print(triangle)
#
# ################### 3)
# my_string = 'qwerty'
# def my_print(string):
#     new_string = '***' + string + '***'
#     return new_string
#
# print(my_print(my_string))

################### 4)
my_dict_1 = {f'key_{a}': a ** 2 for a in range(7)}
my_dict_2 = {f'key_{b}': b ** 3 for b in range(2, 6)}
# print(my_dict_1)
# print(my_dict_2)
#
# ### a)
# my_set_1 = set(my_dict_1)
# my_set_2 = set(my_dict_2)
# my_list = [*my_set_1.intersection(my_set_2)]
# print(my_list)
# new_list = [key for key in my_dict_1 if key in my_dict_2]
# print(new_list)
#
# ### b)
# new_list = [key for key in my_dict_1 if key not in my_dict_2]
# print(new_list)

### c)
# new_dict = {f'key_{key}': my_dict_1[key] for key in my_dict_1 if key not in my_dict_2}
# print(new_dict)

### d)
my_dict_2['key_7'] = 50
new_dict = {}
my_set_1 = set(my_dict_1.keys()).symmetric_difference(my_dict_2.keys())
my_set_2 = set(my_dict_1.keys()).intersection(my_dict_2.keys())
union_dict = {**my_dict_1, **my_dict_2}

for key in my_set_1:
    new_dict[key] = union_dict[key]
for key in my_set_2:
    new_dict[key] = my_dict_1[key], my_dict_2[key]

print(new_dict)







