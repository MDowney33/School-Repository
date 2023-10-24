
#Define a function called hypotenuse that returns hypotenuse

def evenOdd(i: int) -> int:  #give int for int
    #DOCSTRING
    '''this program takes a number,
    returning 0 for even and 1 for odd'''
    i=i%2
    return i

print(evenOdd(-2))


help(evenOdd) #gives help on the function
