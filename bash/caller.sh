#!/bin/bash
#
# Example of using 'caller'

function hello()
{
    world
}

function world()
{
    echo "Hello to my caller:"
    caller 0  # "0" causes function name to be included,
              # otherwise same as no arg
    echo "And my caller's caller:"
    caller 1
}

hello