#!/usr/bin/python3
# -*- coding: utf-8 -

import sys
import json
from smallsmilhandler import SmallSMILHandler
from xml.sax import make_parser
from xml.sax.handler import ContentHandler
from urllib.request import urlretrieve


class KaraokeLocal(SmallSMILHandler):
    def __init__(self, fichero):
        parser = make_parser()
        cHandler = SmallSMILHandler()
        parser.setContentHandler(cHandler)
        parser.parse(open(fichero))
        self.Trunk = cHandler.get_tags()

    def do_local(self):
        '''
        Downloads the files contained on the URL,s
        '''

        doc = ""
        for dict_trunk in self.Trunk:
            for key in dict_trunk:
                doc = doc + key + "\t"
                for key_2 in dict_trunk[key]:
                    if str(dict_trunk[key][key_2])[0:7] == "http://":
                        url = dict_trunk[key][key_2]
                        dict_trunk[key][key_2] = url[url.rfind("/")+1:]
                        urlretrieve(url)

    def to_json(self, File, File_Name = ""):
        '''
        Rewrites the Trunk collection into a .json file
        '''
        if File_Name:
        	File = File_Name
        json_file = open(File, "w")
        json.dump(self.Trunk, json_file, separators=(',', ': '), indent=4)
        json_file.close()

    def __str__(self):

        '''
        Gives format to the collection "Trunk"
        Elemento1\tAtributo11="Valor11"\tAtributo12="Valor12"\t...\n
        '''

        doc = ""
        for dict_trunk in self.Trunk:
            for key in dict_trunk:
                doc = doc + key + "\t"
                for key_2 in dict_trunk[key]:
                    doc = doc + key_2 + '="' + dict_trunk[key][key_2] + '"' + "\t"
                doc = doc + "\n"
        print(doc)
        return(doc)

if __name__ == "__main__":
    try:
        fichero = sys.argv[1]
        Fich = KaraokeLocal(fichero)
    except:
        sys.exit("Usage: python3 karaoke.py file.smil")
    Fich_Json = sys.argv[1][:-5] + ".json"
    Fich.__str__()
    Fich.to_json(Fich_Json)
    Fich.do_local()
    Fich.to_json(Fich_Json, "local.json")
    Fich.__str__()