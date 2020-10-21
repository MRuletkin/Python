def get_death_birthday():
    new_list = []
    my_list = ['birthday', 'death']
    open_file = open('authors.txt')
    for line in open_file.readlines():
        my_line = line.split()
        for i in my_line:
            i = i.replace(',', '')
            i = i.lower()
            if i in my_list:
                new_list.append(line.strip())
    return new_list

from parse import *

datal = []
for line in get_death_birthday():
    if "birthday" in line or "death" in line:
        datal.append(line.replace("\n", ""))

day_b = [line for line in datal if "birthday" in line]
day_d = [line for line in datal if "death" in line]

dict_b = {}
for item in day_b:
    itempars = item.split('-')[0].strip()
    key = item.split('-')[1].split("birthday")[0].strip()
    # value = parse.strftime('%Y/%m/%d')
    dict_b.update({key: itempars})
    # print(itempars)

dict_d = {}
for item in day_d:
    itempars = item.split('-')[0].strip()
    key = item.split('-')[1].split("death")[0].strip()
    try:
        value = itempars
    except:
        value = '1962/07/06'
    dict_d.update({key: value})

dict_back = [{"Name": key, "B_day": dict_b.get(key), "D_day": dict_d.get(key)} for key in dict_b.keys() | dict_d.keys()]
# print(*dict_back, sep='\n')
# return dict_back

datal = []
for line in get_death_birthday():
    if "birthday" in line or "death" in line:
        datal.append(line.replace("\n", ""))

day_b = [line for line in datal if "birthday" in line]
day_d = [line for line in datal if "death" in line]

dict_b = {}
for item in day_b:
    itempars = item.split('-')[0].strip()
    if 'th ' in  itempars:
        sep_line = ' '.join(itempars.split('th '))
    elif 'nd ' in itempars:
        sep_line = ' '.join(itempars.split('nd '))
    else:
        sep_line = ' '.join(itempars.split('st '))

line = ['18th December 1984', '17st March 1985']
my_list = []
for obj in line:
    line_1 = obj.split()
for i in line_1[0]:
    if i.isdigit():
        my_list.append(i)
        print(''.join(my_list))

