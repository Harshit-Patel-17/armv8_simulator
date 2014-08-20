'''
Created on Aug 8, 2014

@author: abhiagar90
'''

import decoder
import os


import parsehelper
import armdebug
from armdebug import isDebugMode, executeRegs, executeFlag
from utilFunc import resetInstrFlag
import sys
import global_data
import traceback
import mem
    
if __name__ == '__main__':
    
        filename=None
        
        if len(sys.argv)>3:
            print 'Too much arguments. Rerun with just --help for help'
            sys.exit(0)
        elif(len(sys.argv)==3):
            if(sys.argv[1]=='--debug'):
                filename=sys.argv[2]
                armdebug.startDebugMode()
            else:
                print 'Incorrect arguments. Rerun with just --help for help'
                sys.exit(0)
        elif (len(sys.argv)==2):
            if(sys.argv[1]=='--help'):
                armdebug.printMainHelp()
                sys.exit(0)
            filename = sys.argv[1]
            
        else:
            print 'Please enter a filename. Rerun with just --help for help'
            sys.exit(0)

        if not os.path.isfile(filename):
            print 'Not a file. Rerun with just --help for help'
            sys.exit(0)
            
        try:
            #here we first check for global data
            global_data.parseDataSection(filename)
            hexes=parsehelper.return_parsed_section(filename,'.text')
            parsehelper.fetch_PC(filename)
            #and now tell the parsehelper to save the inst to memory!!!
            #mem.init()
            
            #print hexes
        except:
            print traceback.format_exc()
            print "He's dead Larry." 
            print "The inputfile seems to be a not compatibe ARMv8 elf."
            sys.exit(0)
        
        
        armdebug.setHexes(hexes)
        armdebug.saveAllToMemoryModel()
        if isDebugMode():
            armdebug.startInteraction()
        else:        
            for hexcode in hexes:
                resetInstrFlag()
                decoder.decodeInstr(hexcode)
            print ''             
            executeRegs()
            print ''
            executeFlag()
        
'''            
def main():
    print "Inside Main"
    hexCode = "0a020020"   
    decoder.decodeInstr(hexCode) 
    printAllRegs()
    printAllFlags()
        
#main()'''