num = int(input('Введите число: '))
fac = 1
while num > 1:
    fac = fac * num
    num = num - 1
print('Факториал числа:',fac)