import writeback_dicts
import utilFunc
import const
import writeback_dicts_branch
import writeback_dicts_loadStore

def decodeInstr(hexCode): 
    binary = utilFunc.hexToBin(hexCode)
    const.FLAG_WRITEBACK_EXECUTED = False
    #Checking for branch type
    if(binary[3:6] == '101'):
        for i in range(4):
            writeback_dicts_branch.INSTRUCTION_TYPE(binary, i)
            if(const.FLAG_WRITEBACK_EXECUTED==True):
                break
    
    #Checking for load-store
    elif(binary[4] == '1' and binary[6] == '0'):
        for i in range(8):
            writeback_dicts_loadStore.INSTRUCTION_TYPE(binary, i)
            if(const.FLAG_WRITEBACK_EXECUTED==True):
                break
    
    if(const.FLAG_WRITEBACK_EXECUTED == False):
        for i in range(14):  
            writeback_dicts.INSTRUCTION_TYPE(binary, i)
            if(const.FLAG_WRITEBACK_EXECUTED==True):
                break
            
    if(const.FLAG_WRITEBACK_EXECUTED==False):
        print 'Sorry WRITEBACK!!! :( Instruction with hexCode: ' + hexCode + ' is incorrect or not supported'
