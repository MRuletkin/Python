import random

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

def create_randome_triangle():
    coords = tuple([(get_x()[i], get_y()[i]) for i in range(len(get_x()))])
    return coords

triangle = create_randome_triangle()
# print(triangle)

def get_space():
    x1_x3 = triangle[0][0] - triangle[2][0]
    x2_x3 = triangle[1][0] - triangle[2][0]
    y1_y3 = triangle[0][1] - triangle[2][1]
    y2_y3 = triangle[1][1] - triangle[2][1]
    a = x1_x3 * y2_y3
    b = x2_x3 * y1_y3
    s = 0.5 * abs(a - b)
    return f'Площадь треугольника {triangle} равна {s}'
print(get_space())



