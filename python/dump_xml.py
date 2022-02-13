#!/usr/bin/env python3
import xml.dom.minidom

dom = xml.dom.minidom.parse('./test.xml')
print(dom.toprettyxml())
