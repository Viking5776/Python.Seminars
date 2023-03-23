### Задача 34

# vowels = frozenset(["а", "о", "у", "э", "ы", "я", "ё", "ю", "е", "и"])

# words = "парара-рам рам-пым-папам па-ра-па-да"
# words = (words.split(" "))

# count = []

# for i in range(len(words)):
#     words[i] = [i for i in words[i]]
#     counter = 0
#     for j in range(len(words[i])):
#         if words[i][j] in vowels:
#             counter+=1
#     count.append(counter)

# if len(set(count)) == 1:
#     print("Парам пам-пам")
# else: print("Пам парам")


### Задача 36

# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for i in range(1, num_rows+1):
#         for j in range(1, num_columns):
#             print(operation(i, j), end="\t")
#         print(operation(i, num_columns))

# print_operation_table(lambda x, y: x * y)