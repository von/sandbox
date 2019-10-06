#!/usr/bin/env bash
# Parse the output of 'git submodule status' with bash and a regex.
# Useful because this command covers unitialized submodules, unlike
# 'git submodule foreach'

parse_submodule_line() {
  # Kudos: https://stackoverflow.com/a/22539067/197789
  # Note that lack of quoting on regex important.
  # [:print:] is [:graph:] plus spaces, so [:print:]*[:graph:] matches
  # strings without space at end.
  if [[ "$line" =~ (.)([[:xdigit:]]+)\ ([[:print:]]*[[:graph:]])($|\ \([[:print:]]+\)$) ]] ; then
    local state=${BASH_REMATCH[1]}
    case "${state}" in 
      -) state="Not initialized" ;;
      +) state="SHA differs" ;;
      U) state="Merge conflicts" ;;
      ' ') state="";;
      ?) state="Unrecognized state: \"${state}\"" ;;
    esac
    local sha=${BASH_REMATCH[2]}
    local subpath=${BASH_REMATCH[3]}
    local desc=${BASH_REMATCH[4]}  # Needs clean up if present
    if [[ $desc =~ \(([[:print:]]+)\) ]]; then
      desc=${BASH_REMATCH[1]}
    fi
    echo "Submodule: $subpath"
    echo "SHA: $sha"
    [[ -n "${state}" ]] && echo "State: $state"
    [[ -n "${desc}" ]] && echo "Description: $desc"
  else
    echo "Match failed for: \"$line\""
  fi
}

# Kudos: https://stackoverflow.com/a/32931403/197789
mapfile -t lines < <( git submodule status )
for line in "${lines[@]}" ; do
  parse_submodule_line "${line}"
done
exit 0
