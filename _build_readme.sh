#!/bin/bash

OUTPUT=./README.md
echo "# LeetCode " > $OUTPUT
now=$(date)
echo "### last update: ${now}" >> $OUTPUT


echo "## questions" > /tmp/README.md
echo "| problem | level| last modified |" >> /tmp/README.md
echo "|-|-|-|" >> /tmp/README.md


easy=0
medium=0
hard=0
for file_path in $(find . -name "README.md")
do
  if [ "$file_path" != "./README.md" ]; then
    info=$(head -n 2 "${file_path}")
    name=$(echo ${info} | sed 's/##/#/g' | cut -d '#' -f 2)
    level=$(echo ${info} |  cut -d ':' -f 2 | tr '[:upper:]' '[:lower:]' | tr -d '[:space:]')
    modified=$(date -r ${file_path})

    if [ "${level}" = "easy" ]; then
      ((easy+=1))
    fi
    if [ "${level}" = "medium" ]; then
      ((medium+=1))
    fi
    if [ "${level}" = "hard" ]; then
      ((hard+=1))
    fi


    echo "| [${name}]($file_path) | ${level} | ${modified} |" >> /tmp/README.md
  fi
done

echo "## summary" >> $OUTPUT
echo "| level | counts |" >> $OUTPUT
echo "|-|-|" >> $OUTPUT
echo "| easy |${easy} |" >> $OUTPUT
echo "| medium |${medium} |" >> $OUTPUT
echo "| hard |${hard} |" >> $OUTPUT
echo "" >> $OUTPUT
cat /tmp/README.md >> $OUTPUT
rm /tmp/README.md
