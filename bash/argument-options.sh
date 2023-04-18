#!/usr/bin/env bash
# Demonstrate how to slice commend-line options into arrays.
# Kudos:
# https://stackoverflow.com/a/33271194/197789
# https://stackoverflow.com/a/1215592/197789

# Everything but last parameter is an option.
# Use arrays to preserves whitespace in options
declare -a options
options=( "${@:1:$#-1}" ) # all parameters except the last

# '@Q' here adds quotes to options so when concatenated into string
# they get separated.
echo "Options: ${options[@]@Q}"

# No '@Q' here as extra quotes become part of option
for option in "${options[@]}" ; do
  echo "Option: $option"
done

# Last parameter is special.
last=${@:$#} # last parameter
echo "Last parameter: ${last}"

exit 0
