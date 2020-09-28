############################ 1)
# my_list = [50, 99, 100, 150, 199, 200]
# for symbol in my_list:
#     if symbol > 100:
#         print(symbol)
#     else:
#         None
########################### 2)
# my_list = [50, 99, 100, 150, 199, 200]
# my_results = []
# for symbol in my_list:
#     if symbol > 100:
#         my_results.append(symbol)
#     else:
#         None
# print(my_results)
############################ 3)
# my_list = []
# n = int(input('Введите кол-во целочисленных элементов в списке: '))
# for symbol in range(n):
#     element = int(input('Введите элемент: '))
#     my_list.append(element)
# print(my_list)
# if len(my_list) < 2:
#     my_list.append(0)
#     print(my_list)
# else:
#     print(my_list[-1] + my_list[-2])
############################## 4)
# value = input('Введите число с запятой: ')
# try:
#     value = float(value)
#     new_value = value ** -1
#     print(new_value)
# except(ValueError):
#     print('Это не число')
# except(ZeroDivisionError):
#     print('На ноль делить нельзя')
############################## 5)
# my_indexes = [0, 1, 2, 3, 4]
# my_list = 'qwert'
# for index in my_indexes:
# 	print(my_list[index])
############################# 6)
# my_indexes = [0, 1, 2, 3, 4]
# my_list_1 = 'qwert'
# my_list_2 = 'asdfg'
# for index in my_indexes:
#     print(my_list_1[index], my_list_2[index])
############################# 7)
my_string_1 = '0123456789'
my_string_2 = my_string_1[:]
new_list = []
for symbol_1 in my_string_1:
    for symbol_2 in my_string_2:
        elem = symbol_1 + symbol_2
        elem = int(elem)
        new_list.append(elem)
print(new_list)












