def acronym():
    x = input('ввод: ')
    p = 0
    c = ''
    for i in x.split():
        c += i[p]
    print('результат: ' + c.upper())
