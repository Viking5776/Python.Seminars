import random

### Задача 16

# list = [((i*0)+random.randint(0, 9)) for i in range(int(input("Введите длину масива: ")))]
# print(list)

# x = int(input("Ведите искомое число: "))
# count = 0
# for i in range(len(list)):
#     if list[i] == x:
#         count+=1
# print(f"Количество искомых чисел: {count}.")


### Задача 18

# list = [((i*0)+random.randint(0, 99)) for i in range(int(input("Введите длину масива: ")))]
# print(list)

# x = int(input("Ведите искомое число: "))
# max = max(list)
# min = min(list)
# for i in list:
#     if i > min and i <= x:
#         min = i
# for i in list:
#     if i < max and i >= x:
#         max = i
# if abs(x-min) < abs(x-max): print(f"Ближайшее число к искомому числу: {min}.")
# elif abs(x-max) < abs(x-min): print(f"Ближайшее число к искомому числу: {max}.")
# elif max==min: print(f"Ближайшее число к искомому числу: {min}.")
# else: print(f"Ближайшие числа к искомому числу: {min} и {max}.")


### Задача 20

# one_score = ("А", "В", "Е", "И", "Н", "О", "Р", "С", "Т")
# two_score = ("Д", "К", "Л", "М", "П", "У")
# three_score = ("Б", "Г", "Ё", "Ь", "Я")
# four_score = ("Й", "Ы")
# five_score = ("Ж", "З", "Х", "Ц", "Ч")
# eight_score = ("Ш", "Э", "Ю")
# ten_score = ("Ф", "Щ", "Ъ")

# word = list(str.upper(input("Введите слово: ")))
# sum = 0
# for i in word:
#     if i in one_score: sum+=1
#     elif i in two_score: sum+=2
#     elif i in three_score: sum+=3
#     elif i in four_score: sum+=4
#     elif i in five_score: sum+=5
#     elif i in eight_score: sum+=8
#     elif i in ten_score: sum+=10
#     else: sum+=0
# print(f"Стоимость слова, баллов: {sum}")