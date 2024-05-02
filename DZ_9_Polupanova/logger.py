from data_create import name_data, surname_data, phone_data, adress_data


file_name = 'data_1.txt'

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = adress_data()
    var = int(input(f"Введите 1, чтобы записать данные\n"))

    while var != 1:
        print("Неправильный ввод")
        var = int(input('Введите число '))

    if var == 1:
        with open('DZ_9_Polupanova/data_1.txt', 'a', encoding='utf-8') as f:
            f.write(f"{name};{surname};{phone};{address}\n\n")


def print_data():
    print('Вывожу данные из файла: \n')
    with open('DZ_9_Polupanova/data_1.txt', 'r', encoding='utf-8') as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range (len(data_first)):
            if data_first[i] == '\n' or i == len(data_first) - 1:
                data_first_list.append(''.join(data_first[j:i+1]))
                j = i
        print(''.join(data_first_list))


# Изменяет информацию из файла
def edit_data():
    print("\n Имя | Фамилия | Телефон  | Город")
    with open('DZ_9_Polupanova/data_1.txt', 'r', encoding='utf-8') as data:
        tel_book = data.read()
        print(tel_book)
        print("")

    index_delete_data = int(input("Введите номер для редактирования: "))
    tel_book_lines = 'DZ_9_Polupanova/data_1.txt'.split('\n')
    edit_tel_book_lines = tel_book_lines[index_delete_data]
    elements = edit_tel_book_lines.split(' | ')
    name_data = input("Введите Имя: ")
    phone_data = input("Введите номер телефона: ")
    
    if len(name_data) == 0:
        fio = elements[1]
    if len(phone) == 0:
        phone = elements[2]
        edited_line = f"{name_data} | {phone_data}"
        tel_book_lines[index_delete_data] = edited_line
        print(f"Запись — {edit_tel_book_lines}, изменена на — {edited_line}\n")
    with open('DZ_9_Polupanova/data_1.txt', 'w', encoding='utf-8') as f:
        f.write("\n".join(tel_book_lines))

# Удаляет информацию из файла
def delete_data():
    print("\nПП | ФИО | Телефон")
    with open('DZ_9_Polupanova/data_1.txt', "r", encoding='utf-8') as data:
        tel_book = data.read()
        print(tel_book)
        print("")
        index_delete_data = int(input('Введите номер строки для удаления: '))
        tel_book_lines = tel_book.split('\n')
        del_tel_book_lines = tel_book_lines[index_delete_data]
        tel_book_lines.pop(index_delete_data)
        print(f'Удалена запись: {del_tel_book_lines}\n')
    with open('DZ_9_Polupanova/data_1.txt', 'w', encoding='utf-8') as data:
        data.write('\n'.join(tel_book_lines))

        
print_data()