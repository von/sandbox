#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Kudos: http://www.knowthytools.com/2010/03/sax-parsing-with-python.html

import sys
import xml.sax

class MyContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)

    def startElement(self, name, attrs):
        print("startElement '" + name + "'")
        if name == "address":
            print("\tattribute type='" + attrs.getValue("type") + "'")

    def endElement(self, name):
        print("endElement '" + name + "'")

    def characters(self, content):
        print("characters '" + content + "'")


def main(argv=None):
    source = open("xml-sax.xml")
    xml.sax.parse(source, MyContentHandler())
    return(0)

if __name__ == "__main__":
    sys.exit(main())
