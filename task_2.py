# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
list_1 = []
n = 20
for i in range(n):
    list_1.append(random.randint(0, 21))
print(list_1)
try:
    min_number = int(input('min: '))
    max_number = int(input('max: '))
    for i in range(len(list_1)):
        if min_number <= list_1[i] <= max_number:
            print(i)
except ValueError:
    print("Вы ввели не число!")