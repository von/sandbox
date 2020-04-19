#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Demonstration of Mako

Unicode howto: https://docs.makotemplates.org/en/latest/unicode.html

The 'coding' line above lets this file contain unicode characters.
"""

import mako  # pip install mako

from mako.template import Template

template_string = """\

## A simple comment

hello ${data}, ${unicode_data}, and Ivan Krstić!

${"Stuff in brackets is evaluated by Python.".upper()}

${"HTML escaping: < less than > greater than" | h}

<%doc>
A multi-line comment.
</%doc>

<%
# This is a Block of raw python.
max = 5
nums = range(max)
%>


## Accept variable set in Python block
Max is ${max}.

<%def name="myfunc(n)">
   % if n == 3:
       3!
    % else:
       Not 3.
    %endif
</%def>

% for a in nums:
    ${myfunc(a)}
%endfor
"""

t = Template(template_string,
             # Automaticlaly decode all expressions from unicode
             # This lets parameters to render() contain unicode
             # https://docs.makotemplates.org/en/latest/filtering.html
             default_filters=['decode.utf8'],
             # This lets the template_string contain unicode
             input_encoding='utf-8',
             # This lets the output be witten to a file
             output_encoding='utf-8'
             )
print t.render(data="world", unicode_data="Ivan Krstić")
