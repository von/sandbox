#!/usr/bin/env bash
#
find * | \
  fzf --ansi --no-sort --reverse --tiebreak=index \
      --height=50% --layout=reverse --info=inline --border --margin=1 --padding=1 \
      --preview="ls -l {}" --preview-window=down,3,wrap \
      --bind "ctrl-m:execute:less {}" \
      --bind "e:execute:view {}" \
      --bind "p:toggle-preview" \
      --bind "q:abort"
