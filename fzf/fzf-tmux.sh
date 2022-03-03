#!/usr/bin/env bash
#
# fzf-tmux examples derived from:
# https://github.com/junegunn/fzf/blob/master/ADVANCED.md

wait_for_key_press() {
  read -n1 -s -r -p $'Press "q" to quit, any key to continue...\n' key
  [[ $key = "q" ]] && exit 0
}

if test -z "$TMUX" ; then
  echo "Not in tmux. Exiting."
  exit 0
fi

echo "Basic example with fzf-tmux"
echo "Note that \$FZF_DEFAULT_OPTS doesn't work for layout options."
wait_for_key_press
pid=$(ps -ef | fzf-tmux | awk '{print $2}')
echo "Choosen pid is $pid"

FZF_TMUX_OPTS="-u 30%"
echo "Basic example with fzf-tmux $FZF_TMUX_OPTS"
echo "  -u 30% - display above prompt using 30% of screen"
echo "           (-l and -r are also options)"
wait_for_key_press
pid=$(ps -ef | fzf-tmux $FZF_TMUX_OPTS | awk '{print $2}')
echo "Choosen pid is $pid"

export FZF_TMUX_OPTS="-p 80%,60%"
echo "Basic example with fzf-tmux $FZF_TMUX_OPTS"
echo "  -p 80%,60% - Use popup with 80% width, 60% height"
wait_for_key_press
pid=$(ps -ef | fzf-tmux $FZF_TMUX_OPTS | awk '{print $2}')
echo "Choosen pid is $pid"

exit 0
