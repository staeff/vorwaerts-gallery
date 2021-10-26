#!/bin/bash
FILES="$@"
for i in $FILES
do
echo "Processing image $i ..."
/usr/local/bin/convert -thumbnail x400 $i thumbs/`basename $i`
done
