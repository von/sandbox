#!/bin/bash
# Breadth-first search
#
# Find does a variant of depth-first search and while it has an option
# '-depth' for true depth-first search, it has no option for breadth-first
# search.  This means if you have a very deep and highly populated directory
# structure, it may be a long time before find prints all the top-level
# directories, which can be annoying if you are feeding its output to
# soundthing that is consuming it dynamically, such as fzf.
#
# The search is done with minimal buffering to work well with programs
# such as fzf.
#
# Kudos: https://unix.stackexchange.com/a/375375/29832

_bfs() {
  local depth=1
  # egrep is needed to detect when no files are found and we should stop.
  # sed demonstrates cleaning up each file as it is printed.
  # Note arguments to sed and egrep for linebuffering to promote quick output.
  # Use both -depth and -maxdepth: -depth makes the prune work right and
  # -maxdepth speeds things up greatly by pruning the search.
  while find "." "$@" -depth ${depth} -maxdepth ${depth} -print | \
    egrep --line-buffered ".*" ; do
    ((depth++))
  done | sed -l 's@^\./@@'
}

# Search for directories only, ignoring VCS directories
_bfs -name .git -prune -o -name .svn -prune -o -type d
