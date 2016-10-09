#!/usr/bin/python3
# -*- coding: utf-8 -*-

from smallsmilhandler import SmallSMILHandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
import sys
import json

def Format_Trunk(Trunk):
	'''
	
	'''
	doc = ""
	for dict_trunk in Trunk:
		for key in dict_trunk:
			doc = doc + key + '\t'
			for key_2 in dict_trunk[key]:
				doc = doc + key_2 + '="' + dict_trunk[key][key_2] + '"' + "\t"
			doc = doc + "\n"
	print(doc)

if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    try:
    	parser.parse(open(sys.argv[1]))     
    except:
        sys.exit("Usage: python3 karaoke.py file.smil.")

    Format_Trunk(cHandler.get_tags())