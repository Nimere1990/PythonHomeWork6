# 1- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1

from typing import List

def str_enc(lst: List[str], enc: int):
    lst = [i[0] for i in enumerate(lst) if type(i[1]) == str and i[1] in string_search]
    return f"Position of {enc} encounter of {string_search} string:\n{lst[enc-1]}" \
           if len(lst) >= enc else -1

initial_line = list(input('Введите строки через пробел:\n ').split())
print(f'\n Список строк: {initial_line}')
string_search = input("Введите строку которую нужно найти:\n ")
print(f'Строка которую ищем: {string_search}\n')

res = str_enc(initial_line, 2)
print(res)