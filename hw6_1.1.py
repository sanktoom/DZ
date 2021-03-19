while True:
    a = int(input('Число 1 : '))
    c = input('Операция : ')
    b = int(input('Число 2 : '))

    if c == '+':
        print(a+b)
    elif c == '-':
        print(a-b)
    elif c == '/':
        print(a/b)
    elif c == '*':
        print(a*b)
