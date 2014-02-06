#!/bin/bash
# put every post in one category

for i in `find content/ -name "*.md"`
do
    echo "Doing ${i}"
    sed -i 's/^Category:.*/Category: mycat/' $i
done
