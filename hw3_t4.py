print('4.1 #########################\n    выводит на экран и удаляет с начала элементы списка')
list1 = [1, 2, 3, 4, 5, 6, 7, 8, "aa"]
print('список = ' + str(list1))
while list1:
    print(list1.pop(0), end=' | ')
print('\nсписок = ' + str(list1))

print('4.2 #########################\n    выводит на экран и «удаляет» первый символ строки')
str1 = "qwertyuio"

print('строка= "' + str1 + '"')
while len(str1):
    print(str1[0], end=' | ')
    str1 = str1[1:]
print('\nстрока= "' + str1 + '"')

print('4.3 #########################\n    удаляет элементы списка от самого маленького до самого большого')
list1 = [1, 20, 3, 40, 5, 6, 7, 8, 2]
print('список = ' + str(list1))
list1 = sorted(list1)
print('список = ' + str(list1) + ' (после сортировки)')
while list1:
    print(list1.pop(0), end=' | ')
print('\nсписок = ' + str(list1))

print('4.4 #########################\n    удаляет элементы списка от самого маленького до самого большого')
rezultNum = 0
rezultPoz = 0
tempCnt = 0
maxCnt = 0
listNatNumb = [10, 10, 10, 10, 30, 20, 20, 20, 20, 20, 50, 50, 50, 50, 50, 40, 40, 40, 40]
print(listNatNumb)

for el in range(len(listNatNumb)-1):
    if listNatNumb[el] == listNatNumb[el + 1]:
        tempCnt += 1
        #print("Элемент " + str(el) + ", число " + str(listNatNumb[el]) + ", k-vo=" + str(tempCnt))
    if ((el + 1) == (len(listNatNumb) - 1) and tempCnt > 0) or listNatNumb[el] != listNatNumb[el + 1]:
        if tempCnt > 0:
            if tempCnt > maxCnt:
                maxCnt, rezultPoz, rezultNum = tempCnt, el, listNatNumb[el]
                print(
                    'Новый победитель! Число ' + str(rezultNum) + ', встречается ' + str(maxCnt + 1) + ' раз в подряд')
            else:
                print('Пропускаем неудачника! Число ' + str(listNatNumb[el]) + ', встречается ' + str(
                    tempCnt + 1) + ' раз в подряд')
        tempCnt = 0
print("***********************************************")
print('!Победило число ' + str(rezultNum) + ', встречается ' + str(maxCnt + 1) + ' раз подряд, начиная с позиции(отсчет c нуля) '+ str(rezultPoz-maxCnt))

