num = int(input('Введите число, чтобы найти его факториал: '))

fac = 1

while num > 1:
    fac *= num
    num = num - 1

print('Факториал числа:',fac)