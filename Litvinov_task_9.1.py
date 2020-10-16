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
                new_list.append(line)
    return new_list


print(get_death_birthday())
# get_death_birthday()