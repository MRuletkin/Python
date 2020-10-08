########################### 1)
# my_list = ['123', 'abc', 'next', '890']
# new_list = []
# for index, value in enumerate(my_list):
#     if index % 2 == 0:
#         new_list.append(value[::-1])
#     else:
#         new_list.append(value)
# print(new_list)

############################### 2)
# my_list = ['abc', 'aug', 'back', 'auto', 'car', 'bed', 'sad']
# new_list = []
# for index, value in enumerate(my_list):
#     if value[0] == 'a':
#         new_list.append(value)
# print(new_list)
#
# ######################### 3)
# my_list = ['abc', 'aug', 'back', 'auto', 'car', 'bed', 'sad']
# new_list = []
# for index, value in enumerate(my_list):
#     if 'a' in value:
#         new_list.append(value)
# print(new_list)

####################### 4)
# 'my_list = ['abc', 'aug', 'back', 99, 14, 'lol', 25]
# new_list = []
# for index, value in enumerate(my_list):
#     if type(value) == str:
#         new_list.append(value)
# print(new_list)'
######################## 5)

# my_str = '122343'
# new_list = []
# for symbol in my_str:
#     if my_str.count(symbol) == 1:
#         new_list.append(symbol)
# print(new_list)

###################### 6)
# my_str_1 = '122343'
# my_str_2 = '456551'
# new_list = []
# for symbol in my_str_1:
#     if my_str_1.count(symbol) == 1 and symbol in my_str_2:
#         new_list.append(symbol)
# print(new_list)

###################### 7)
my_str_1 = '1534346'
my_str_2 = '4568811'
new_list = []
for symbol in my_str_1:
    if my_str_1.count(symbol) == 1 and symbol in my_str_2 and my_str_2.count(symbol) == 1:
        new_list.append(symbol)
print(new_list)

##################### 8)
