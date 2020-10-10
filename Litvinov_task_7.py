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

################### 4)
my_dict_1 = {f"key_{a}": a ** 2 for a in range(7)}
my_dict_2 = {f"key_{b}": b ** 2 for b in range(2,6)}
#
# ### a)
# new_list = [key for key in my_dict_1 if key in my_dict_2]
# print(new_list)
#
# ### b)
# new_list = [key for key in my_dict_1 if key not in my_dict_2]
# print(new_list)

### c)
# new_dict = {}
# for key in my_dict_1:
#     if key in my_dict_2:
#         print(key, my_dict_1[key]



