a=12
b=34
c=9

def greatest(a,b,c):
    if a>b and a>c :
        return a
    elif b>a and b>c:
            return b
    else:
            return c


print(greatest(a,b,c))