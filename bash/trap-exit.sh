#!/bin/bash
#
# Catch an exit

trap catch_exit EXIT
trap 'catch_err ${LINENO} $?' ERR

function catch_err()
{
    MYSELF="$0"   # script name
    LINE="$1"     # last line of error occurence
    STATUS="$2"   # error code
    echo "catch_err() called from line ${LINE} with status ${STATUS}"
    echo "Returning to script..."
}

function catch_exit()
{
    read -p "Press Return to exit."
    echo "Exiting..."
}

echo "This will cause an error, calling catch_err() to be called."
cause_error

echo "Now we will exit, causing catch_exit() to be called."
exit 0

echo "Will not get here."
