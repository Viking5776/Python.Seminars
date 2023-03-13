import random
import math

### Задача 10

# n = int(input("Введите количество монеток: "))
# obverse = 0
# reverse = 0
# for i in range(n):
#     x = int(input("Введите сторону монетки (0 - орёл, 1 - решка): "))
#     if x == 0:
#         obverse += 1
#     else:
#         reverse += 1
# if obverse < reverse:
#     print(obverse)
# else:
#     print(reverse)


### Задача 12

# x = random.randint(0, 9)
# y = random.randint(0, 9)
# s = x + y
# p = x * y
# print (f"Сумма чисел: {s}, произведение чисел: {p}.")

# a = int(input("Введите сумму чисел: "))
# b = int(input("Введите произведение чисел:"))
# D = (a*a) - 4*b
# x = int((a + math.sqrt(D)) / 2)
# y = int((a - math.sqrt(D)) / 2)
# print(f"x = {x}, y = {y}")


### Задача 14

# n = int(input("Введите число: "))
# i = 0
# while (2 ** i) <= n:
#     print((2 ** i), end=', ')
#     i += 1