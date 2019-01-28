symb_tuple = ('*', '/', '-', '+')

def polencalculate(symb, argone, argtwo):
    try:
        assert float(argone) >= 0 and float(argtwo) >= 0
        result = eval('{} {} {}'.format(argone, symb, argtwo))

        if result % 1 == 0:
            result = int(result)

        return 'Ответ: {}'.format(result)
    except ZeroDivisionError:
        return 'Деление на 0 невозможно!'
    except AssertionError:
        return 'Операции с отрицательными числами не поддерживаются!'

def inputchecking():
    checklist = input('Введите выражение, разделяя аргументы пробелами: ').split()

    try:
        assert len(checklist) == 3, 'insufficient number of arguments'
    except AssertionError:
        que = input('Введено недостаточное количество аргументов'
                 ' или аргументы не разделены пробелом, повторить ввод?, y/n: ').lower()
        if que == 'n':
            return 'Операция завершена пользователем'
        elif  que == 'y':
            return inputchecking()
        else:
            return 'Операция завершена некорректно'

    try:
        assert checklist[0] in symb_tuple, 'operation not supported by func'
        return checklist
    except AssertionError:
        return 'Данная операция не поддерживается'


arg_list = inputchecking()

try:
    assert type(arg_list) == type([]), 'arg_list is not list'
    calc = polencalculate(arg_list[0], arg_list[1], arg_list[2])
    print(calc)
except AssertionError:
    print(arg_list)


