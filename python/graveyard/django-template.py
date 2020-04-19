#!/usr/bin/env python
"""Demonstration of using Django Templates"""
from django.template import Context, Template
from django.conf import settings

import sys

# Avoid needing to set DJANGO_SETTINGS_MODULE
settings.configure(DEBUG=True, TEMPLATE_DEBUG=True)

template_string = """
My name is {{ my_name }} and my age is {{ my_age|default:"undefined" }}.
Number of names: {{ names|length }}
{% for name in names %} Name: {{ name }} 
{% endfor %}
{% for person in people %} Name: {{ person.name }} Role: {{ person.role }} {% if person.blackhat %} (Bad guy) {% else %} (Good guy) {% endif %}
{% endfor %}
"""
t = Template(template_string)

context_params = {
    "my_name" : "Alice",
    "names" : [ "Alice", "Bob", "Eve" ],
    "people" : [
        { "name" : "Alice", "role" : "communicator" },
        { "name" : "Bob", "role" : "communicator" },
        { "name" : "Eve", "role" : "eavesdropper", "blackhat" : True },
        ],
}

context = Context(context_params)
print t.render(context)

sys.exit(0)

