#!/bin/bash -e

for i in content/*.md
do
    date=$(head -10 $i | grep "^Date:" | awk '{print $2}')
    year=$(echo $date | awk -F \- '{print $1}')
    month=$(echo $date | awk -F \- '{print $2}')
    dir="content/${year}/${month}"
    [[ -e $dir ]] || mkdir -p $dir

    ./wp_import_fixup.py $i
    mv $i $dir/
done
