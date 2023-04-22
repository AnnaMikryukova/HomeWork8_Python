''' Создать телефонный справочник с возможностью импорта и экспорта данных в
формате .txt. Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные.
2. Программа должна сохранять данные в текстовом файле.
3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию
человека).
4. Использование функций. Ваша программа не должна быть линейной.
5. Дополнить телефонный справочник возможностью изменения и удаления данных. 
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал 
для изменения и удаления данных.
'''


def add_contact():
	with open("phonebook.txt", "a") as file:
		name = input("Введите имя: ")
		lastname = input("Введите фамилию: ")
		phone_number = input("Введите номер телефона: ")
		file.write(f"{name}, {lastname}, {phone_number}\n")

def read_phonebook():
	phonebook = []
	with open("phonebook.txt", "r") as file:
		for line in file:
			name, lastname, phone_number = line.strip().split(", ")
			phonebook.append({"name": name, "lastname": lastname, "phone_number": phone_number})
	return phonebook

def search_contact():
	phonebook = read_phonebook()
	search_term = input("Введите значение для поиска: ")
	search_by = input("Введите категорию для поиска (name, lastname, phone_number): ")
	result = list(filter(lambda x: x[search_by] == search_term, phonebook))
	print(result)

def edit_contact():
	phonebook = read_phonebook()
	name_to_edit = input("Введите имя контакта для изменения: ")
	for contact in phonebook:
		if contact["name"] == name_to_edit:
			new_name = input(f"Введите новое имя для контакта {name_to_edit}: ")
			new_lastname = input(f"Введите новую фамилию для контакта {name_to_edit}: ")
			new_phone_number = input(f"Введите новый номер телефона для контакта {name_to_edit}: ")
			contact["name"] = new_name
			contact["lastname"] = new_lastname
			contact["phone_number"] = new_phone_number
			with open("phonebook.txt", "w") as file:
				for contact in phonebook:
					file.write(f"{contact['name']}, {contact['lastname']}, {contact['phone_number']}\n")
			print(f"Контакт {name_to_edit} успешно изменен.")

def delete_contact():
	phonebook = read_phonebook()
	name = input("Введите имя контакта, который нужно удалить: ")
	lastname = input("Введите фамилию контакта, который нужно удалить: ")
	for contact in phonebook:
		if contact['name'] == name and contact['lastname'] == lastname:
			phonebook.remove(contact)
			with open("phonebook.txt", "w") as file:
				for contact in phonebook:
					file.write(f"{contact['name']}, {contact['lastname']}, {contact['phone_number']}\n")
			print(f"Контакт {name} {lastname} был успешно удален!")
			return
	print(f"Контакт {name} {lastname} не найден в телефонной книге.")

while True:
	print("Выберите действие:")
	print("1 - Добавить контакт")
	print("2 - Просмотреть телефонную книгу")
	print("3 - Поиск контакта")
	print("4 - Изменить контакт")
	print("5 - Удалить контакт")
	print("6 - Выход")

	choice = input("Введите номер действия: ")
	if choice == "1":
		add_contact()
	elif choice == "2":
		phonebook = read_phonebook()
		print(phonebook)
	elif choice == "3":
		search_contact()
	elif choice == "4":
		edit_contact()
	elif choice == "5":
		delete_contact()
	elif choice == "6":
		break
	else:
		print("Некорректный ввод. Попробуйте еще раз.")