import random
from math import sqrt
######################## 1)
def get_x():
    x_list = [random.uniform(-100, 100) for _ in range(3)]
    diff_1 = abs(x_list[0]) - abs(x_list[1])
    diff_2 = abs(x_list[0]) - abs(x_list[2])
    while 1 > abs(diff_1) or 1 > abs(diff_2):
        x_list = [random.uniform(-100, 100) for _ in range(3)]
        diff_1 = abs(x_list[0]) - abs(x_list[1])
        diff_2 = abs(x_list[0]) - abs(x_list[2])
    return x_list

def get_y():
    y_list = [random.uniform(-100, 100) for _ in range(3)]
    diff_1 = abs(y_list[0]) - abs(y_list[1])
    diff_2 = abs(y_list[0]) - abs(y_list[2])
    while 1 > abs(diff_1) or 1 > abs(diff_2):
        y_list = [random.uniform(-100, 100) for _ in range(3)]
        diff_1 = abs(y_list[0]) - abs(y_list[1])
        diff_2 = abs(y_list[0]) - abs(y_list[2])
    return y_list

def create_randome_triangle() -> tuple:
    coords = tuple([(get_x()[i], get_y()[i]) for i in range(len(get_x()))])
    return coords

############################## 2)
def get_area(triangle):
    x1_x3 = triangle[0][0] - triangle[2][0]
    x2_x3 = triangle[1][0] - triangle[2][0]
    y1_y3 = triangle[0][1] - triangle[2][1]
    y2_y3 = triangle[1][1] - triangle[2][1]
    a = x1_x3 * y2_y3
    b = x2_x3 * y1_y3
    s = 0.5 * abs(a - b)
    return f'Площадь треугольника {triangle} равна {s}'

########################### 3)
def create_right_triangle(tuple):
    x2 = tuple[0] + (10 * sqrt(2))
    y3 = tuple[1] + (10 * sqrt(2))

    b = (x2, tuple[1])
    c = (tuple[0], y3)
    s = get_area((tuple, b, c))
    return s

import json
import os
import string

def get_str():
    return ''.join(random.choice(str(random.randint(0, 9)) + '_') for _ in range(1, 5)) + ''.join(random.choice(string.ascii_lowercase) for _ in range(1, 3))

def get_new_dir(data):
    path = 'tmp_folder'
    file_name = get_str()
    if not os.path.isdir(path):
        os.mkdir(path)

    with open(path + chr(92) + file_name, 'w') as json_file:
        json.dump(data, json_file, indent=2)

def generate_data_for_file(file_name):
    width = random.randint(0, 400)
    data = {
        'filename': file_name,
        'width': width,
        'objects': [
        {f"object{index}": {
                "class": symbol,
                "xmin": width / 4 * index,
                "xmax": width / 4 * (index + 1),}
            for index, symbol in enumerate(file_name[0:4]) if symbol != '_'}
        ]
    }
    return data

get_new_dir(generate_data_for_file(get_str()))

