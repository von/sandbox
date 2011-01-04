#!/bin/bash
#
# Demonstrate that 'declare -x' (or '+x') in a function makes a
# variable local.  Not sure if this is a bug or not.
#
# Expected output:
# Function change_foo1 did not change foo: "HELLO" = "HELLO"
# Function change_foo2 did change foo: "HELLO ALL" != "HELLO"
# Function change_foo3 did not change foo: "HELLO" = "HELLO"
# Function change_foo4 did change foo: "HELLO THERE" != "HELLO"
#
# With
# GNU bash, version 3.2.48(1)-release (x86_64-apple-darwin10.0)


function change_foo1()
{
    # changes to foo will be local
    declare -x foo
    foo+=" WORLD"
}

function change_foo2()
{
    # changes to foo will be global
    foo+=" ALL"
}

function change_foo3()
{
    # changes to foo will be local
    declare +x foo
    foo+=" AGAIN"
}

function change_foo4()
{
    # 'export' does not make foo local
    export foo
    foo+=" THERE"
}

for f in change_foo1 change_foo2 change_foo3 change_foo4 ; do
    foo="HELLO"
    foo_orig=${foo}
    ${f}
    if test "${foo}" = "${foo_orig}" ; then
	echo "Function ${f} did not change foo: \"${foo}\" = \"${foo_orig}\""
    else
	echo "Function ${f} did change foo: \"${foo}\" != \"${foo_orig}\""
    fi
done
