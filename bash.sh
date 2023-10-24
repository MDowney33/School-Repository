#!/bin/bash

#DEFINING VARIABLES
notes=Fun/bashNotes                                 #File Location
touch Other/Logs/bashNotes.log                  #Updates Log File
newstFileLog=Other/Logs/bashNotes.log           #Defines Log file Variable
newstFile=$(cat $newstFileLog)                                 #Defines Log file contents as Variable
space=`echo $'\n.'`
space=${space%.}
read -p "What would you like your file name to be?$space" fileName

#FUNCTIONS

findNumber () {                               #Finds and updates what notes we're on and converts to int if not already one
    #findNumber <string> <subString>
    fileNumber=${1%%$2*}
    if [ ${fileNumber:0:1} = 0 ]; then
        fileNumber=${fileNumber/0}
    fi
    fileNumber=$(($fileNumber + 1))
}

fileExist () {                                #Tests for existence of file while returning own str
    #fileExist <fileName>
    if ! [ -f $1 ]; then
        echo "Check if $newstFileLog has the latest file."
    fi
}

fileMakingProcess () {                        #Creates and opens file in nano
    #fileMakingProcess <int> <string> <typeOfFile>
    if [[ $1 -lt 10 && $1 -gt 0 ]]; then
        file="0${1}_${2}.${3}"
        #touch $notes/$file
        echo "#!/bin/bash" > $notes/$file
        nano $notes/$file
        echo $file > $newstFileLog
    else
        file="${1}_${2}.${3}"
        #touch $notes/$file
        echo "#!/bin/bash" > $notes/$file
        nano $notes/$file
        echo $file > $newstFileLog
    fi
    echo "File successfully created."
}

#SCRIPTRUN

findNumber $newstFile _
fileExist $notes/$newstFile
fileMakingProcess $fileNumber $fileName "sh"
