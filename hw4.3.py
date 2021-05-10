#!/usr/bin/env python
# coding: utf-8

# In[ ]:


directories = {
'1': ['2207 876234', '11-2'],
'2': ['10006'],
'3': []
}

documents = [
{'type': 'passport', 'number': '2207 876234', 'name': 'Василий Гупкин'},
{'type': 'invoice', 'number': '11-2', 'name': 'Геннадий Покемонов'},
{'type': 'insurance', 'number': '10006', 'name': 'Аристарх Павлов'}
]


def find_owner(number):
res = 'Документ не найден в базе'
for i in documents:
if i['number'] == number:
res = 'Владелец документа: ' + i['name']
return res


number = input("Введите номер документа: ")
find_owner(documents)


def shelf(number):
res = 'Документ не найден в базе'
for i in directories:
if number in directories:
res = 'Документ хранится на полке:' + i
return res

number = input("Введите номер документа: ")
shelf(directories)


# Пользователь по команде “p” может узнать владельца документа по его номеру;
def people_document(arg_number):
    for doc_number in documents:
        if doc_number["number"] == arg_number:
            print(' Владелец документа: ', doc_number["name"])
            break
    else:
        print(' Такого документа - нет в архиве.')
        
# Пользователь по команде “s” может по номеру документа узнать на какой полке он хранится;
def shelf_number(arg_number):
    shelf_break = False
    for shelf_directory in directories.items():
        for doc_number in shelf_directory[1]:
            if doc_number == arg_number:
                print('Данный документ находится на полке - ', shelf_directory[0])
                shelf_break = True
                break
        if shelf_break == True:
            break
    else:
        print(' Документа нет на полке.')



# Пользователь по команде “l” может увидеть полную информацию по всем документам;
def list_documents():
    for document in documents:
        print('{} "{}" "{}"'.format(document['type'], document['number'], document['name']))
        
# Пользователь по команде “as” может добавить новую полку;

def add_shelf(number):
if number in directories:
return 'Такая полка уже существует. Текущий перечень полок:' + ','.join(directories.keys())
directories[number] = []
return 'Полка добавлена. Текущий перечень полок:' + ','.join(directories.keys())


number = input("Введите номер документа: ")
add_shelf(directories)
        
#Пользователь по команде “ds” может удалить существующую полку из данных (только если она пустая)

def rem_shelf(number):
if number in directories:
if len(directories[number]) > 0:
return 'На полке есть документа, удалите их перед удалением полки. Текущий перечень полок: ' + ', '.join(directories.keys())
directories.removed[number]
return 'Полка удалена. Текущий перечень полок: ' + ', '.join(directories.keys())
return 'Такой полки не существует. Текущий перечень полок:' + ', '.join(directories.keys())

rem_shelf(directories)


# Пользователь по команде “ad” может добавить новый документ в данные
def add_new_document(agr_type, arg_number, arg_name, arg_dir_number):
    if int(arg_dir_number) == 1 or int(arg_dir_number) == 2 or int(arg_dir_number) == 3:
        documents.append({"type": agr_type, "number": arg_number, "name": arg_name})
        directories[arg_dir_number].append(arg_number)
        print('\n Ваш документ добавлен в Архив!')
    else:
        print('\n Такой полки не существует.')


# Пользователь по команде “d” может удалить документ из данных
def del_document(arg_number):
    break_p = False
    for document in documents:
        if document['number'] == arg_number:
            document['number'] = 'Удален'
            for directory_value in directories.values():
                if arg_number in directory_value:
                    directory_value.remove(arg_number)
                    print('\n  Номер документа удален из каталога и полки!')
                    break_p = True
                    break
            if break_p == True:
                break
    else:
        print('\n Такого документа - нет.')


# Пользователь по команде “m” может переместить документ с полки на полку

def move_document(arg_number, arg_another_shelf):
    for directory_value in directories.values():
        if arg_number in directory_value:
            directory_value.remove(arg_number)
            directories[arg_another_shelf].append(arg_number)
            print('\n  Документ перемещён на указанную полку!')
            break
    else:
        print('\n Такого документа - нет, введите номер правильно.')

