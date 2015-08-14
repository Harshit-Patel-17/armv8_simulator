'''
Created on Aug 8, 2014

@author: harinder
'''
import const
import utilFunc
import mem


def execMov_iwi32(binary):
    mov_imm(binary, "MOV w", '1', 32)
    
def execMov_iwi64(binary):
    mov_imm(binary, "MOV x", '1', 64)
    
def execMov_wi32(binary):
    mov_imm(binary, "MOV w", '0', 32)
    
def execMov_wi64(binary):
    mov_imm(binary, "MOV x", '0', 64)
    
def mov_imm(binary, instr, inverted, N):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    if(inverted == '1'):
        mem.ALUResultBuffer = utilFunc.negate(mem.operand1Buffer)
    else:
        mem.ALUResultBuffer = mem.operand1Buffer
    mem.ALUResultBuffer = mem.ALUResultBuffer.zfill(const.REG_SIZE)
    mem.regValueAvailableInALU[rdKey] = True
    const.FLAG_INST_EXECUTED = True

def mov_reg(binary, N):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    mem.ALUResultBuffer = mem.operand1Buffer
    mem.ALUResultBuffer = mem.ALUResultBuffer.zfill(const.REG_SIZE)
    mem.regValueAvailableInALU[rdKey] = True
    const.FLAG_INST_EXECUTED = True

def execMov_r32(binary):
    mov_reg(binary, 32)
    
def execMov_r64(binary):
    mov_reg(binary, 64)
                           
                           
def mov_bmi(binary, N):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    mem.ALUResultBuffer = utilFunc.logical_or('0'*N,mem.operand1Buffer).zfill(const.REG_SIZE)
    mem.regValueAvailableInALU[rdKey] = True
    const.FLAG_INST_EXECUTED = True
    
def execMov_bmi32(binary):
    mov_bmi(binary, 32)
    
def execMov_bmi64(binary):
    mov_bmi(binary, 64)

#------------------- floating point moves----------------

def execFMove_SP(binary):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    resultBinary = binary[11:19]
    resultBinary = resultBinary.zfill(128)

    utilFunc.setRegValueSIMDFP(rdKey, resultBinary)

def execFMove_DP(binary):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    resultBinary = binary[11:19]
    resultBinary = resultBinary.zfill(128)

    utilFunc.setRegValueSIMDFP(rdKey, resultBinary)
