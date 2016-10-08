#!/usr/bin/python3
# -*- coding: utf-8 -*-

from smallsmilhandler import SmallSMILHandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
import json

def Format_Trunk(Trunk):
	for i in range(len(Trunk)):
		print(Trunk[i])

if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    try:
    	parser.parse(open(sys.argv[1]))     
    except:
        sys.exit("Usage: python3 karaoke.py file.smil.")

    Format_Trunk(cHandler.get_tags())