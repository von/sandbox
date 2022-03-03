#!/usr/bin/env bash
#
# fzf examples derived from:
# https://github.com/junegunn/fzf/blob/master/ADVANCED.md

wait_for_key_press() {
  read -n1 -s -r -p $'Press "q" to quit, any key to continue...\n' key
  [[ $key = "q" ]] && exit 0
}

echo "Basic usage example..."
wait_for_key_press
pid=$(ps -ef | fzf | awk '{print $2}')
echo "Choosen pid is $pid"

export FZF_DEFAULT_OPTS="--height 40%"
echo "Basic example with \"$FZF_DEFAULT_OPTS\""
wait_for_key_press
pid=$(ps -ef | fzf | awk '{print $2}')
echo "Choosen pid is $pid"

export FZF_DEFAULT_OPTS="--height=40% --layout=reverse --info=inline --border --margin=1 --padding=1"
echo "Basic example with \"$FZF_DEFAULT_OPTS\""
echo "  --layout=reverse - display from top of screen"
echo "  --info-inline - display file infor on same line as prompt"
echo "  --margin=1 - space around the finder"
echo "  --padding=1 - space between border and finder"
wait_for_key_press
pid=$(ps -ef | fzf | awk '{print $2}')
echo "Choosen pid is $pid"

export FZF_DEFAULT_OPTS='--header "This is a Header" --header-lines=1 --height=40% --layout=reverse --info=inline --border --margin=1 --padding=1'
echo "Basic example with \"${FZF_DEFAULT_OPTS}\""
echo "  --header - Specify a fixed header"
echo "  --header-lines=1 - specify header lines in input that are not selectable"
wait_for_key_press
pid=$(ps -ef | fzf | awk '{print $2}')
echo "Choosen pid is $pid"

export FZF_DEFAULT_OPTS='--header-lines=1 --height=40% --layout=reverse --bind "ctrl-r:reload(date; ps -ef)"'
echo "Basic example with \"${FZF_DEFAULT_OPTS}\""
echo "  Reload with Ctrl-r"
wait_for_key_press
pid=$((date; ps -ef; ) | fzf | awk '{print $2}')
echo "Choosen pid is $pid"

export FZF_DEFAULT_OPTS='--prompt "All> " --header "CTRL-D: Directories / CTRL-F: Files" --bind "ctrl-d:change-prompt(Directories> )+reload(find * -type d)"  --bind "ctrl-f:change-prompt(Files> )+reload(find * -type f)"'
echo "Example with switching inputs \"${FZF_DEFAULT_OPTS}\""
echo "  --prompt - set prompt"
wait_for_key_press
pid=$(cd .. ; find * | fzf | awk '{print $2}')
echo "Choosen pid is $pid"

export FZF_DEFAULT_OPTS='--header "This is a Header" --header-lines=1 --height=40% --layout=reverse --info=inline --border --margin=1 --padding=1 --preview="echo {}" --preview-window=down,3,wrap'
echo "Basic example with preview: \"${FZF_DEFAULT_OPTS}\""
echo "  --preview - Command to preview option"
echo "  --preview-window=down,3,wrap - position at bottom, 3 lines, wrap lines"
wait_for_key_press
pid=$(ps -ef | fzf | awk '{print $2}')
echo "Choosen pid is $pid"

exit 0
