def menu(book):
    choice = input("Выберите действие: \n1. Показать все записи \n2. Найти запись \n3. Добавить запись \n4. Выход \n\n:")
    if choice == "1":
        show_all(book)
    elif choice == "2":
        line_num = int(search(book))
        with open(book, "r+", encoding="UTF-8") as file:
            print(file.readlines()[line_num])
            search_menu(book, line_num)
    elif choice == "3":
        add_new(book)
    elif choice != "4":
        print("Выберите корректное действие.")
        enter = input("Нажмите Enter, чтобы продолжить.\n")
        menu(book)
    else:
        print("Выход.")
        exit()

def show_all(book):
    with open(book, "r+", encoding="UTF-8") as file:
        bookcontents = file.read() 
        if len(bookcontents) == 0: 
            print("В книге нет записей.")
            enter = input("Нажмите Enter, чтобы продолжить.\n")
        else: 
            print("Показ всех записей.\n")
            print(bookcontents)
    show_all_menu(book)

def show_all_menu(book):
    choice = input("Выберите действие: \n1. Назад \n\n:")
    if choice == "1":
        menu(book)
    else:
        print("Выберите корректное действие.")
        enter = input("Нажмите Enter, чтобы продолжить.\n")
        show_all_menu(book)

def search(book):
    print("Поиск записей.")
    choice = input("Выберите действие: \n1. Поиск по фамилии \n2. Поиск по имени \n3. Поиск по номеру телефона \n4. Назад \n\n:")
    if choice == "1":
        return search_function(book, 0)
    elif choice == "2":
        return search_function(book, 1)
    elif choice == "3":
        return search_function(book, 3)
    elif choice == "4":
        menu(book)
    else: 
        print("Выберите корректное действие.")
        enter = input("Нажмите Enter, чтобы продолжить.\n")
        return search(book)   

def add_new(book):
    print("Добавление новой записи.")
    lastname = (input("Введите фамилию: ")).capitalize()
    firstname = (input("Введите имя: ")).capitalize()
    patronymic = (input("Введите отчество: ")).capitalize() 
    phone_num = input("Введите номер телефона: ") 
    contents_details =(f"{lastname} {firstname} {patronymic}, {phone_num}\n") 
    with open(book, "a", encoding="UTF-8") as file:
        file.write(contents_details) 
        print(f"Новая запись: \n {contents_details}успешно добавлена!\n")
    sort(book)
    add_new_menu(book)
    

def add_new_menu(book):
    choice = input("Выберите действие: \n1. Добавить другую запись \n2. Назад \n\n:")
    if choice == "1":
        add_new(book)
    elif choice == "2":
        menu(book)
    elif choice == "3":
        print("Выход.")
    else:
        print("Выберите корректное действие.")
        enter = input("Нажмите Enter, чтобы продолжить.\n")
        add_new_menu(book)

def search_function(book, index):
    with open(book, "r+", encoding="UTF-8") as file:
        if index == 0: object = input("Введите фамилию (часть фамилии): ")
        elif index == 1: object = input("Введите имя (часть имени): ")
        elif index == 3: object = input("Введите номер телефона (часть номера телефона): ")
        lines = file.readlines()
        line_search = []
        i = 0
        for line in lines:
            if object.casefold() in line.split(" ")[index].casefold():
                line_search.append(f"{i}# {line}")
            i+=1
        if len(line_search)>1:
            print("".join(line_search))
            return research_function(book, line_search)
        elif len(line_search)<1: 
            print("Совпадений не найдено!\n")
            enter = input("Нажмите Enter, чтобы продолжить.\n")
            return search(book)
        else: return ("".join(line_search).split("#")[0])

def research_function(book, lines):
    choice = input(f"Совпадений найдено: {len(lines)}! Уточните поиск: \n1. Поиск по ID \n2. Поиск по фамилии \n3. Поиск по имени \n4. Поиск по номеру телефона \n5. Назад \n\n:")
    if choice == "1": index = 0; object = input("Введите ID: ") + "#"
    elif choice == "2": index = 1; object = input("Введите фамилию (часть фамилии): ")
    elif choice == "3": index = 2; object = input("Введите имя (часть имени): ")
    elif choice == "4": index = 4; object = input("Введите номер телефона (часть номера телефона): ")
    elif choice == "5":
        return search(book)
    else: 
        print("Выберите корректное действие.")
        enter = input("Нажмите Enter, чтобы продолжить.\n")
        return research_function(book, lines)
    line_search = []
    for line in lines:
        if object.casefold() in line.split(" ")[index].casefold():
            line_search.append(line)
    if len(line_search)>1:
            print("".join(line_search))
            return research_function(book, line_search)
    elif len(line_search)<1: 
        print("Совпадений не найдено!\n")
        enter = input("Нажмите Enter, чтобы продолжить.\n")
        return search(book)
    else: return ("".join(line_search).split("#")[0])
    
def sort(book):
    with open(book, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        with open(book, "w", encoding="UTF-8") as file:
            for line in data:
                file.write(line)

def search_menu(book, line):
    choice = input("Выберите действие: \n1. Изменить запись \n2. Удалить запись \n3. Назад \n\n:")
    if choice == "1":
        change(book, line)
    elif choice == "2":
        choice = input('Вы уверены? Для подтверждения введите "ДА" \n\n:')
        if choice == "ДА":
            delite(book, line)
            menu(book)
        else:
            print("Запись не удалена.\n")
            search_menu(book, line)            
    elif choice == "3":
        menu(book)
    else: 
        print("Выберите корректное действие.")
        enter = input("Нажмите Enter, чтобы продолжить.\n")
        search_menu(book, line)

def delite(book, line):
    with open(book, "r", encoding="UTF-8") as file:
        data = file.readlines()
        data.pop(line)
        with open(book, "w", encoding="UTF-8") as file:
            for line in data:
                file.write(line)

def change(book, line):
    with open(book, "r", encoding="UTF-8") as file:
        data = file.readlines()
        lastname = (input("Введите фамилию (оставить фамилию без изменений - введите Enter): ")).capitalize()
        if lastname == "":
            lastname = data[line][0]
        firstname = (input("Введите имя (оставить имя без изменений - введите Enter): ")).capitalize()
        if firstname == "":
            firstname = data[line][1]
        patronymic = (input("Введите отчество (оставить отчество без изменений - введите Enter): ")).capitalize()
        if patronymic == "":
            patronymic = data[line][2]
        phone_num = input("Введите номер телефона (оставить номер телефона без изменений - введите Enter): ")
        if phone_num == "":
            phone_num = data[line][3]
        new_contents =(f"{lastname} {firstname} {patronymic}, {phone_num}\n")
        print(f"Запись: \n{data[line]} успешно заменена на запись: \n{new_contents}")
        data[line], new_contents = new_contents, data[line]
        with open(book, "w", encoding="UTF-8") as file:
            for line in data:
                file.write(line)
        sort(book)
        menu(book)