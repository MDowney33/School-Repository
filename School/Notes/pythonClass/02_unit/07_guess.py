import random

num = random.randint(1,10)
i = False
while i == False:
    numguess = int(input("Guess yo numba\n"))
    if numguess == num:
        print("you won!!")
        i = True
    elif numguess != num:
        print("wrong number")
    else:
        print("that number is not in the range")


myList = ['dog', 'dog', 'cat', 'cat']

l = myList.count('dog')
j = myList.count('cat')

if l>j:
    print('more dogs')
elif l==j:
    print('same')
else:
    print('more cats')
