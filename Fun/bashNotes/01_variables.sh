#!/bin/bash

#myname="matthew" --def variable
#reference using $

#files=$(ls) --defines as output of command

#"" vs '' makes a difference between variables take into account or not

stuff="01_variables"
fileTest=$(ls $stuff)
echo $fileTest
