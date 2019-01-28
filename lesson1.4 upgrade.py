documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "insurance", "number": "66613"}
]
directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}
que_comands = ('y', 'n')
break_string = 'Обработка запроса завершена'

def help_command():
    commands = ('p', 'l', 's', 'a', 'd', 'm', 'as', 'all')
    check = input('Необходимо ли вывести инструкцию?, y/n: ').lower()

    if check == 'y':
        print('p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит')
        print(
            'l– list – команда, которая выведет список всех документов '
            'в формате passport "2207 876234" "Василий Гупкин"')
        print('s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится')
        print(
            'a – add – команда, которая добавит новый документ в каталог и в перечень полок, '
            'спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться')
        print('d – delete – команда, которая спросит номер документа и удалит его из каталога и из перечня полок')
        print(
            'm – move – команда, которая спросит номер документа и целевую полку'
            ' и переместит его с текущей полки на целевую')
        print('as – add shelf – команда, которая спросит номер новой полки и добавит ее в перечень')
        print('all – all names – команда, которая выведет имена всех владельцев документов')
        print()

        return switch(input('Введите команду: ').lower(), commands)

    elif check not in que_comands:
        print('Команда некорректна!')
        return break_string

    else:
        return switch(input('Введите команду: ').lower(), commands)

def switch(com, com_tup):
    if com not in com_tup:
        print('Команда некорректна!')
        return break_string

    if com == 'p':
        return f_people(input('Введите номер документа: '))

    elif com == 'l':
        return f_list()

    elif com == 's':
        return f_shelf(input('Введите номер документа: '))

    elif com == 'a':
        return f_add(input('Введите номер нового документа: '))

    elif com == 'd':
        return f_delete()

    elif com == 'm':
        return f_move()

    elif com == 'as':
        return f_add_shelf()

    elif com == 'all':
        return f_all()

def type_check(check_val):
    try:
        return str(int(check_val))
    except ValueError:
        return type_check(input('Введите число!: '))

def f_people(doc_num):
    for num in documents:
        if num["number"] == doc_num:
            try:
                return num["name"]
            except KeyError:
                print('Отсутствует имя владельца документа с номером {}'.format(num['number']))
                return break_string

    doc_check = input('Документ не найден, занести новый?, y/n: ').lower()
    if doc_check not in que_comands:
        print('Команда некорректна!')
        return break_string
    elif doc_check == 'y':
        return f_add(doc_num)
    else:
        return break_string

def f_list():
    for doc in documents:
        print('"', '" "'.join(list(doc.values())), '"', sep='')

    return 'Готово'

def f_shelf(doc_num, del_check=False, move_check=False):
    for num in documents:
        if num["number"] == doc_num:
            for key in tuple(directories.keys()):
                if doc_num in directories[key]:
                    return 'Номер полки: ' + key

    if del_check:
        return break_string

    doc_check = input('Документ не найден, занести новый?, y/n: ').lower()
    if doc_check not in que_comands:
        print('Команда некорректна!')
        return break_string
    elif doc_check == 'y':
        return f_add(doc_num)
    else:
        return break_string

def f_add(new_doc_num, move_check=False):
    for key in tuple(directories.keys()):
        if new_doc_num in directories[key]:
            print('Документ с данным номером уже существует!')
            return break_string

    new_doc_shelf = type_check(input('Введите номер полки, на которой необходимо разместить документ: '))
    if directories.get(new_doc_shelf) == None:
        shelf_check = input('Данной полки не существует, создать новую?, y/n: ').lower()
        if shelf_check not in que_comands:
            print('Команда некорректна!')
            return break_string
        elif shelf_check == 'y':
            new_doc_shelf = f_add_shelf()
            if new_doc_shelf == break_string:
                print('Полка не выбрана!')
                return break_string
            new_doc_shelf = new_doc_shelf.replace('Создана полка с номером ', '')
        else:
            print('Полка не выбрана!')
            return break_string

    new_doc_type = input('Введите тип нового документа: ')
    new_doc_owner = input('Введите имя владельца документа: ')

    doc_dict = {"type": str(new_doc_type), "number": str(new_doc_num), "name": str(new_doc_owner)}
    documents.append(doc_dict)
    directories[new_doc_shelf].append(new_doc_num)
    print(documents)
    print(directories)
    if not move_check:
        return 'Документ успешно добавлен'
    else:
        return True

def f_delete():
    del_check = True
    m_doc_num = input('Введите номер документа: ')
    del_doc_shelf = f_shelf(m_doc_num, True)
    if del_doc_shelf == break_string:
        return 'Документа не существует!'
    del_doc_shelf = del_doc_shelf.replace('Номер полки: ', '')
    directories[del_doc_shelf].remove(m_doc_num)
    for doc in documents:
        if doc["number"] == m_doc_num:
            documents.remove(doc)
            print(documents)
            print(directories)
            break
    return 'Документ успешно удалён'

def f_move():
    m_doc_num = input('Введите номер документа: ')
    old_shelf_num = f_shelf(m_doc_num, False, True)
    if old_shelf_num == break_string:
        return old_shelf_num
    elif old_shelf_num:
        return 'Документ успешно добавлен'

    old_shelf_num = old_shelf_num.replace('Номер полки: ', '')
    new_shelf_num = type_check(input('Введите номер полки, на которую следует переместить документ: '))
    if directories.get(new_shelf_num) == None:
        shelf_check = input('Данной полки не существует, создать новую?, y/n: ').lower()
        if shelf_check not in que_comands:
            print('Команда некорректна!')
            return break_string
        elif shelf_check == 'y':
            new_shelf_num = f_add_shelf()
            if new_shelf_num == break_string:
                print('Полка не выбрана!')
                return break_string
            new_shelf_num = new_shelf_num.replace('Создана полка с номером ', '')
        else:
            print('Полка не выбрана!')
            return break_string

    directories[old_shelf_num].remove(m_doc_num)
    directories[new_shelf_num].append(m_doc_num)
    print(directories[old_shelf_num])
    print(directories[new_shelf_num])
    return 'Документ перемещён'

def f_add_shelf():
    print('Создание новой полки')
    new_shelf = int(sorted(list(directories.keys()))[-1]) + 1
    def_check = input('Номер новой полки по умолчанию {}, подтверждаете?, y/n: '.format(new_shelf)).lower()
    if def_check not in que_comands:
        print('Команда некорректна!')
        return break_string
    elif def_check == 'y':
        directories.update({str(new_shelf): []})
        print(directories)
    else:
        new_shelf = type_check(input('Введите номер новой полки: '))
        br = 0
        while not directories.get(new_shelf) == None:
            br += 1
            print('Полка с таким номером уже существует!')
            print('Список существующих полок ', ' '.join(tuple(directories.keys())))
            if br == 5:
                print('Превышен лимит попыток ввода!')
                return break_string
            new_shelf = type_check(input('Введите номер новой полки: '))
        directories.update({str(new_shelf): []})
        print(directories)

    return 'Создана полка с номером ' + str(new_shelf)

def f_all():
    for num in documents:
        try:
            print(num['name'])
        except KeyError:
            print('Отсутствует имя владельца документа с номером {}'.format(num['number']))
    print()
    return 'Операция завершена'

action = help_command()
print(action)

