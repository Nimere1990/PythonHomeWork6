# 4 - Дан список случайных чисел. 
# Оставьте только те, сумма цифр которых четна

import random

number = int(input("Введите число N: "))
spisok = [random.randint(0, 100) for i in range(0,number)]
print(f"Cписок из {number} чисел: \n{spisok}")
spisok_2 = ([sum(map(int, str(el))) for el in spisok])
spisok_2 = [i for i in spisok_2 if i % 2 == 0]
print(f"Результат: \n{spisok_2}")