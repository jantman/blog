#!/bin/bash

for i in *.md
do
    echo $i
    date=$(head -10 $i | grep "^Date:" | awk '{print $2}')
    year=$(echo $date | awk -F \- '{print $1}')
    month=$(echo $date | awk -F \- '{print $2}')
    dir="${year}/${month}"
    [[ -e $dir ]] || mkdir -p $dir
    mv $i $dir/
done
