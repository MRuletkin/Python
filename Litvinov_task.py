######################### 1)
value = int(input('Введите число: '))
new_value = value / 2 if value < 100 else value * (-1)
print(new_value)
######################### 2)
value = int(input('Введите число: '))
new_value = 1 if value < 100 else 0
print(new_value)
########################## 3)
value = int(input('Введите число: '))
new_value = 1 if value < 100 else 0
print(bool(new_value))
####################### 4)
my_str = 'ArDuiNo'
print(my_str.upper())
######################### 5)
my_str = 'ArDuiNo'
print(my_str.lower())
######################### 6)
my_str = input('Введите что-нибудь: ')
if len(my_str) < 5:
    print(my_str * 2)
else:
    print(my_str)
######################## 7)
my_str = input('Введите что-нибудь: ')
if len(my_str) < 5:
    print(my_str + my_str[:-1])
else:
    print(my_str)
####################### 8)
my_str = 'P ! t h 0 n @'
for i in my_str:
    if i.isalnum():
        print(i)
####################### 9)
my_str = 'P ! t h 0 n @'
for i in my_str:
    if not i.isalnum():
        print(i)
####################### 10)
my_str = 'P ! t h 0 n @'
for i in my_str:
    if not i.isalnum() and not i.isspace():
        print(i)




