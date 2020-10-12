############# 1)
def domains():
    domains = []
    open_file = open('domains.txt', 'r')
    for line in open_file.readlines():
        domen = line.strip().replace('.', '')
        domains.append(domen)
    return domains

list_domains = domains()
# print(list_domains)

############# 2)
def names():
    nationality = ['English', 'Spanish', 'Welsh', 'Irish', 'Scottish']
    new_list = []
    open_file = open('names.txt', 'r')
    for line in open_file.readlines():
        my_line = line.split()
        for line in my_line:
            if line not in nationality and line.isalpha():
                new_list.append(line)
    return new_list

list_names = names()
# print(list_names)

############## 3)
import random

def get_name():
    return random.choice(list_names)

def get_num():
    return str(random.randint(100, 999))

def get_letters():
    my_alphabet = []
    for index in range(ord('a'), ord('z') + 1):
        my_alphabet += chr(index)
    return ''.join(random.choice(my_alphabet) for i in range(random.randint(5, 7)))

# a = get_letter()
# print(a)

def get_domain():
    return random.choice(list_domains)

def get_email():
    return get_name() + '.' + get_num() + '@' + get_letters() + '.' + get_domain()
a = get_email()
print(a)


