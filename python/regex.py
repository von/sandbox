#!/usr/bin/env python
"""Example of using python regex"""

import re

regex="\d\d"
string="foo99bar"
# match() only checks begining while search() will match anywhere in string
print "re.match({}, {}) = {}".format(regex, string, re.match(regex, string)) 
print "re.search({}, {}) = {}".format(regex, string, re.search(regex, string)) 

compiled_regex = re.compile(regex)
print "compiled_regex.match({}) = {}"\
    .format(string, compiled_regex.match(string)) 
print "compiled_regex.search({}) = {}"\
    .format(string, compiled_regex.search(string)) 
