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
triangle = {'A': (),
            'B': (),
            'C': ()}
for key in triangle:
    triangle[key] = tuple([randint(1, 10) for _ in range(3)])

print(triangle)
#
# ################### 3)
# my_string = 'qwerty'
# def my_print(string):
#     new_string = '***' + string + '***'
#     return new_string
#
# print(my_print(my_string))
#
# ################### 4)
# my_dict_1 = {f'key_{a}': a ** 2 for a in range(7)}
# my_dict_2 = {f'key_{b}': b ** 3 for b in range(2, 6)}
# #
# # ### a)
# my_list = [*set(my_dict_1).intersection(set(my_dict_2))]
# print(my_list)
# # new_list = [key for key in my_dict_1 if key in my_dict_2]
# # print(new_list)
# #
# # ### б)
# my_list = [*set(my_dict_1).difference(set(my_dict_2))]
# print(my_list)
# # new_list = [key for key in my_dict_1 if key not in my_dict_2]
# # print(new_list)
#
# ### в)
# new_dict = {f'{key}': my_dict_1[key] for key in my_dict_1 if key not in my_dict_2}
# print(new_dict)
#
# ### г)
# my_dict_2['key_7'] = 50
# new_dict = {}
# union_dict = {**my_dict_1, **my_dict_2}
# for key in set(my_dict_1.keys()).symmetric_difference(my_dict_2.keys()):
#     new_dict.update({key: union_dict.get(key)})
# for key in set(my_dict_1.keys()).intersection(my_dict_2.keys()):
#     new_dict[key] = my_dict_1[key], my_dict_2[key]
#
# print(new_dict)







