########################### 1)
my_list = ['123', 'abc', 'next', '890']
new_list = []
for index, value in enumerate(my_list):
    if index % 2 == 0:
        new_list.append(value[::-1])
    else:
        new_list.append(value)
print(new_list)

############################### 2)
my_list = ['abc', 'aug', 'back', 'auto', 'car', 'bed', 'sad']
new_list = [value for value in my_list if value[0] == 'a']
print(new_list)

# # ######################### 3)
my_list = ['abc', 'aug', 'back', 'auto', 'car', 'bed', 'sad']
new_list = [value for value in my_list if 'a' in value]
print(new_list)

# ####################### 4)
my_list = ['abc', 'aug', 'back', 99, 14, 'lol', 25]
new_list = [value for value in my_list if type(value) == str]
print(new_list)

# ######################## 5)
my_str = 'aabcdde'
new_list = [symbol for symbol in my_str if my_str.count(symbol) == 1]
print(new_list)

###################### 6)
my_str_1 = '1224343'
my_str_2 = '4565512'
new_list = []
set_str = set(my_str_1).intersection(my_str_2)
print(list(set_str))

###################### 7)
my_str_1 = '1534346'
my_str_2 = '4568811'
set_str = set(my_str_1).intersection(my_str_2)
new_list = [s for s in set_str if my_str_1.count(s) == 1 and my_str_2.count(s) == 1]
print(new_list)

##################### 8)
residence = {'country': 'Ukraine',
             'city': 'Dnipro',
             'street': 'Polya'}

work = {'existence': False,
        'position': 'Junior'}

somebody = {'name': 'Michael',
            'age': 19,
            'residence': residence,
            'work': work}

print(somebody['residence'])

##################### 9)
Massa = {10: '10 грамм',
         50: '50 грамм',
         100: '100 грамм',
         200: '200 грамм',
         500: '500 грамм',
         1000: '1 кг',
         'Kol-vo': '4 шт.'}

Korji = {'Мука': Massa[200],
         'Молоко': Massa[1000],
         'Масло': Massa[100],
         'Яйцо': Massa['Kol-vo']}

Krem = {'Сахар': Massa[1000],
        'Масло': Massa[50],
        'Ваниль': Massa[10],
        'Сметана': Massa[200]}

Glazur = {'Какао': Massa[100],
          'Сахар': Massa[200],
          'Масло': Massa[50]}

Components = {'Корж': Korji,
              'Крем': Krem,
              'Глазурь': Glazur}

Tort = {'Торт': Components}
print(Tort)
