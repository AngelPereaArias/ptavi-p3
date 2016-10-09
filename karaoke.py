#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import json
from smallsmilhandler import SmallSMILHandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler



def Create_Json(doc):
	'''
	Rewrites the doc collection into a .json file
	'''
	
	json_file = open(sys.argv[1][:-5] + ".json", "w")
	json.dump(doc, json_file)
	json_file.close()

def Format_Trunk(Trunk):
	'''
	Gives format to the collection "Trunk" 
	Elemento1\tAtributo11="Valor11"\tAtributo12="Valor12"\t...\n
	'''

	doc = ""
	for dict_trunk in Trunk:
		for key in dict_trunk:
			doc = doc + key + "\t"
			for key_2 in dict_trunk[key]:
				doc = doc + key_2 + '="' + dict_trunk[key][key_2] + '"' + "\t"
			doc = doc + "\n"
	return doc

if __name__ == "__main__":

    parser = make_parser()
    cHandler = SmallSMILHandler()
    parser.setContentHandler(cHandler)
    try:
    	parser.parse(open(sys.argv[1]))     
    except:
        sys.exit("Usage: python3 karaoke.py file.smil.")

    Create_Json(Format_Trunk(cHandler.get_tags()))