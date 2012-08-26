#!/bin/sh
#
# Start of script bash for bash...
#

set -o errexit  # Fail on any error
set -o nounset  # Unset variables are an error

######################################################################
#
# Support functions

DEBUG=0
debug()
# <message>
# Prints message if DEBUG is non-zero
{
    if [ ${DEBUG} -eq 1 ] ; then
        message "${1}"
    fi
}

QUIET=0
message()
# <message>
# Print message to stdout if QUIET is 0
{
    if [ ${QUIET} -eq 0 ] ; then
        echo ${1}
    fi
}

warn()
# <message>
# Write a message to stderr
{
    echo ${1} >&2
}

error()
# <message> [<exit status>]
# Write a message to stderr and exit
{
    warn "${1}"
    exit ${2:-1}
}

usage()
# Print usage
{
    message "Usage: $0 [-d|-q]"
}

######################################################################
#
# Main code

args=$(getopt dq $*)
set -- ${args}
for arg ; do
    case "${arg}" in
        -d)  # Debug mode
            DEBUG=1
            shift
            ;;
        -q)  # Quiet mode
            QUIET=1
            shift
            ;;
        --)
            shift
            break
            ;;
    esac
done

if test ${DEBUG} -eq 1 -a ${QUIET} -eq 1 ; then
    error "Debug (-d) and quiet (-q) modes are incompatible."
fi

debug "This is a debug message."
message "This is a normal message."
warn "This is a warning."

exit 0
