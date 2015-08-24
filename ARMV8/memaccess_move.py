'''
Created on Aug 8, 2014

@author: harinder
'''
import const
import utilFunc
import mem
import armdebug


def memaccessMov_iwi32(binary):
    mov_imm(binary, "MOV w", '1', 32)
    
def memaccessMov_iwi64(binary):
    mov_imm(binary, "MOV x", '1', 64)
    
def memaccessMov_wi32(binary):
    mov_imm(binary, "MOV w", '0', 32)
    
def memaccessMov_wi64(binary):
    mov_imm(binary, "MOV x", '0', 64)
    
def mov_imm(binary, instr, inverted, N):
    const.FLAG_MEMACCESS_EXECUTED = True    
    const.FLAG_MEMACCESS_COMPLETED = True
    if(armdebug.pipelineStages[4] != '--------'):
        return
    
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    mem.writeBackBuffer[0] = mem.ALUResultBuffer   
    mem.regValueAvailableInWB[rdKey] = True
    mem.regValueAvailableInWB_buffer_indices[rdKey] = 0
    #const.FLAG_MEMACCESS_EXECUTED = True
    #const.FLAG_MEMACCESS_COMPLETED = True

def mov_reg(binary, N):
    const.FLAG_MEMACCESS_EXECUTED = True    
    const.FLAG_MEMACCESS_COMPLETED = True
    if(armdebug.pipelineStages[4] != '--------'):
        return
    
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    mem.writeBackBuffer[0] = mem.ALUResultBuffer
    mem.regValueAvailableInWB[rdKey] = True
    mem.regValueAvailableInWB_buffer_indices[rdKey] = 0
    #const.FLAG_MEMACCESS_EXECUTED = True
    #const.FLAG_MEMACCESS_COMPLETED = True

def memaccessMov_r32(binary):
    mov_reg(binary, 32)
    
def memaccessMov_r64(binary):
    mov_reg(binary, 64)
                           
                           
def mov_bmi(binary, N):
    const.FLAG_MEMACCESS_EXECUTED = True    
    const.FLAG_MEMACCESS_COMPLETED = True
    if(armdebug.pipelineStages[4] != '--------'):
        return
    
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    mem.writeBackBuffer[0] = mem.ALUResultBuffer
    mem.regValueAvailableInWB[rdKey] = True
    mem.regValueAvailableInWB_buffer_indices[rdKey] = 0
    #const.FLAG_MEMACCESS_EXECUTED = True
    #const.FLAG_MEMACCESS_COMPLETED = True
    
def memaccessMov_bmi32(binary):
    mov_bmi(binary, 32)
    
def memaccessMov_bmi64(binary):
    mov_bmi(binary, 64)

#------------------- floating point moves----------------

def memaccessFMove_32toSP(binary):
    execFMOVE_general(binary,'0','00','00','111')

def memaccessFMove_SPto32(binary):
    execFMOVE_general(binary,'0','00','00','110')

def memaccessFMove_64toDP(binary):
    execFMOVE_general(binary,'1','01','00','111')

def memaccessFMove_64to128(binary):
    execFMOVE_general(binary,'1','10','01','111')

def memaccessFMove_DPto64(binary):
    execFMOVE_general(binary,'1','01','00','110')

def memaccessFMove_128to64(binary):
    execFMOVE_general(binary,'1','10','01','110')

def execFMOVE_general(binary,sf,typeBits,rmode,opcode):
    const.FLAG_MEMACCESS_EXECUTED = True    
    const.FLAG_MEMACCESS_COMPLETED = True
    if(armdebug.pipelineStages[4] != '--------'):
        return
    
    destRegister = utilFunc.getRegKeyByStringKey(binary[27:32])
    
    mem.writeBackBuffer[0] = mem.ALUResultBuffer

    if(opcode[2] == '1'):
        mem.regValueAvailableInFloatWB[destRegister] = True
        mem.regValueAvailableInFloatWB_buffer_indices[destRegister] = 0
    else:
        mem.regValueAvailableInWB[destRegister] = True
        mem.regValueAvailableInWB_buffer_indices[destRegister] = 0

def memaccessFMove_iSP(binary):
    const.FLAG_MEMACCESS_EXECUTED = True    
    const.FLAG_MEMACCESS_COMPLETED = True
    if(armdebug.pipelineStages[4] != '--------'):
        return
    
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    mem.writeBackBuffer[0] = mem.ALUResultBuffer
    mem.regValueAvailableInWB[rdKey] = True
    mem.regValueAvailableInWB_buffer_indices[rdKey] = 0

def memaccessFMove_iDP(binary):
    const.FLAG_MEMACCESS_EXECUTED = True    
    const.FLAG_MEMACCESS_COMPLETED = True
    if(armdebug.pipelineStages[4] != '--------'):
        return
    
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    mem.writeBackBuffer[0] = mem.ALUResultBuffer
    mem.regValueAvailableInWB[rdKey] = True
    mem.regValueAvailableInWB_buffer_indices[rdKey] = 0

def memaccessFMove_regSP(binary):
    const.FLAG_MEMACCESS_EXECUTED = True    
    const.FLAG_MEMACCESS_COMPLETED = True
    if(armdebug.pipelineStages[4] != '--------'):
        return
    
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    mem.writeBackBuffer[0] = mem.ALUResultBuffer
    mem.regValueAvailableInWB[rdKey] = True
    mem.regValueAvailableInWB_buffer_indices[rdKey] = 0

def memaccessFMove_regDP(binary):
    const.FLAG_MEMACCESS_EXECUTED = True    
    const.FLAG_MEMACCESS_COMPLETED = True
    if(armdebug.pipelineStages[4] != '--------'):
        return
    
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    mem.writeBackBuffer[0] = mem.ALUResultBuffer
    mem.regValueAvailableInWB[rdKey] = True
    mem.regValueAvailableInWB_buffer_indices[rdKey] = 0
