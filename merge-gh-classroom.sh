#! /bin/bash
while IFS="," read -r rec_column1 rec_column2 rec_column3 rec_column4 r5 r6 r7 r8 r9 r10
do
  temp="${r7%\"}"
  temp="${temp#\"}"
  url="$temp/pull/1"
  echo "USERNAME: $rec_column4"
  echo "URL: $url"
  
  gh pr merge $url --merge
done < <(tail -n +2 ps3b-repos-2.csv)
