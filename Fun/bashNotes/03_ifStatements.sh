#!/bin/bash

mynum=200

if [ $mynum -eq 200 ] #for opposite [ ! $mynum ... ]
#USE "man test" to see learn more about [ ] / test command
then
    echo "the condition is true"
else
    echo "the condition is not true"
fi

#Can check for the existence of a file
#adding -f before /workspaces... for if it's a file and -d for dir


if [ /workspaces/codespaces-blank/School ]; then
    echo "It exists"
else
    echo "It does not exist"
fi

#which command can check for existence of application is present
command=htop
#command=../../../../../../../usr/bin/htop

if command -v $command; then      #brackets indicate "test" command. command checks for the existence of a command
#if [ -f $command ]; then
    echo "$command is available"
else
    echo "$command is not available, installing it..."
    sudo apt update && sudo apt install -y  $command  #update (check up on) applications and if successuful install htop w/out prompting, assume yes
fi
$command
