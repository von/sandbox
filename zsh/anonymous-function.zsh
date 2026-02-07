#!/usr/bin/env zsh
# Show the use of a zsh anonymous function for scoping variables.
#
# See:
# https://zsh.sourceforge.io/Doc/Release/Functions.html#Anonymous-Functions

local i="Hello world"

echo "Before anonymous function i=${i}"

# Anonymous function. Show we can have separately scoped variable 'i'
# After closing brace one can put arguments.
# Note errors in this function will be reported with a line number
# relative to the function, which is confusing.
function {
  local i=${1}
  echo "Inside anonymous function i=${i}"
} "Hello anonymous function"

echo "After anonymous function i=${i}"
exit 0
