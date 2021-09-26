#!/bin/bash
temp=$#
if [ -s "$temp" ]
then
	echo "File exists"
else
	echo "File not found"
fi	

echo "adding a new line"
echo "adding another line from github console"
sh temp.sh path/test.txt

New line added 
