import memaccess_dicts
import utilFunc
import const
import memaccess_dicts_branch
import memaccess_dicts_loadStore
import sys
import mem

def decodeInstr(hexCode): 
    binary = utilFunc.hexToBin(hexCode)
    mem.regValueAvailableInWB = list(False for i in range(mem.regNum))
    mem.regValueAvailableInWB_buffer_indices = list(-1 for i in range(mem.regNum))
    mem.regValueAvailableinWB_last_modified_indices = []
    const.FLAG_MEMACCESS_EXECUTED = False
    #Checking for branch type
    if(binary[3:6] == '101'):
        for i in range(4):
            memaccess_dicts_branch.INSTRUCTION_TYPE(binary, i)
            if(const.FLAG_MEMACCESS_EXECUTED==True):
                break
    
    #Checking for load-store
    elif(binary[4] == '1' and binary[6] == '0'):
        for i in range(8):
            memaccess_dicts_loadStore.INSTRUCTION_TYPE(binary, i)
            if(const.FLAG_MEMACCESS_EXECUTED==True):
                break
    
    if(const.FLAG_MEMACCESS_EXECUTED == False):
        for i in range(23):  
            memaccess_dicts.INSTRUCTION_TYPE(binary, i)
            if(const.FLAG_MEMACCESS_EXECUTED=="1"):
                break
            
    if(const.FLAG_MEMACCESS_EXECUTED==False):
        print 'Sorry!!! :( Instruction with hexCode: ' + hexCode + ' is incorrect or not supported in memory access stage'
        sys.exit(1)
