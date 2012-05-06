#!/usr/bin/env python
"""Demonstration of Mako"""

import mako  # pip install mako

from mako.template import Template

template_string = """\

## A simple comment

hello ${data}!

${"Stuff in brackets is evaluated by Python.".upper()}

${"HTML escaping: < less than > greater than" | h}

<%doc>
A multi-line comment.
</%doc>

<%
# This is a Block of raw python.
nums = range(5)
%>

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

print Template(template_string).render(data="world")

