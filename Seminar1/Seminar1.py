### Задача 2
# num = int((input("Введите трехзначное число: ")))
# temp = num
# if temp < 0: temp *=-1
# if temp < 1000 and temp > 99:
#     summ = 0
#     while temp > 0:
#         a = temp % 10
#         summ += a
#         temp //= 10
#     print(f"Сумма цифр числа {num}: {summ}")
# else:
#     print("Число не трехзначное!")


### Задача 4
# S = int(input("Введите количество журавликов из бумаги: "))
# print(f"Петя и Сережа сделали по {int(S/6)} журавликов из бумаги каждый")
# print(f"Катя сделала {int((S/6)*4)} журавликов из бумаги")


### Задача 6
# ticket = input("Введите шесть цифр: ")
# if len(ticket) == 6:
#     a = int(ticket[:3])
#     b = int(ticket[3:])
#     summA = 0
#     summB = 0
#     while a > 0 and b > 0:
#         summA += a % 10
#         a //= 10
#         summB += b % 10
#         b //= 10
#     if summA == summB:
#         print("Это счастливый билет!")
#     else:
#         print("Увы.. Это обычный билет.")
# else:
#     print("Номер введен неверно.")


### Задача 8
# n = int(input("Введите длину шоколадки в количестве плиток: "))
# m = int(input("Введите ширину шоколадки в количестве плиток: "))
# k = int(input("Введите количество долек, которое хотите отломить: "))
# if (k%n!=0 and k%m!=0) or k>=n*m: print("no")
# elif k%n==0 or k%m==0: print("yes")