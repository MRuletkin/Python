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
value = input('Введите число с запятой: ')
try:
    value = float(value)
    new_value = value ** -1
    print(new_value)
except(ValueError):
    print('Это не число')
except(ZeroDivisionError):
    print('На ноль делить нельзя')
except:
    print('Что-то не так')
############################## 5)








