'''
@author: harinder
'''

import dicts
import utilFunc
import const
import dicts_branch
import dicts_loadStore
import sys
import mem

def decodeInstr(hexCode): 
    binary = utilFunc.hexToBin(hexCode)
    mem.regValueAvailableInALU = list(False for i in range(mem.regNum))
    mem.regValueAvailableInALU_last_modified_indices = []
    const.FLAG_INST_EXECUTED = False
    #Checking for branch type
    if(binary[3:6] == '101'):
        for i in range(4):
            dicts_branch.INSTRUCTION_TYPE(binary, i)
            if(const.FLAG_INST_EXECUTED==True):
                break
    
    #Checking for load-store
    elif(binary[4] == '1' and binary[6] == '0'):
        for i in range(8):
            dicts_loadStore.INSTRUCTION_TYPE(binary, i)
            if(const.FLAG_INST_EXECUTED=="1"):
                break

    if(const.FLAG_INST_EXECUTED==False):
        for i in range(23):
            dicts.INSTRUCTION_TYPE(binary, i)
            if(const.FLAG_INST_EXECUTED==True):
                break
            
    if(const.FLAG_INST_EXECUTED==False):
        print 'Sorry!!! :( Instruction with hexCode: ' + hexCode + ' is incorrect or not supported in execution stage'
        sys.exit(1)
