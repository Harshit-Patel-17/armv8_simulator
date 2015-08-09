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
import const
    
if __name__ == '__main__':
    
        filename=None
        totalArguments = len(sys.argv)
        
        if(totalArguments > 4):
            print 'Too much arguments. Rerun with just --help for help'
            sys.exit(0)
        else:
            if(sys.argv[totalArguments-1] == '--forward'):
                const.FLAG_DATA_FORWARDING = True
                totalArguments -= 1
            if(totalArguments > 3):
                print 'Too much arguments. Rerun with just --help for help'
                sys.exit(0)
            elif(totalArguments == 3):
                if(sys.argv[1] == '--debug'):
                    filename=sys.argv[2]
                    armdebug.startDebugMode()
                else:
                    print 'Incorrect arguments. Rerun with just --help for help'
                    sys.exit(0)
            elif (totalArguments == 2):
                if(sys.argv[1] == '--help'):
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
            armdebug.startRunEngine() 
            print ''             
            executeRegs()
            print ''
            executeFlag()