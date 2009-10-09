#!/usr/bin/python
import sys
import xml.dom.minidom
from xml.dom.ext import PrettyPrint

dom = xml.dom.minidom.parse('./test.xml')

PrettyPrint(dom)




