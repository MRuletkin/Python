############# 1)
def domains():
    domains = []
    open_file = open('domains.txt', 'r')
    for line in open_file.readlines():
        domen = line.strip().replace('.', '')
        domains.append(domen)
    return domains

# ############# 2)
# def names():
#     nationality = ['English', 'Spanish', 'Welsh', 'Irish', 'Scottish']
#     new_list = []
#     open_file = open('names.txt', 'r')
#     for line in open_file.readlines():
#         my_line = line.split()
#         for line in my_line:
#             if line not in nationality and line.isalpha():
#                 new_list.append(line)
#     return new_list
def names():
    name_list = []
    open_file = open('names.txt', 'r')
    for line in open_file.readlines():
        my_line = line.split()
        name_list.append(my_line[1])
    return name_list

# ############## 3)
import random

def get_name():
    return random.choice(names())

def get_num():
    return str(random.randint(100, 999))

def get_letters():
    my_alphabet = []
    for index in range(ord('a'), ord('z') + 1):
        my_alphabet += chr(index)
    return ''.join(random.choice(my_alphabet) for i in range(random.randint(5, 7)))

def get_domain():
    return random.choice(domains())

def get_email():
    return get_name() + '.' + get_num() + '@' + get_letters() + '.' + get_domain()

print(get_email())

################# 4)
number = 5
mask = 'xxx.xx.x.x'

from random import randint
def get_rand_0_255(mask=''):
    new_list = []
    if mask == '':
        return randint(0, 255)
    else:
        parts = mask.split('.')
        for s in parts:
            if len(s) == 1:
                new_list.append(str(randint(0, 9)))
            elif len(s) == 2:
                new_list.append(str(randint(10, 99)))
            elif len(s) == 3:
                new_list.append(str(randint(100, 255)))
    return new_list

def get_ip(mask=''):
    if mask == '':
        ip_parts = [str(get_rand_0_255(mask)) for _ in range(4)]
        return ".".join(ip_parts)
    else:
        return '.'.join(get_rand_0_255(mask))

def sort_ip_key(ip):
    ip_parts = ip.split(".")
    key_list = []
    for part in ip_parts:
        key_list.append(int(part))
    return key_list

def generate_list_ip_address(number: int, mask='', repeat=True, sort=False) -> list:
    ip_list = []
    for _ in range(number):
        ip_list.append(get_ip(mask))
    if not repeat:
        ip_list = list(set(ip_list))
    if sort:
        ip_list.sort(key=sort_ip_key)
    return ip_list

ip_list = generate_list_ip_address(number, mask, sort=True)
print(ip_list)