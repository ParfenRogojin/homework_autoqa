import string
str1 = 'We are not what we should be!\nWe are not what we need to be.\nBut at least we are not what we used to be\n (Football Coach)'

print(str1)
str2 = str1.split()
print(str2)
print('слов в тексте: '+str(len(str2)))
for item in range(len(str2)):
    str2[item]=str2[item].strip('!.()')
print('Удалены знаки препинания: '+str(str2))
str2.sort()
print('в алфавитном порядке: '+str(str2))

dict1={}
for item in range(len(str2)):
    if (str2[item].capitalize()) in dict1:
        dict1[str2[item].capitalize()]+=1
    else:
        dict1.update({str2[item].capitalize():1})
print('сколько раз встречается каждое слово: '+str(dict1))
