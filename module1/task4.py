def match(operation):
    if operation == 'save':
        print('сохранить')
    elif operation == 'load':
        print('загрузить')
    else:
        print('неизвестная операция')


# пример использования
match('save')
match('load')
match('abcd')
