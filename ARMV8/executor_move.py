'''
Created on Aug 8, 2014

@author: harinder
'''
import const
import utilFunc
import mem
import config
import armdebug


def execMov_iwi32(binary):
    mov_imm(binary, "MOV w", '1', 32)
    
def execMov_iwi64(binary):
    mov_imm(binary, "MOV x", '1', 64)
    
def execMov_wi32(binary):
    mov_imm(binary, "MOV w", '0', 32)
    
def execMov_wi64(binary):
    mov_imm(binary, "MOV x", '0', 64)
    
def mov_imm(binary, instr, inverted, N):
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
    if(inverted == '1'):
        mem.ALUResultBuffer = utilFunc.negate(mem.operand1Buffer)
    else:
        mem.ALUResultBuffer = mem.operand1Buffer
    mem.ALUResultBuffer = mem.ALUResultBuffer.zfill(const.REG_SIZE)
    mem.regValueAvailableInALU[rdKey] = True
    #const.FLAG_INST_EXECUTED = True
    #const.FLAG_EXECUTION_COMPLETED = True

def mov_reg(binary, N):
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
    mem.ALUResultBuffer = mem.operand1Buffer
    mem.ALUResultBuffer = mem.ALUResultBuffer.zfill(const.REG_SIZE)
    mem.regValueAvailableInALU[rdKey] = True
    #const.FLAG_INST_EXECUTED = True
    #const.FLAG_EXECUTION_COMPLETED = True

def execMov_r32(binary):
    mov_reg(binary, 32)
    
def execMov_r64(binary):
    mov_reg(binary, 64)
                           
                           
def mov_bmi(binary, N):
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
    mem.ALUResultBuffer = utilFunc.logical_or('0'*N,mem.operand1Buffer).zfill(const.REG_SIZE)
    mem.regValueAvailableInALU[rdKey] = True
    #const.FLAG_INST_EXECUTED = True
    #const.FLAG_EXECUTION_COMPLETED = True
    
def execMov_bmi32(binary):
    mov_bmi(binary, 32)
    
def execMov_bmi64(binary):
    mov_bmi(binary, 64)

#------------------- floating point moves----------------

def execFMove_32toSP(binary):
    execFMOVE_general(binary,'0','00','00','111')

def execFMove_SPto32(binary):
    execFMOVE_general(binary,'0','00','00','110')

def execFMove_64toDP(binary):
    execFMOVE_general(binary,'1','01','00','111')

def execFMove_64to128(binary):
    execFMOVE_general(binary,'1','10','01','111')

def execFMove_DPto64(binary):
    execFMOVE_general(binary,'1','01','00','110')

def execFMove_128to64(binary):
    execFMOVE_general(binary,'1','10','01','110')

def execFMOVE_general(binary,sf,typeBits,rmode,opcode):
    const.FLAG_INST_EXECUTED = True    
    if(const.FLAG_EXECUTION_COMPLETED == False and const.EXECUTION_COUNTER == 0):
        const.EXECUTION_COUNTER = config.latency['IntALU']
    
    if(const.EXECUTION_COUNTER != 0):
        armdebug.floatALUActivityCounter += 1
        const.EXECUTION_COUNTER -= 1
        
    if(const.EXECUTION_COUNTER == 0):
        const.FLAG_EXECUTION_COMPLETED = True
        if(armdebug.pipelineStages[3] != '--------'):
            return
    else:
        return
    
    destRegister = utilFunc.getRegKeyByStringKey(binary[27:32])

    if(sf == '1'):
        intsize = 64
    else:
        intsize = 32
        
    if((opcode[0:2]+rmode) == '1100'):
        part = 0
    elif((opcode[0:2]+rmode == '1101')):
        part = 1

    if(opcode[2] == '1'):
        operation = "IntToFlt"
    else:
        operation = "FltToInt"

    if(operation == "FltToInt"):
        if(part == 0):
            if(intsize == 32):
                resultBinary = mem.operand1Buffer[96:128]
            else:
                resultBinary = mem.operand1Buffer[64:128]
        else:
            resultBinary = mem.operand1Buffer[0:64]
        resultBinary = resultBinary.zfill(64)
    elif(operation == "IntToFlt"):
        if(part == 0):
            if(intsize == 32):
                resultBinary = mem.operand1Buffer[32:64]
            else:
                resultBinary = mem.operand1Buffer[0:64]
            resultBinary = resultBinary.zfill(128)
        else:
            resultBinary = mem.operand1Buffer[0:64]
            resultBinary = resultBinary + "0"*64
            
    mem.ALUResultBuffer = resultBinary
    if(operation == 'FltToInt'):
        mem.regValueAvailableInALU[destRegister] = True
    elif(operation == "IntToFlt"):
        mem.regValueAvailableInFloatALU[destRegister] = True


def execFMove_iSP(binary):
    const.FLAG_INST_EXECUTED = True    
    if(const.FLAG_EXECUTION_COMPLETED == False and const.EXECUTION_COUNTER == 0):
        const.EXECUTION_COUNTER = config.latency['IntALU']
    
    if(const.EXECUTION_COUNTER != 0):
        armdebug.floatALUActivityCounter += 1
        const.EXECUTION_COUNTER -= 1
        
    if(const.EXECUTION_COUNTER == 0):
        const.FLAG_EXECUTION_COMPLETED = True
        if(armdebug.pipelineStages[3] != '--------'):
            return
    else:
        return
    
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    resultBinary = utilFunc.VFPExpandImm(binary[11:19], 32)
    resultBinary = resultBinary.zfill(128)
    
    mem.ALUResultBuffer = resultBinary
    mem.regValueAvailableInALU[rdKey] = True

def execFMove_iDP(binary):
    const.FLAG_INST_EXECUTED = True    
    if(const.FLAG_EXECUTION_COMPLETED == False and const.EXECUTION_COUNTER == 0):
        const.EXECUTION_COUNTER = config.latency['IntALU']
    
    if(const.EXECUTION_COUNTER != 0):
        armdebug.floatALUActivityCounter += 1
        const.EXECUTION_COUNTER -= 1
        
    if(const.EXECUTION_COUNTER == 0):
        const.FLAG_EXECUTION_COMPLETED = True
        if(armdebug.pipelineStages[3] != '--------'):
            return
    else:
        return
    
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    resultBinary = utilFunc.VFPExpandImm(binary[11:19], 64)
    resultBinary = resultBinary.zfill(128)

    mem.ALUResultBuffer = resultBinary
    mem.regValueAvailableInALU[rdKey] = True

def execFMove_regSP(binary):
    const.FLAG_INST_EXECUTED = True    
    if(const.FLAG_EXECUTION_COMPLETED == False and const.EXECUTION_COUNTER == 0):
        const.EXECUTION_COUNTER = config.latency['IntALU']
    
    if(const.EXECUTION_COUNTER != 0):
        armdebug.floatALUActivityCounter += 1
        const.EXECUTION_COUNTER -= 1
        
    if(const.EXECUTION_COUNTER == 0):
        const.FLAG_EXECUTION_COMPLETED = True
        if(armdebug.pipelineStages[3] != '--------'):
            return
    else:
        return
    
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    resultBinary = utilFunc.getRegValueByStringkeyFPSIMD(binary[22:27])
    resultBinary = resultBinary[96:128]
    resultBinary = resultBinary.zfill(128)
    
    mem.ALUResultBuffer = resultBinary
    mem.regValueAvailableInALU[rdKey] = True

def execFMove_regDP(binary):
    const.FLAG_INST_EXECUTED = True    
    if(const.FLAG_EXECUTION_COMPLETED == False and const.EXECUTION_COUNTER == 0):
        const.EXECUTION_COUNTER = config.latency['IntALU']
    
    if(const.EXECUTION_COUNTER != 0):
        armdebug.floatALUActivityCounter += 1
        const.EXECUTION_COUNTER -= 1
        
    if(const.EXECUTION_COUNTER == 0):
        const.FLAG_EXECUTION_COMPLETED = True
        if(armdebug.pipelineStages[3] != '--------'):
            return
    else:
        return
    
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    resultBinary = utilFunc.getRegValueByStringkeyFPSIMD(binary[22:27])
    resultBinary = resultBinary[64:128]
    resultBinary = resultBinary.zfill(128)
    
    mem.ALUResultBuffer = resultBinary
    mem.regValueAvailableInALU[rdKey] = True
