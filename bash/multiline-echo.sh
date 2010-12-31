#!/bin/bash
#
# Use quoting to prevent echo from eating carriage returns

var="Line 1
Line 2
Line 3
"

echo "Unquoted echo, will eat carriage returns:"
echo ${var}

echo ""
echo "Quoted echo, will preserve carriage returns:"
echo "${var}"
