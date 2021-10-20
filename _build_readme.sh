#!/bin/bash

OUTPUT=./README.md
echo "# LeetCode " > $OUTPUT
now=$(date)
echo "### last update: ${now}" >> $OUTPUT
echo "| problem | level| last modified |" >> $OUTPUT
echo "|-|-|-|" >> $OUTPUT


for file_path in $(find . -name "README.md")
do
  if [ "$file_path" != "./README.md" ]; then
    info=$(head -n 2 "${file_path}")
    name=$(echo ${info} | sed 's/##/#/g' | cut -d '#' -f 2)
    level=$(echo ${info} |  cut -d ':' -f 2 | tr '[:upper:]' '[:lower:]')
    modified=$(date -r ${file_path})

    echo "| [${name}]($file_path) | ${level} | ${modified} |" >> $OUTPUT
  fi
done
