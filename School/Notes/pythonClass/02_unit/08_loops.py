import random

ranNum = random.randint(1,1000)
game = False
numGuess = 0
myLis = []
#while game == False:

#    playerGuess = int(input("Guess your number: "))
#    if playerGuess == ranNum:
#        print("you won")
#        game = True
#        print("You guessed " + str(numGuess+1) + " times")
#    else:
#        if playerGuess > ranNum:
#            print("that number is too high!")
#        else:
#            print("that number is too low!")
#    myLis.append(playerGuess)
#    print("you've guessed: ")
#    print(myLis)
#    numGuess+=1

#i = 1
#x = 0
#while i <= 100:

#    triMultiple = i%3
#    septMult = i%7#

#    if triMultiple ==0 or septMult ==0:
#        print(i)
#        x+=1
#    if i == 101:
#        print("there are " + str(x) + " number of multiples")
#    i+=1

mystr = "the heights school"
i = 0
vowels = ['a', 'e', 'i', 'o', 'u']
while i < len(mystr):
    if mystr[i] in vowels:
        print(mystr[i])
    i += 1

L = ['Peter', 'Patrick', 'Joe']
i = 0

def loopP(a):
    i = 0
    while i < len(a):
        if a[i][0] == 'P':
            print(a[i])
        i+=1

loopP(L)

L1 = [2,6,3,8]
L2 = [4,3,5,7]

i = 0
while i < len(L1):
    if L1[i] > L2[i]:
        print(L1[i])
    else:
        print(L2[i])
    i+=1
