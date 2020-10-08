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
# new_list = [value for value in my_list if value[0] == 'a']
# print(new_list)
# #
# # ######################### 3)
# my_list = ['abc', 'aug', 'back', 'auto', 'car', 'bed', 'sad']
# new_list = [value for value in my_list if 'a' in value]
# print(new_list)
#
# ####################### 4)
# my_list = ['abc', 'aug', 'back', 99, 14, 'lol', 25]
# new_list = [value for value in my_list if type(value) == str]
# print(new_list)
# ######################## 5)
#
# my_str = '122343'
# new_list = [symbol for symbol in my_str if my_str.count(symbol) == 1]
# print(new_list)
#
# my_str = '122343'
# new_list = []
# for symbol in set(my_str):
#     new_list.append(symbol)
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
# my_str_1 = '1534346'
# my_str_2 = '4568811'
# new_list = []
# for symbol in my_str_1:
#     if my_str_1.count(symbol) == 1 and symbol in my_str_2 and my_str_2.count(symbol) == 1:
#         new_list.append(symbol)
# print(new_list)

##################### 8)
# residence = {'country': 'Ukraine',
#              'city': 'Dnipro',
#              'street': 'Polya'}
# work = {'existence': False,
#         'position': 'Junior'}
# somebody = {'name': 'Michael',
#             'age': 19,
#             'residence': residence,
#             'work': work}
#
# print(somebody['residence'])

##################### 9)
KG = {50 : "50 грамм",
      100: "100 грамм",
      200: "0,2 кг",
      500: "0,5 кг",
      1000: "Один кг"}
Korj = {"Мука": KG[200],
        "Молоко": KG[1000],
        "Масло": "150 г.",
        "Яйцо": "3 шт."}
Krem =  {"Сахар": KG[1000],
        "Масло": "50 г.",
        "Ваниль": "0,02 Кг.",
        "Сметана": "3 Ст.Л."}
Glazur = {"Какао": "1 стакан",
        "Сахар": "0,15 Кг.",
        "Масло": "30 г."}
Ing_step = {"Корж": Korj,
            "Крем": Krem,
            "Глазурь": Glazur}
Tort = {"Состовляющие торта": Ing_step}
