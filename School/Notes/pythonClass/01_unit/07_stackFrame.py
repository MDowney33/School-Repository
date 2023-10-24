
x1="hi"
x2=4
x3=6
x4=8



def averageFour(a, b, c, d) -> float:
    '''Takes four floats and returns a float average b/w the numbers'''
    print(a, b, c, d)
    answ = (a+b+c+d)/4
    return answ
print(averageFour(4,5,6,7))



def avgFour(int1, int2, int3, int4):
    r = int1 + int2 + int3 + int4
    r /= 4
    """
    returns the average of 4 numbers
    """
    return r

print(float(avgFour(float(input("Number 1: ")) ,float(input("Number 2: ")), float(input("Number 3: ")), float(input("Number 4: ")))))
