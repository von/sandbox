#!/bin/bash
#
# Examples of doing arithmetic

a=$((7+8))
echo "a=$a"

b=$((${a}/5))
echo "b=$b"

# Declaring a variable as an integer allows arithmetic directly
declare -i i=5
echo "i=$i"
i+=7
echo "i=$i"
