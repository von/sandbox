#!/bin/sh
#
# Example of using getopts

usage() {
    cat <<EOF
Usage: $0 [<options>]
EOF
}

# Leading colon means silent errors, script will handle them
# Colon after a parameter, means that parameter has an argument
while getopts ":ab:h" opt; do
  case $opt in
    a)
      echo "-a was triggered!" >&2
      ;;
    b)
      echo "-b $OPTARG was given." >&2
      ;;
    h)
      usage
      ;;
    \?)
      echo "Invalid option: -$OPTARG" >&2
      ;;
    :)
      echo "Option -$OPTARG requires an argument." >&2
      exit 1
      ;;
  esac
done

shift $(($OPTIND - 1))

echo "Extra arguments: $@"
exit 0
