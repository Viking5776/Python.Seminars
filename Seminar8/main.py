import function

phonebook = "phonebook.txt" 
file = open("phonebook.txt" , "a+", encoding="UTF-8")
file.close

function.menu(phonebook)