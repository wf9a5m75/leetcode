#!/bin/bash

OUTPUT=./README.md
echo "# LeetCode " > $OUTPUT
now=$(date)
echo "### last update: ${now}" >> $OUTPUT


echo "" > /tmp/README.md

easy=0
medium=0
hard=0
total=0
for file_path in $(find . -name "README.md")
do
  if [ "$file_path" != "./README.md" ]; then
    info=$(head -n 2 "${file_path}")
    name=$(echo ${info} | sed 's/##/#/g' | cut -d '#' -f 2)
    level=$(echo ${info} |  cut -d ':' -f 2 | tr '[:upper:]' '[:lower:]' | tr -d '[:space:]')
    modified=$(stat -f "%Sm" -t "%Y-%m-%d %H:%M" ${file_path})
    modified_sort=$(stat -f "%Sm" -t "%Y%m%d%H%M" ${file_path})
    dir_path=$(dirname $file_path)

    if [ "${level}" = "easy" ]; then
      ((easy+=1))
    fi
    if [ "${level}" = "medium" ]; then
      ((medium+=1))
    fi
    if [ "${level}" = "hard" ]; then
      ((hard+=1))
    fi


    echo "${modified_sort}@| [${name}]($dir_path/) | ${level} | ${modified} | " >> /tmp/README.md
  fi
done
((total=easy+medium+hard))
echo "## summary" >> $OUTPUT
echo "| level | counts |" >> $OUTPUT
echo "|-|-|" >> $OUTPUT
echo "| easy |${easy} |" >> $OUTPUT
echo "| medium |${medium} |" >> $OUTPUT
echo "| hard |${hard} |" >> $OUTPUT
echo "| total | ${total} |" >> $OUTPUT
echo "" >> $OUTPUT
echo "## questions" >> $OUTPUT
echo "| problem | level| last modified |" >> $OUTPUT
echo "|-|-|-|" >> $OUTPUT

sort -t'@' -k1 -nr /tmp/README.md  | cut -d'@' -f 2 >> $OUTPUT
rm /tmp/README.md
