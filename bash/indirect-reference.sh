#!/bin/bash
#
# Demonstrate indirect referencing
#
# Request BASH v2 or later

function print_value()
# Given the name of the variable, print i
{
    echo ${!1}

    # Old pre-v2 way
    eval echo "\$${1}"
}

FOO="Hello world!"
print_value FOO
