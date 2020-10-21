from random import choice, sample, randint
from string import *
############## 1)
def txt():
    my_string = ''.join(choice(ascii_letters + digits + chr(32) + chr(44) + chr(45) + chr(58) + chr(59)) for i in range(100, 1000 + 1))
    indexes = [i for i in range(len(my_string))]
    sam = sample(indexes, 9)
    my_list = list(my_string)
    for i in sam:
        my_list[i] = chr(10)
    return ''.join(my_list)
############## 2)
def get_str():
    return ''.join(choice(ascii_lowercase) for i in range(5))

def get_randint():
    return randint(-100, 100)

def get_randfloat():
    return randint(0, 100) / 100

def get_randbool():
    return bool(randint(0, 1))

def get_randvalue():
    my_list = [get_randint(), get_randfloat(), get_randbool()]
    return choice(my_list)

def get_dict():
    my_list = [get_str() for i in range(randint(5, 20 + 1))]
    my_dict = {key: get_randvalue() for key in my_list}
    return my_dict

################ 3)
def get_n():
    return randint(3, 10)

def get_m():
    return randint(0, 1)

