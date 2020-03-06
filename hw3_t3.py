print('  Задание 3')

print('выводит числа от 0 до 10')
i = 0
while i < 10:
    print(i)
    i += 1
print('выводит числа от 20 до 1 (в одной строчке, разделённые пробелом)')
i = 20
while i > 0:
    print(i, end=' ')
    i -= 1

cntIter = 0

num = 200
print("\nчисло= " + str(num))
while (int)(num % 2) == 0:
    cntIter += 1
    num = (int)(num / 2)
    print(num, end=' ')
print('\nделили нацело на два: ' + str(cntIter) + '-раз(а)')

