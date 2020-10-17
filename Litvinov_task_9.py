############### 0)
# import os
#
# def mkdict (path = os.getcwd()):
#     list_dir = os.listdir(path)
#     files = []
#     folders = []
#     for item in list_dir:
#         if os.path.isfile(item):
#             files.append(item)
#         else:
#             folders.append(item)
#     path_dict = {'files': files, 'folders': folders}
#     return path_dict
#
# path_dict = mkdict()
# print(path_dict)

################ 1)
# import time
def get_death_birthday():
    new_list = []
    my_list = ['birthday', 'death']
    open_file = open('authors.txt')
    for line in open_file.readlines():
        for s in line.split():
            if s.replace(',', '') in my_list and s.lower() in my_list:
                new_list.append(line.strip())
    return new_list
# print(get_death_birthday())

############### 2)
def get_dicts():
    my_list_1 = ['birthday', 'death']
    my_list_2 = get_death_birthday()
    for line in my_list_2:
        # my_date_line = line.split('-')[0]
        my_name_line = line.split('-')[1]
        for i in my_name_line.split():
            i = i.replace(',', '')
            i = i.lower()
            if i in my_list_1:
                name_dict = {'name': my_name_line.split(i)[0]}
                return name_dict


mm = get_dicts()
print(mm)

############# 3)








