#!/bin/bash
temp=$#
if [ -s "$temp" ]
then
	echo "File exists"
else
	echo "File not found"
fi	

echo "adding a new line"
sh temp.sh path/test.txt

New line added 
