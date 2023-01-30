#!/usr/bin/env zsh
# The joys of variable expansion and word splitting (shwordsplit/SH_WORD_SPLIT).
# Kudos:
#   https://zsh.sourceforge.io/FAQ/zshfaq03.html#31
#   http://mywiki.wooledge.org/BashFAQ/050

echo "Set up:"
arg-count() { echo $# }
whence -f arg-count

s="A B C D"
echo "s=\"${s}\""

echo "Making sure shwordsplit is off"
echo "setopt +o shwordsplit"
setopt +o shwordsplit

echo ""
echo "Zsh does not split variables into words by defaul"
echo "arg-count \${s} = " $(arg-count ${s})

echo
echo "Splitting can be turned on for an invidivual expansion with \${=VAR}"
echo "arg-count \${=s} = " $(arg-count ${=s})

echo
echo "Or by 'setopt -o shwordsplit'"
setopt -o shwordsplit
echo "setopt -o shwordsplit"
echo "arg-count \${s} = " $(arg-count ${s})
setopt +o shwordsplit

echo
echo "SH_WORD_SPLIT also works..."
setopt -o SH_WORD_SPLIT
echo "setopt -o SH_WORD_SPLIT"
echo "arg-count \${s} = " $(arg-count ${s})
setopt +o SH_WORD_SPLIT

echo
echo "But, this splitting doesn't respecting quoting..."
s="The person said \"Hello world\""
echo "s=\"${s}\""
echo "arg-count \${=s} = " $(arg-count ${=s})

echo
echo "This can come up when you are passing snippets of shell code:"
print-stuff() { print $@ }
whence -f print-stuff
s="-f \"The answer is %d\" 42"
echo "s=\"${s}\""

echo
echo "You might expect:"
echo "print-stuff \${s} = The answer is 42"
echo "But you get:"
echo "print-stuff \${s} = " $(print-stuff ${s})
echo "Because the whole string is treated as one argument:"
echo "arg-count \${s} = " $(arg-count ${s})

echo
echo "And splitting doesn't help the way you hope..."
echo "arg-count \${=s} = " $(arg-count ${=s})
echo "print-stuff \${=s} = " $(print-stuff ${=s})

echo
echo "One way around this is to use eval in the function to treat"
echo "the passed string as the shell would (note this has security"
echo "issues - you mush trust the source of the string!)"
print-stuff-eval() { eval "print $@" }
whence -f print-stuff-eval
echo "print-stuff-eval \${s} = " $(print-stuff-eval ${s})

echo
echo "Arrays may be a better way."
echo "Use eval to split the string and create the array:"
echo "eval \"words=(\${s})\""
eval "words=(${s})"
echo "\${#words} = ${#words}"
# The following uses RC_EXPAND_PARAM
echo "Elements of words are:" \"${^words}\"
echo "arg-count \${words[@]} = " $(arg-count ${words[@]})
echo "print-stuff \${words[@]} = " $(print-stuff ${words[@]})

echo
echo "Can also pass as one string and use eval and an array in the function"
echo "to split the string."
print-split-stuff() { eval "a=($@)" ; print ${a} }
whence -f print-split-stuff
echo "print-split-stuff \${s} = " $(print-split-stuff ${s})

exit 0
