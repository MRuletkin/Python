################## 1)
num = 505000
num = str(num)
print(num.count('0'))

################## 2)
num = 505000
num = str(num)
my_num = num[::-1]
count = 0
for symbol in my_num:
    if symbol == '0':
        count += 1
    else:
        break
print(count)

################## 3)
my_list_1 = [1, 2, 3, 4, 5, 7, 8]
my_list_2 = [10, 15, 20, 25, 5]
my_result = []
for symbol in my_list_1[1::2]:
    my_result.append(symbol)
for symbol_2 in my_list_2[::2]:
    my_result.append(symbol_2)
print(my_result)

################### 4)
my_list = [1, 2, 3, 4]
new_list = []
for symbol in my_list[1:]:
    new_list.append(symbol)
new_list.extend(my_list[:1])
print(new_list)

################## 5)
my_list = [1, 2, 3, 4]
my_list.append(my_list.pop(0))
print(my_list)

################## 6)
my_str = '43 больше чем 34 но меньше чем 56 и все это равно 133'
numbers = my_str.split(' ')
sum = 0
for symbol in numbers:
    if symbol.isdigit():
        symbol = int(symbol)
        sum += symbol
print(sum)

################### 7)
my_str = 'abcde'
my_list = []
if len(my_str) % 2 != 0:
    my_str += '_'
for symbol in range(0, len(my_str), 2):
    my_list.append(my_str[symbol: symbol + 2])
print(my_list)

################### 8)
my_str = 'My_long str'
l_limit = 'o'
r_limit = 't'
index_1 = my_str.find(l_limit)
index_2 = my_str.find(r_limit)
sub_str = my_str[index_1 + 1 : index_2]
print(sub_str)

#################### 9)
my_str = 'My_long string'
l_limit = 'o'
r_limit = 'g'
index_1 = my_str.find(l_limit)
index_2 = my_str.rfind(r_limit)
sub_str = my_str[index_1 + 1 : index_2]
print(sub_str)

##################### 10)
my_list = [2, 4, 1, 5, 3, 9, 0, 7]
my_result = []
for symbol in my_list[1:-2]:
    if my_list[my_list.index(symbol)] > my_list[my_list.index(4) + 1] + my_list[my_list.index(4) - 1]:
        my_result.append(symbol)
print(len(my_result))



# for index in range(len(my_list)):
#     if index != 0 and index != (-1) and my_list[index] > (my_list[index - 1] + my_list[index + 1]):
#         my_result.append(my_list[index])
# print(len(my_result))






