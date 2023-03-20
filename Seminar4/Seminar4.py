import random

### Задача 22

# list_n = [None for x in range(int(input("Введите длину масива A: ")))]
# list_m = [None for x in range(int(input("Введите длину масива B: ")))]

# for i in range(len(list_n)):
#     list_n[i] = int(input(f"Введите элемент [{i}] масива A: "))

# for i in range(len(list_m)):
#     list_m[i] = int(input(f"Введите элемент [{i}] масива B: "))

# print(list_n)
# print(list_m)

# list_x = sorted(list(set(list_n).intersection(set(list_m))))

# if len(list_x) > 0: print(f"Количество совпадений: {len(list_x)}. {list_x}")
# else: print("Cовпадений нет.")


### Задача 24

# array = [random.randint(10, 49) for i in range(int(input("Введите количество грядок: ")))]
# print(array)

# max = array[-2] + array[-1] + array[0]
# index_max = [len(array)-2, len(array)-1, 0]

# for i in range(1, len(array)):
#     a = (array[i-2] + array[i-1] + array[i])
#     if a > max: 
#         max = a
#         index_max = [-len(array)+(len(array)+(i-2)), -len(array)+(len(array)+(i-1)), i]

# print(f"Максимальное количество ягод: {max}, на кустах с индексами {index_max}")