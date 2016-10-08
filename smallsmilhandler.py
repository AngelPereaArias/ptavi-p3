#!/usr/bin/python3
# -*- coding: utf-8 -*-

from xml.sax import make_parser
from xml.sax.handler import ContentHandler

class SmallSMILHandler(ContentHandler):

    def __init__(self):
        self.General = {"root-layout" : ["width", "height", "background_color"],
                    "region" : ["id", "top", "bottom", "left", "right"],
                    "img" : ["src", "region", "begin", "dur"],
                    "audio" : ["src", "begin", "dur"],
                    "textstreams" : ["src", "region"]}

if __name__ == "__main__":
    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    parser.parse(open("karaoke.smil"))
