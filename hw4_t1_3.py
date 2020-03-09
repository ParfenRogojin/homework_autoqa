def createSong(cntLines=3, cntLa=3, isUp=0):
    rezult=((("La-"*cntLa)[:-1:]+'\n')*cntLines)[:-1:]
    return rezult+'!' if isUp else  rezult+'.'


def secondMin(*args):
    return sorted({*args})[1]

def clrNonAlph(s):
    rez=''
    assert type(s) not in (float,int,bool),'AssertionError: '+str(s)+' - '+'not a string'
    for ch in s:
        if ('qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'.find(ch))>-1:
            rez+=ch
    return rez

if __name__=='__main__':
    print(createSong(3, 3, 0))
    print(createSong(4, 4, 1))

    print(secondMin(56,12,78,13,23,34,56,67))
    print(secondMin(4,7,2,4,5,8,1,0))
    print(secondMin('fg','we','aa','ab','jk','as','sa'))

    print(clrNonAlph('asddgr45-sfsds+.sdfgsd'))
    print(clrNonAlph('asdSDd5-sfs+.sАПgsd'))
    #print(clrNonAlph(5))
    try:
        print(clrNonAlph(5))
    except Exception as e:
        print('Exception: '+str(e))

