#!/bin/bash

files=$(find . -name "input*.txt")
for file in $files
do
    sed -i '' -E 's/,/ /g' $file
    sed -i '' -E  's/\[|]//g' $file
done
