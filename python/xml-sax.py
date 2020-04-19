#!/usr/bin/env python3
# Kudos: http://www.knowthytools.com/2010/03/sax-parsing-with-python.html

import sys
import xml.sax

class MyContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        xml.sax.ContentHandler.__init__(self)

    def startElement(self, name, attrs):
        print(f"startElement '{name}'")
        if name == "address":
            print(f"\tattribute type='{attrs.getValue('type')}'")

    def endElement(self, name):
        print(f"endElement '{name}'")

    def characters(self, content):
        print(f"characters '{content}'")


def main(argv=None):
    source = open("test.xml")
    xml.sax.parse(source, MyContentHandler())
    return(0)

if __name__ == "__main__":
    sys.exit(main())
