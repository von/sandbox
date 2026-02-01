#!/usr/bin/env zsh
# Examples of associate arrays.
# Kudos:
# https://scriptingosx.com/2019/11/associative-arrays-in-zsh/

# File with associate array
local afile=$(dirname $0)/associative-array.txt

typeset -A a

echo "Populating array in bulk..."
a=(key1 value1 key2 value2 key3 value3)

echo "Assigning an individual element..."
a[key4]=value4

echo "Iterating over keys and values..."
for key value in ${(kv)a}; do
  echo "$key -> $value"
done

echo "Iterating over keys only..."
for key in ${(k)a}; do
  echo "Key: $key, Value: $a[$key]"
done

echo "Checking for key2 existence..."
if [[ -v a[key2] ]]; then
  echo "Key2 exists!"
else
  echo "Key2 does not exist."
fi

echo "Deleteing key2..."
unset 'a[key2]'

echo "Checking for key2 existence..."
if [[ -v a[key2] ]]; then
  echo "Key2 exists!"
else
  echo "Key2 does not exist."
fi

echo "Reading associative array from ${afile}..."
a=()
while read -r key value; do
  a[$key]="$value"
done < ${afile}

echo "Keys: ${(k)a}"
echo "Values: ${(v)a}"

exit 0
