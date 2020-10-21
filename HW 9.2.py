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


a_list = [{'name': ' Mark Twain', 'b_date': '30th November 1835'}, {'name': ' J. D. Salinger', 'd_date': '1st January 1919'}]
b_list = [{'name': ' Mark Twain', 'd_date': '16th December 1775'}, {'name': ' J. R. R. Tolkien', 'date': '3rd January 1892'}]

for index in range(len(a_list)):
    a_list[index].update(b_list[index])
# print(a_list)
def help_func_1():
    my_list_2 = get_death_birthday()
    name_list = []
    for line in my_list_2:
        my_date_line = line.split('-')[0]
        my_name_line = line.split('-')[1]
        for i in my_name_line.split():
            name = my_name_line.split("'")[0]
            i = i.lower()
            i = i.replace(',', '')
            if i == 'birthday':
                name_dict = {'name': name, 'b_date': my_date_line}
                name_list.append(name_dict)
            elif i == 'death':
                name_dict = {'name': name}
                name_list.append(name_dict)
    return name_list

def help_func_2():
    my_list_2 = get_death_birthday()
    name_list = []
    for line in my_list_2:
        my_date_line = line.split('-')[0]
        my_name_line = line.split('-')[1]
        for i in my_name_line.split():
            name = my_name_line.split("'")[0]
            i = i.lower()
            i = i.replace(',', '')
            if i == 'death':
                name_dict = {'name': name, 'd_date': my_date_line}
                name_list.append(name_dict)
            elif i == 'birthday':
                name_dict = {'name': name}
                name_list.append(name_dict)
    return name_list

def help_func_3():
    my_list_2 = get_death_birthday()
    name_list_1 = []
    for line in my_list_2:
        my_date_line = line.split('-')[0]
        my_name_line = line.split('-')[1]
        for i in my_name_line.split():
            name = my_name_line.split("'")[0]
            i = i.lower()
            i = i.replace(',', '')
            if i == 'birthday' or i == 'death':
                name_dict = {'name': name}
                name_list_1.append(name_dict)
    return name_list_1

def help_func_4():
    birth_list = help_func_1()
    death_list = help_func_2()
    big_list = help_func_3()
    try:
        for index in range(len(big_list)):
            big_list[index].update(birth_list[index])
            big_list[index].update(death_list[index])
    except:
        pass
    return big_list


# def get_dicts():
#     print(*help_func_1(), sep='\n')
# get_dicts()
#
# def get_dicts():
#      print(*help_func_3(), sep='\n')
# get_dicts()
