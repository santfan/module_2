import random

def find_key(num):
    volums_key = []
    keys = []
    for key_1 in range(1, num):
        for key_2 in range(1, num):
            if (num % (key_1 + key_2) == 0) and (key_1 != key_2):
                if [key_1, key_2][:: -1] not in keys:
                    keys.append([key_1, key_2])
    volums_key.extend(keys)

    print(f'Загадное число {num} пары ключей {volums_key}')

num = random.choice(range(3, 21))
find_key(num)