################ 1)
from random import randint
my_list = [randint(1, 100) for _ in range(20)]
print(my_list)

my_list = []
for _ in range(20):
    my_list.append(randint(1, 100))
print(my_list)