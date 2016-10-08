#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.trunk = []
        self.General = {"root-layout" : ["width", "height", "background-color"],
                    "region" : ["id", "top", "bottom", "left", "right"],
                    "img" : ["src", "region", "begin", "dur"],
                    "audio" : ["src", "begin", "dur"],
                    "textstreams" : ["src", "region"]}


    def startElement(self, name, attrs):

        if name in self.General:
            Value_Box = {}
            for i in self.General[name]:
                Value_Box[i] = attrs.get(i, "Empty attrs")

            General_Slice = {name : Value_Box}
            self.trunk.append(General_Slice)

    def get_tags(self):
        return self.trunk

if __name__ == "__main__":
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open("karaoke.smil"))
    print(cHandler.get_tags())
