def basic1(a,b,c):
    return (a+b)/c

def basic2(a,b):
    return a**2 - b

def basic3(a,b):
    if (a+b)%2 == 0:
        return True
    else:
        return False

def basic4(a,b,c):
    return (a+b+c)/c


def vowelsquare(strAr):
    xLen = len(strAr[0])
    yLen = len(strAr)
    vowels = "aeiou"
    xind=0
    yind=0
    if xLen >=2 and yLen >= 2:
        xIndexes=[]
        yIndexes=[]
        boolMatrix=[]
        for i in strAr:     #makes a matrix of vowels being "1" and other as "0"
            boolMatrix.append("")
            for l in i:
                if l in vowels:
                    boolMatrix[yind]=boolMatrix[yind] + "1"
                else:
                    boolMatrix[yind]=boolMatrix[yind] + "0"
            yind+=1

        for i in boolMatrix: #finds a set of two vowels next to eachother in x-axis and appends index to a list
            xIndexes.append(str(i.find("11")))

        xIndex="".join(xIndexes) #turns the list into a string of same amount of characters
        xIndex=xIndex.replace("-1","-")

        while xind<len(xIndexes)-1: #finds repeating sets of 2 vowels and assigns index to value "yIndex"
            if xIndexes[xind]==xIndexes[xind+1]:
                yIndex=xIndex.find(str(xIndex[xind])*2)
                xIndex=xIndex[xind]
                break
            xind+=1

        if yIndex==-1:
            returnVar="1-0"
        else:
            returnVar=str(int(xIndex)+1)+"-"+str(yIndex+1) #just concatonates indexes as natural numbers

        return returnVar
    else:
        return "Matrix is not at least 2x2"

myArray = ["dweeapl","efaiffr","oufjfre","aepqrtr"]
print(vowelsquare(myArray))

#def questionmarks(myStr):
#    ind=0
#    questInd=[]
#    findNums=[]
#    for i in myStr:
#        if i = "???":
#            questInd.append(ind)
#        ind+=1
#    ind=0
#    for i in questInd:

def approxcbrt(arg):
    rt=arg**(1/3)
    print(rt)
    rtStr=str(rt)
    roundUp="56789"
    roundDown="1234"
    decPlace=str(rt).find(".")
    if len(rtStr[decPlace:]) >= 2 and decPlace != -1:
        print("l")
        if rtStr[decPlace+3] in roundUp:






approxcbrt(33)

