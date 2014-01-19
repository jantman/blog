#!/bin/bash

for i in *.rst
do
    echo $i
    date=$(head -10 $i | grep "^:date:" | awk '{print $2}')
    year=$(echo $date | awk -F \- '{print $1}')
    month=$(echo $date | awk -F \- '{print $2}')
    dir="${year}/${month}"
    [[ -e $dir ]] || mkdir -p $dir
    mv $i $dir/
done
