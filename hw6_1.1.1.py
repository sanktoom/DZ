while True:
    try:
        a = int(input('Число 1 : '))
        c = input('Операция : ')
        b = int(input('Число 2 : '))
        if c == '+':
            print(a + b)
        elif c == '-':
            print(a - b)
        elif c == '/':
            print(a / b)
        elif c == '*':
            print(a * b)
        elif c == '**':
            print(a**b)
        elif c == '2':
            print(pow(a, 0.5))
    except ValueError:
        print('Не число!')
        continue
    except ZeroDivisionError:
        print('Не делиться на 0!')
        continue
