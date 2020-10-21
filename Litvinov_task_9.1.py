############### 0)
import os

def mkdict (path = os.getcwd()):
    list_dir = os.listdir(path)
    files = []
    folders = []
    for item in list_dir:
        if os.path.isfile(item):
            files.append(item)
        else:
            folders.append(item)
    path_dict = {'files': files, 'folders': folders}
    return path_dict

############### 1)
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

def get_name():
    name_list = []
    for line in get_death_birthday():
        my_name_line = line.split('-')[1]
        my_date_line = line.split('-')[0]
        if "'" in my_name_line:
            name_dict = {'name': my_name_line.split("'")[0], 'date': my_date_line}
            name_list.append(name_dict)
        elif 'Dostoyevsky' in my_name_line:
            name_dict = {'name': my_name_line.split(" d")[0], 'date': my_date_line}
            name_list.append(name_dict)
        else:
            name_dict = {'name': my_name_line.split(" a")[0], 'date': my_date_line}
            name_list.append(name_dict)
    return name_list

get_name()

# def help_func():
#     my_list_1 = ['birthday']
#     my_list_3 = ['death']
#     my_list_2 = get_death_birthday()
#     name_list_1 = []
#     name_list_2 = []
#     for line in my_list_2:
#         my_date_line = line.split('-')[0]
#         my_name_line = line.split('-')[1]
#         for i in my_name_line.split():
#             name = my_name_line.split("'")[0]
#             i = i.lower()
#             i = i.replace(',', '')
#             if i in my_list_1:
#                 name_dict = {'name': name, 'b_date': my_date_line, 'd_date': ''}
#                 name_list_1.append(name_dict)
#             elif i in my_list_3:
#                 name_dict = {'d_date': my_date_line}
#                 name_list_2.append(name_dict)
#     return name_list_2

# print(help_func())
############# 2)
def get_dicts():
    print(*get_name(), sep='\n')
# get_dicts()
# ############ 3)
def get_list_dicts():
    print(get_name())
# get_list_dicts()
############## 4)
def get_dicts_2():
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

    dict_d = {}
    for item in day_d:
        itempars = item.split('-')[0].strip()
        key = item.split('-')[1].split("death")[0].strip()
        value = itempars
        dict_d.update({key: value})

    dict_back = [{"Name": key, "B_day": dict_b.get(key), "D_day": dict_d.get(key)} for key in dict_b.keys() | dict_d.keys()]
    return dict_back

# print(*get_dicts_2(), sep='\n')
