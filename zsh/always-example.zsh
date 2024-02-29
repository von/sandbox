#!/usr/bin/env zsh
# Example of 'always'
# See https://zsh.sourceforge.io/Doc/Release/Shell-Grammar.html#Complex-Commands

{
  echo "try block"
} always {
  echo "always block"
}
echo "Status should be 0: $?"

{
  foo="bar"
  echo "Beofre an error..."
  break  # will cause error
  echo "After error - shouldn't see this."
} always {
  echo "always after error"
  echo "Showing foo was set: foo=${foo}"
  echo "Exit will follow now with status == 1"
}
echo "This code will not be reached."
exit 0
