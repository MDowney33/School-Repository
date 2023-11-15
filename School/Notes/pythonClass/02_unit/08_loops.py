import random

ranNum = random.randint(1,10)
game = False
numGuess = 0
myLis = []
while game == False:

    playerGuess = int(input("Guess your number: "))
    if playerGuess == ranNum:
        print("you won")
        game = True
        print("You guessed " + str(numGuess+1) + " times")
        print("These were your guesses:")
        print(myLis.append(playerGuess))
    else:
        print("that's not right!")
    myLis.append(playerGuess)
    numGuess+=1
