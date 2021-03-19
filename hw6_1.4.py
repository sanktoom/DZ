while True:
    try:
        a = int(input('Введите год: '))
        if a % 4 == 0:
            if a % 100 == 0:
                if a % 400 == 0:
                    print('Год високосный')
                    break
                else:
                    print('Не високосный')
                    break
            else:
                print('Год високосный')
                break
        else:
            print('Не високосный')
            break
    except ValueError:
        print('Введите число!')
        continue

