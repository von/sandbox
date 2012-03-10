#!/usr/bin/env python
"""Demonstration of using Tempita Templates

http://pythonpaste.org/tempita/
"""
from tempita import Template, bunch

import sys

# Differences from Django:
#
# * You can't have space between keywords (e.g., 'for' 'if') and the
# brackets.
#
# * You can't reference dictionay attributes by 'dict.attr' but must
# use normal dictionary methods - e.g. dict["attr"],
# dict.has_key("attr")

template_string = """
{{# This is a comment }}

{{py: def custom_filter(s): return "** " + s + " **"}}

My name is {{ my_name.capitalize() }}

{{# tempita.bunch is a dictionary with attribute access }}
Bunch test: {{a_bunch.a}}{{a_bunch.b}}{{a_bunch.c}}

{{# looper is a tempita object }}
{{for loop,name in looper(names)}}
Name: {{ name | custom_filter }} {{# Equivalent to 'custom_filter(name)' }} 
Number: {{ loop.number }}
{{endfor}}

{{for person in people}}
{{# Use 'plus_filter' from subtituions }}
Name: {{ person["name"] | plus_filter }} Role: {{ person["role"] }} {{if person.has_key("blackhat") }} (Bad guy) {{else}} (Good guy) {{endif}}
{{endfor}}
"""
t = Template(template_string)

def plus_filter(s): return "++ " + s + " ++"

context_params = {
    "my_name" : "alice",
    "names" : [ "alice", "bob", "eve" ],
    "people" : [
        { "name" : "alice", "role" : "communicator" },
        { "name" : "bob", "role" : "communicator" },
        { "name" : "eve", "role" : "eavesdropper", "blackhat" : True },
        ],
    "a_bunch" : bunch(a=1,b=2,c=3),
    "plus_filter" : plus_filter,  # Make available as filter
}

print t.substitute(context_params)

sys.exit(0)

