#!/bin/bash
# Timout a command in bash
#
# Kudos:
# http://www.bashcookbook.com/bashinfo/source/bash-4.0/examples/scripts/timeout3
# http://stackoverflow.com/questions/81520/how-to-suppress-terminated-message-after-killing-in-bash/81539#81539

function timeout()
{
    # Usage: <timeout> <command> <args...>
    timeout=$1; shift
    
    $* &

    child_pid=$!
    # Avoid termination message
    disown $child_pid

    # How frequently to check child
    interval=1

    while ((timeout > 0)); do
	# kill -0 <pid> tells if process can receive a signal (is alive)
	# See if child still alive
	if kill -0 $child_pid 2> /dev/null ; then
	    # Still alive, sleep and check it again until we hit timeout
	    sleep $interval
	    ((timeout -= interval))
	else
	    # Child dead, get and return exit status
	    wait $child_pid
	    return $?
	fi
    done

    # We timed out, kill child, nicely first with SIGTERM
    kill -s SIGTERM $child_pid 2> /dev/null
    kill -0 $child_pid 2> /dev/null || return 
    sleep $interval
    kill -0 $child_pid 2> /dev/null || return
    # SIGTERM didn't work, use SIGKILL
    kill -s SIGKILL $child_pid 2> /dev/null
}

echo "Calling timeout 2 sleep 10"
date
timeout 2 sleep 10
date
echo "Done."
exit 0

