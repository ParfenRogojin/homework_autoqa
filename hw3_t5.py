str1=5
str2=3
try:
    rez=str1+str2
except Exception as e:
    print(e)
    rez=str(str1)+str(str2)
print(rez)
