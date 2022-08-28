#!/usr/bin/env python3
# Shows ways of splitting longs strings over multiple lines.
# Kudos: https://stackoverflow.com/q/10660435/197789
import sys

long_string = "This is a very long string that goes on and on and on and on and on and on and on until it finally ends."

# Paren method
# https://stackoverflow.com/a/10660443/197789
# Note: no commas between strings and the whitespace explicitly in the
# string.
s = ("This is a very long string"
     " that goes on and on and on and"
     " on and on and on and on until"
     " it finally ends.")
assert long_string == s

# Backslash method
# https://stackoverflow.com/a/24331604/197789
# Note: whitespace explicitly in the string.
s = "This is a very long string" \
    " that goes on and on and on and" \
    " on and on and on and on until" \
    " it finally ends."
assert long_string == s

# Triple quote and replace method
# https://stackoverflow.com/a/14155520/197789
# Note indentation problems if not starting at zero indentation
# textwrap.dedent can help with this:
# https://docs.python.org/3/library/textwrap.html#textwrap.dedent
s = """This is a very long string
that goes on and on and on and
on and on and on and on until
it finally ends.""".replace('\n', ' ')
assert long_string == s

# Join method
# https://stackoverflow.com/a/24300699/197789
# Note the double quotes - join() is called with a tuple of strings.
s = " ".join(("This is a very long string",
               "that goes on and on and on and",
               "on and on and on and on until",
               "it finally ends."))
assert long_string == s

print("Success.")
sys.exit(0)
