#!/bin/sh

function add_prompt_func()
{
    __PROMPT_FUNCS=${__PROMPT_FUNCS}${__PROMPT_FUNCS:+ }${1}
}

function create_prompt()
{
    local prompt
    for func in ${__PROMPT_FUNCS} ; do
	local out=`$func`
	if test -n "${out}" ; then
	    prompt=${prompt}${prompt:+ }${out}
	fi
    done
    echo $prompt
}

function hello_world() {
    #echo "Hello world"
    echo ""
}
function hello_again() {
    echo "Hello again"
}
function goodbye() {
    echo "Goodbye"
}

add_prompt_func hello_world
echo ${__PROMPT_FUNCS}
add_prompt_func hello_again
echo ${__PROMPT_FUNCS}
add_prompt_func goodbye
echo ${__PROMPT_FUNCS}

create_prompt
