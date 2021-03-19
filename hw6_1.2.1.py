a = int(input('Число : '))
b = a-1
c = ' '
s = '**'
for i in range(a):
    print((b * c) + s + (b * c))
    s += '**'
    b -= 1
