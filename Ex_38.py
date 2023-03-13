# Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать 
# функционал для изменения и удаления данных

# Поиск данных по заданному параметру
def print_info(atribut):
    with open('/Users/olgadrach/Documents/GB/Python/Homework/Python_Homework_08/save.txt', 'r', encoding='UTF-8') as save_info:
        for line in save_info:
            if str(atribut).lower() in str(line).lower():
                print(line)

# Запрос у пользователя атрибута для поиска
def find_atribut():
        atribut = input('Введите инфо для поиска или оставьте пустым для вывода всех данных: ')
        return atribut

# Добавление данных
def import_new_data():
    print('Введите новые данные в формате: Имя Фамилия Телефон')
    with open('/Users/olgadrach/Documents/GB/Python/Homework/Python_Homework_08/save.txt', 'a', encoding='UTF-8') as save_info:
        save_info.writelines(input('Строка ввода: '))
        save_info.write('\n')
        print('Данные внесены')


def replace_data():
    old_item = input("введите Имя или Фамилию для поиска данных : ")
    with open('/Users/olgadrach/Documents/GB/Python/Homework/Python_Homework_08/save.txt', 'r', encoding='UTF-8') as s:
        new_item = input('Введите новые данные: ')
        result_list = [elem.replace(old_item, new_item) for elem in s]
        print(result_list)
    
                


# print_info(find_atribut())
# import_new_data()
replace_data()
