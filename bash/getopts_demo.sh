#!/bin/sh
#
# Example of using getopts

# Leading colon means silent errors, script will handle them
# Colon after a parameter, means that parameter has an argument
while getopts ":a" opt; do
  case $opt in
    a)
      echo "-a was triggered!" >&2
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      ;;
  esac
done

shift $(($OPTIND - 1))

echo "$@"
