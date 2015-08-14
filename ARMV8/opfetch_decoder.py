import opfetch_dicts
import utilFunc
import const
import opfetch_dicts_branch
import opfetch_dicts_loadStore
import mem
import sys

def decodeInstr(hexCode): 
    binary = utilFunc.hexToBin(hexCode)
    #const.FLAG_OP_FETCHED = False
    const.FLAG_OPFETCH_EXECUTED = False
    mem.regObsolete_last_modified_indices = []
    #Checking for branch type
    if(binary[3:6] == '101'):
        for i in range(4):
            opfetch_dicts_branch.INSTRUCTION_TYPE(binary, i)
            if(const.FLAG_OPFETCH_EXECUTED==True):
                break
    
    #Checking for load-store
    elif(binary[4] == '1' and binary[6] == '0'):
        for i in range(8):
            opfetch_dicts_loadStore.INSTRUCTION_TYPE(binary, i)
            if(const.FLAG_OPFETCH_EXECUTED==True):
                break
    
    if(const.FLAG_OPFETCH_EXECUTED == False):
        for i in range(18):  
            opfetch_dicts.INSTRUCTION_TYPE(binary, i)
            if(const.FLAG_OPFETCH_EXECUTED==True):
                break
            
    if(const.FLAG_OPFETCH_EXECUTED==False):
        print 'Sorry!!! :( Instruction with hexCode: ' + hexCode + ' is incorrect or not supported in decode stage'
        sys.exit(1)
