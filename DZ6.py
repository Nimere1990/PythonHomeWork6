# 6 - Из списка выше оставьте только те пары, где сумма кортежа кратна 5
# Пример
# [(10,25),(3,4),(4,1)] => [(10,25),(4,1)]

import random

numbers = [random.randint(1, 100) for _ in range(200)]
print(f'Cписок из 200 элементов: {list(enumerate(numbers))}')
print(f'Cписок пар, где сумма кортежа кратна 5 -> {list(filter(lambda i: (i[0]+i[1])%5==0, enumerate(numbers)))}')