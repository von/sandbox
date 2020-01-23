#!/usr/bin/env bash
# Kudos: https://stackoverflow.com/a/33271194/197789

options=${*%${!#}} # all parameters except the last
echo "Options: ${options}"

last=${@:$#} # last parameter 
echo "Last parameter: ${last}"

exit 0
