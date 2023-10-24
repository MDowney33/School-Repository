def avgThree(a,b,c,d):
    t = a+b+c+d
    t -= min(a,b,c,d)
    return t/3
print(avgThree(1,2,3,4))


def absolut(x:float,y:float) -> float:
    '''
    Takes absolute value of x-y
    '''
    return abs(x-y)

print(absolut(2,1))


def d(a):
    a/=1.6
    return a

print(d(5))

def avgGrade(a:float,b:float,c:float) -> float:
    d=(a+b+c)/3
    return d

print(avgGrade(55,66,77))


def funct(a, b, c):
    return max(a,b,c) * min(a,b,c)
print(funct(1,2,3))

def funct2(a,b,c,d):
    avg = (a*b*c*d)/4
    other = abs(min(a,b,c,d) - max(a,b,c,d))
    return other*avg
print(funct2(1,2,3,4))

