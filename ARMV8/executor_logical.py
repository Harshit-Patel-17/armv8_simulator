'''
Created on Aug 8, 2014

@author: harinder
'''

import utilFunc
import mem
import const
import config
import armdebug

def op_i(binary, N, setFlags):
    const.FLAG_INST_EXECUTED = True    
    if(const.FLAG_EXECUTION_COMPLETED == False and const.EXECUTION_COUNTER == 0):
        const.EXECUTION_COUNTER = config.latency['IntALU']
    
    if(const.EXECUTION_COUNTER != 0):
        armdebug.intALUActivityCounter += 1
        const.EXECUTION_COUNTER -= 1
        
    if(const.EXECUTION_COUNTER == 0):
        const.FLAG_EXECUTION_COMPLETED = True
        if(armdebug.pipelineStages[3] != '--------'):
            return
    else:
        return
    
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    mem.ALUResultBuffer = utilFunc.logical_and(mem.operand1Buffer,mem.operand2Buffer).zfill(const.REG_SIZE)
    mem.regValueAvailableInALU[rdKey] = True
    if(setFlags):
    	flags = mem.ALUResultBuffer[0] + utilFunc.isZero(mem.ALUResultBuffer) + '00'
    	utilFunc.setFlags(flags)
    const.FLAG_INST_EXECUTED = True

def execAnd_i32(binary):
    op_i(binary, 32, 0)
    
    
def execAnd_i64(binary):
    op_i(binary, 64, 0)

def execAnds_i32(binary):
	op_i(binary, 32, 1)

def execAnds_i64(binary):
	op_i(binary, 64, 1)
    
def execAnd_sr32(binary):
    const.FLAG_INST_EXECUTED = True    
    if(const.FLAG_EXECUTION_COMPLETED == False and const.EXECUTION_COUNTER == 0):
        const.EXECUTION_COUNTER = config.latency['IntALU']
    
    if(const.EXECUTION_COUNTER != 0):
        armdebug.intALUActivityCounter += 1
        const.EXECUTION_COUNTER -= 1
        
    if(const.EXECUTION_COUNTER == 0):
        const.FLAG_EXECUTION_COMPLETED = True
        if(armdebug.pipelineStages[3] != '--------'):
            return
    else:
        return
    
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    mem.ALUResultBuffer = utilFunc.logical_and(mem.operand1Buffer,mem.operand2Buffer).zfill(const.REG_SIZE)
    mem.ALUResultBuffer = mem.ALUResultBuffer.zfill(const.REG_SIZE)
    mem.regValueAvailableInALU[rdKey] = True
    const.FLAG_INST_EXECUTED = True
    
def execAnd_sr64(binary):
    const.FLAG_INST_EXECUTED = True    
    if(const.FLAG_EXECUTION_COMPLETED == False and const.EXECUTION_COUNTER == 0):
        const.EXECUTION_COUNTER = config.latency['IntALU']
    
    if(const.EXECUTION_COUNTER != 0):
        armdebug.intALUActivityCounter += 1
        const.EXECUTION_COUNTER -= 1
        
    if(const.EXECUTION_COUNTER == 0):
        const.FLAG_EXECUTION_COMPLETED = True
        if(armdebug.pipelineStages[3] != '--------'):
            return
    else:
        return
    
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    mem.ALUResultBuffer = utilFunc.logical_and(mem.operand1Buffer,mem.operand2Buffer).zfill(const.REG_SIZE)
    mem.ALUResultBuffer = mem.ALUResultBuffer.zfill(const.REG_SIZE)
    mem.regValueAvailableInALU[rdKey] = True
    const.FLAG_INST_EXECUTED = True

def execAnds_sr32(binary):
    const.FLAG_INST_EXECUTED = True    
    if(const.FLAG_EXECUTION_COMPLETED == False and const.EXECUTION_COUNTER == 0):
        const.EXECUTION_COUNTER = config.latency['IntALU']
    
    if(const.EXECUTION_COUNTER != 0):
        armdebug.intALUActivityCounter += 1
        const.EXECUTION_COUNTER -= 1
        
    if(const.EXECUTION_COUNTER == 0):
        const.FLAG_EXECUTION_COMPLETED = True
        if(armdebug.pipelineStages[3] != '--------'):
            return
    else:
        return
    
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    mem.ALUResultBuffer = utilFunc.logical_and(mem.operand1Buffer,mem.operand2Buffer).zfill(const.REG_SIZE)
    mem.ALUResultBuffer = mem.ALUResultBuffer.zfill(const.REG_SIZE)
    mem.regValueAvailableInALU[rdKey] = True
    flags = mem.ALUResultBuffer[0] + utilFunc.isZero(mem.ALUResultBuffer) + '00'
    utilFunc.setFlags(flags)
    const.FLAG_INST_EXECUTED = True

def execAnds_sr64(binary):
    const.FLAG_INST_EXECUTED = True    
    if(const.FLAG_EXECUTION_COMPLETED == False and const.EXECUTION_COUNTER == 0):
        const.EXECUTION_COUNTER = config.latency['IntALU']
    
    if(const.EXECUTION_COUNTER != 0):
        armdebug.intALUActivityCounter += 1
        const.EXECUTION_COUNTER -= 1
        
    if(const.EXECUTION_COUNTER == 0):
        const.FLAG_EXECUTION_COMPLETED = True
        if(armdebug.pipelineStages[3] != '--------'):
            return
    else:
        return
    
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    mem.ALUResultBuffer = utilFunc.logical_and(mem.operand1Buffer,mem.operand2Buffer).zfill(const.REG_SIZE)
    mem.ALUResultBuffer = mem.ALUResultBuffer.zfill(const.REG_SIZE)
    mem.regValueAvailableInALU[rdKey] = True
    flags = mem.ALUResultBuffer[0] + utilFunc.isZero(mem.ALUResultBuffer) + '00'
    utilFunc.setFlags(flags)
    const.FLAG_INST_EXECUTED = True
