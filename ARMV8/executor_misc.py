'''
Created on Aug 8, 2014

@author: abhiagar90
'''
import utilFunc
import armdebug
import mem
import const
import config
    
def execADR(binary):
    const.FLAG_INST_EXECUTED = True    
    if(const.FLAG_EXECUTION_COMPLETED == False and const.EXECUTION_COUNTER == 0):
        const.EXECUTION_COUNTER = config.latency['IntALU']
    
    if(const.EXECUTION_COUNTER != 0):
        const.EXECUTION_COUNTER -= 1
        
    if(const.EXECUTION_COUNTER == 0):
        const.FLAG_EXECUTION_COMPLETED = True
        if(armdebug.pipelineStages[3] != '--------'):
            return
    else:
        return
    
    rdKey=binary[-5:]
    regnum=utilFunc.uInt(rdKey)
    mem.ALUResultBuffer = mem.operand1Buffer + mem.operand2Buffer
    mem.ALUResultBuffer = utilFunc.intToBinary(mem.ALUResultBuffer, 64)
    mem.regValueAvailableInALU[regnum] = True
    #const.FLAG_INST_EXECUTED = True
    
def execADRP(binary):
    const.FLAG_INST_EXECUTED = True    
    if(const.FLAG_EXECUTION_COMPLETED == False and const.EXECUTION_COUNTER == 0):
        const.EXECUTION_COUNTER = config.latency['IntALU']
    
    if(const.EXECUTION_COUNTER != 0):
        const.EXECUTION_COUNTER -= 1
        
    if(const.EXECUTION_COUNTER == 0):
        const.FLAG_EXECUTION_COMPLETED = True
        if(armdebug.pipelineStages[3] != '--------'):
            return
    else:
        return
    
    rdKey=binary[-5:]
    regnum=utilFunc.uInt(rdKey)
    mem.ALUResultBuffer = mem.operand1Buffer + mem.operand2Buffer
    mem.ALUResultBuffer = utilFunc.intToBinary(mem.ALUResultBuffer, 64)
    mem.regValueAvailableInALU[regnum] = True
    #const.FLAG_INST_EXECUTED = True

def execNOP(binary):
    const.FLAG_INST_EXECUTED = True    
    if(const.FLAG_EXECUTION_COMPLETED == False and const.EXECUTION_COUNTER == 0):
        const.EXECUTION_COUNTER = config.latency['IntALU']
    
    if(const.EXECUTION_COUNTER != 0):
        const.EXECUTION_COUNTER -= 1
        
    if(const.EXECUTION_COUNTER == 0):
        const.FLAG_EXECUTION_COMPLETED = True
        if(armdebug.pipelineStages[3] != '--------'):
            return
    else:
        return
    #const.FLAG_INST_EXECUTED = True