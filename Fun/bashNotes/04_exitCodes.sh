#!/bin/bash

ls -l
echo $?       #echo's the exit code of last command. 0 = success, anything else = failure

package=htop
sudo apt install $package #>> something.log      --moves output to file rather than on screen-is cleaner

if [ $? -eq 0 ]; then
    echo "Installation of package was successful. Command located here:" && which $package
else
    echo "Package failed to install"
fi

#exit <number>     --forces exit code to be equal to x
#exit --exits script with exit code of typed num
#therefore useful to use in else statements
