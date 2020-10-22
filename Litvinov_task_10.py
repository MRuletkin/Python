from random import choice, sample, randint
from string import ascii_letters, digits, ascii_lowercase
import csv
import json
############## 1)
def txt():
    my_string = ''.join(choice(ascii_letters + digits + chr(32) + chr(44) + chr(45) + chr(58) + chr(59)) for i in range(100, 1000 + 1))
    indexes = [i for i in range(len(my_string))]
    sam = sample(indexes, 9)
    my_list = list(my_string)
    for i in sam:
        my_list[i] = chr(10)
    return ''.join(my_list)

def write_txt(filename_with_path):
    f = open(filename_with_path, 'w')
    f.write(txt())

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

def write_json(filename_with_path):
    my_json = json.dumps(get_dict())

    with open(filename_with_path, 'w') as json_file:
        json.dump(my_json, json_file, indent=2)

    with open('test.json', 'r') as json_file:
        my_json = json.load(json_file)

################ 3)
def get_value():
    return randint(0, 1)

def get_randints():
    return randint(3, 10)

def get_list(n = get_randints()):
    list = [get_value() for a in range(n)]
    return list

def get_data(m = get_randints()):
    data = [get_list() for _ in range(m)]
    return data

def write_csv(filename_with_path):
    with open(filename_with_path, 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=";")
        csvwriter.writerows(get_data())

def file_writer(filename_with_path):
    mode = filename_with_path.rsplit(".")[-1]
    if mode == "txt":
        data = write_txt(filename_with_path)
    elif mode == "json":
        data = write_json(filename_with_path)
    elif mode == "csv":
        data = write_csv(filename_with_path)
    else:
        raise Exception("Unsupported file format!")
    return data

file_writer('test.jpg')
