#!/bin/bash
#
# Example of 'complete -F' function

function _complete()
{
    # Three arguments:
    local _command=${1}
    local _word_being_completed=${2}
    local _word_before_word_being_completed=${3}

    echo "Command: ${_command}"
    echo "Word: ${_word_being_completed}"
    echo "Preceding word: ${_word_before_word_being_completed}"

    # The complete line
    echo "COMP_LINE=${COMP_LINE}"
    
    echo "\${COMP_LINE[\${COMP_POINT}]}=${COMP_LINE[${COMP_POINT}]}"

    # The complete line as an array
    echo "COMP_WORDS=${COMP_WORDS[*]}"
    # COMP_CWORD is index in COMP_WORDS to word being completed
    echo "\${COMP_WORDS[\${COMP_CWORD}]} = ${COMP_WORDS[${COMP_CWORD}]}"


    COMP_REPLY=("Array" "of" "possible" "completions")
}

complete -F _complete do_completion

# compgencan be used to make list of completions
# E.g. the following outputs all functions starting with _com
compgen -A function _com
