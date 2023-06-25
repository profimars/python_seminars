# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал
# для изменения и удаления данных

# Формируем телефонный справочник
def output_file_fon(selected_file):
    print("\nНомер | ID | Фамилия | Имя | Отчество | Телефон")
    with open(selected_file, "r", encoding="utf-8") as file:
        print(file.read())
    print()


# Добавляем новую запись в телефонный справочник
def input_record(file_fon, count):
    number = count + 1
    ID = 1000 + number
    record_template = enter_record_template()
    record = f"{number} | {ID} | {record_template}"
    with open(file_fon, "a", encoding="utf-8") as file:
        file.write(record)
    print(f"Добавили запись в телефонный справочник: {record}")


# Редактируем старую запись
def edit_record(file_fon, count, telephone_directory):
    output_file_fon(file_fon)
    record_number = int(input("Введите номер строки для редактирования: "))
    OK = check_count(count, record_number)
    if (OK == 1):
        selected_line = telephone_directory[record_number - 1]
        elements = selected_line.split(" | ")
        record_template = enter_record_template()
        number = elements[0]
        ID = elements[1]
        edited_line = f"{number} | {ID} | {record_template}"
        telephone_directory[record_number - 1] = edited_line
        print(f"На строке {number} запись - {selected_line}, изменена на - {edited_line}\n")
        with open(file_fon, "w", encoding='utf-8') as file:
            file.write("\n".join(telephone_directory))


# Удаляем ненужную запись
def delete_record(file_fon, count, telephone_directory):
    output_file_fon(file_fon)
    record_number = int(input("Введите номер строки удаляемой записи: ")) - 1
    OK = check_count(count, record_number + 1)
    if (OK == 1):
        deleted_record = telephone_directory[record_number]
        telephone_directory.pop(record_number)
        print(f"Удалена запись: {deleted_record}\n")
        with open(file_fon, "w", encoding='utf-8') as file:
            file.write("\n".join(telephone_directory))


def check_count(count, record_number):
    if (record_number > count):
        print(f"В телефонном справочнике количество записей {count}, а вы ввели {record_number}")
        print()
        return 0
    return 1


def enter_record_template():
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    telephone = input("Ведите телефон: ")
    record_template = f"{surname} | {name} | {patronymic} | {telephone}\n"
    print(f"record_template = {record_template}")
    return record_template


def main():
    working = 1
    file_fon = "fon.txt"
    # Если файла нет то создаем его в папке
    with open(file_fon, "a", encoding="utf-8") as file:
        file.write("")
    while working == 1:
        print("Выберите одно из действий:")
        print("1 - Вывести телефонный справочник")
        print("2 - Ввести данные в справочник")
        print("3 - Изменить данные в справочнике")
        print("4 - Удалить данные в справочнике")
        print("0 - Выход из программы")
        selected_option = int(input("Выберите вариант: "))
        if (selected_option == 2):
            with open(file_fon, "r", encoding='utf-8') as file:
                text = file.readlines()
            count = len(text)
        elif (selected_option == 3 or selected_option == 4):
            with open(file_fon, "r", encoding='utf-8') as file:
                text = file.readlines()
            count = len(text)
            with open(file_fon, "r", encoding='utf-8') as file:
                text = file.read()
            telephone_directory = text.split("\n")
        if selected_option == 1:
            output_file_fon(file_fon)
        elif selected_option == 2:
            input_record(file_fon, count)
        elif selected_option == 3:
            edit_record(file_fon, count, telephone_directory)
        elif selected_option == 4:
            delete_record(file_fon, count, telephone_directory)
        else:
            working = 0

    print("Вышли из программы")


if __name__ == "__main__":
    main()
