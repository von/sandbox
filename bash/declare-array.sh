#!/bin/bash
# Demonstrate that 'declare -ap' shows arrays as empty unless they
# are echo'd first.
pushd /tmp
pushd /etc
pushd /var
declare -ap | grep DIRSTACK  # Will show as empty
echo ${DIRSTACK[*]}
declare -ap | grep DIRSTACK  # Will show contents
