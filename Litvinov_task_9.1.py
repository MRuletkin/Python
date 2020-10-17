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


def help_func():
    my_list_1 = ['birthday', 'death']
    my_list_2 = get_death_birthday()
    name_list = []
    for line in my_list_2:
        my_date_line = line.split('-')[0]
        my_name_line = line.split('-')[1]
        for i in my_name_line.split():
            name = my_name_line.split("'")[0]
            i = i.lower()
            i = i.replace(',', '')
            if i in my_list_1:
                name_dict = {'name': name, 'date': my_date_line}
                name_list.append(name_dict)
    return name_list
print(help_func())
# ############# 2)
def get_dicts():
    print(*help_func(), sep='\n')
get_dicts()

# ############ 3)
def get_list_dicts():
    print(help_func())
get_list_dicts()


# def get_name():
#     names = []
#     my_list = get_death_birthday()
#     for line in my_list:
#         my_name_line = line.split('-')[1]
#         for _ in my_name_line:
#             if _ == "'":
#                 name = my_name_line.split("'")[0]
#                 names.append(name)
#     return names
# #
# # print(len(get_name()))
#
# def get_date():
#     dates = []
#     my_list = get_death_birthday()
#     for line in my_list:
#         for elem in line:
#             if elem == "'":
#                 date = line.split("-")[0]
#                 dates.append(date)
#     return dates
# #
# # print(get_date())

