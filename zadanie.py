import csv

# Определение функций
def add_entry():
    name = input("Введите имя: ")
    surname = input("Введите фамилию: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    with open('phonebook.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, surname, patronymic, phone_number])
    print("Контакт успешно добавлен")

def search_entry():
    query = input("Введите имя, фамилию или отчество: ")
    with open('phonebook.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if query.lower() in [name.lower(), surname.lower(), patronymic.lower() for name, surname, patronymic, _ in reader]:
                print(f"Найден контакт: {name} {surname} {patronymic}: {phone_number}")
                break
        else:
            print("Контакт не найден")

def edit_entry():
    query = input("Введите имя, фамилию или отчество для редактирования: ")
    with open('phonebook.csv', 'r') as file:
        reader = csv.reader(file)
        entries = list(reader)
    for i, (name, surname, patronymic, phone_number) in enumerate(entries):
        if query.lower() in [name.lower(), surname.lower(), patronymic.lower()]:
            new_name = input(f"Введите новое имя для {name} {surname} {patronymic}: ")
            new_surname = input(f"Введите новую фамилию для {name} {surname} {patronymic}: ")
            new_patronymic = input(f"Введите новое отчество для {name} {surname} {patronymic}: ")
            new_phone_number = input(f"Введите новый номер телефона для {name} {surname} {patronymic}: ")
            entries[i] = [new_name, new_surname, new_patronymic, new_phone_number]
            with open('phonebook.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(entries)
            print("Контакт успешно изменен")
            break
    else:
        print("Контакт не найден")

def display_entries():
    with open('phonebook.csv', 'r') as file:
        reader = csv.reader(file)
        for name, surname, patronymic, phone_number in reader:
            print(f"{name} {surname} {patronymic}: {phone_number}")

def export_entries():
    with open('phonebook.csv', 'r') as file:
        reader = csv.reader(file)
        with open('phonebook.txt', 'w') as export_file:
            for name, surname, patronymic, phone_number in reader:
                export_file.write(f"{name} {surname} {patronymic}: {phone_number}\n")
    print("Контакты успешно экспортированы в phonebook.txt")

# Главная функция
def main():
    while True:
        print("1. Добавить контакт")
        print("2. Найти контакт")
        print("3. Редактировать контакт")
        print("4. Показать все контакты")
        print("5. Экспортировать контакты в .txt файл")
        print("6. Выход")
        choice = input("Выберите действие: ")

        if choice == '1':
            add_entry()
        elif choice == '2':
            search_entry()
        elif choice == '3':
            edit_entry()
        elif choice == '4':
            display_entries()
        elif choice == '5':
            export_entries()
        elif choice == '6':
            break
        else:
            print("Неправильный выбор. Попробуйте еще раз")

if __name__ == '__main__':
    main()
