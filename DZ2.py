# 2- Найти произведение пар чисел в списке. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import random

number = int(input("Введите число N: "))
spisok = [random.randint(0, 10) for i in range(0,number)]
print(f"Cписок из {number} чисел: \n{spisok}")

spisok2 = []
for i in range ( 0, ((len(spisok) + 1)//2) ): spisok2.append(spisok[i] * spisok[-1-i]) 
print(f"Результат: \n{spisok2}")