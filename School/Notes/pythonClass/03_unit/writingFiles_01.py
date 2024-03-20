#The TextIO Class is object representing data on the hard drive.
#We instantiate using built-in function open()

#Open function takes at least 2 args, the name as well as mode -- 'r','w','a','x' which read, erase and write, append, and x is like w except if it already exists nothing happens
#read methon returns all the text in a file as a string
#file.readlines() gives list of lines
#file.strip() gets rid of whitespace
#You can iterate over a file to get a line each iteration
#file.read(<int>) reads certain number of characters
#WHEN FINISHED ALWAYS USE close() method

#Writing to files
newFile = open('new.txt', 'w')
newFile.write('Hi mom!')
