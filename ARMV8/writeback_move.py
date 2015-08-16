'''
Created on Aug 8, 2014

@author: harinder
'''
import const
import utilFunc
import mem
import armdebug

def writebackMov_iwi32(binary):
    mov_imm(binary, "MOV w", '1', 32)
    
def writebackMov_iwi64(binary):
    mov_imm(binary, "MOV x", '1', 64)
    
def writebackMov_wi32(binary):
    mov_imm(binary, "MOV w", '0', 32)
    
def writebackMov_wi64(binary):
    mov_imm(binary, "MOV x", '0', 64)
    
def mov_imm(binary, instr, inverted, N): 
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32]) 
    utilFunc.setRegValue(rdKey, mem.writeBackBuffer[0], '0')
    armdebug.intRFActivityCounter += 1
    const.FLAG_WRITEBACK_COMPLETED = True
    const.FLAG_WRITEBACK_EXECUTED = True
    mem.regObsolete[rdKey] -= 1

def mov_reg(binary, N):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    utilFunc.setRegValue(rdKey, mem.writeBackBuffer[0], '0')
    armdebug.intRFActivityCounter += 1
    const.FLAG_WRITEBACK_COMPLETED = True
    const.FLAG_WRITEBACK_EXECUTED = True
    mem.regObsolete[rdKey] -= 1

def writebackMov_r32(binary):
    mov_reg(binary, 32)
    
def writebackMov_r64(binary):
    mov_reg(binary, 64)
                           
                           
def mov_bmi(binary, N):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    utilFunc.setRegValue(rdKey, mem.writeBackBuffer[0], '1')
    armdebug.intRFActivityCounter += 1
    const.FLAG_WRITEBACK_COMPLETED = True
    const.FLAG_WRITEBACK_EXECUTED = True
    mem.regObsolete[rdKey] -= 1
    
def writebackMov_bmi32(binary):
    mov_bmi(binary, 32)
    
def writebackMov_bmi64(binary):
    mov_bmi(binary, 64)

#------------------- floating point moves----------------

def writebackFMove_SP(binary):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    utilFunc.setRegValueSIMDFP(rdKey, mem.writeBackBuffer[0])
    armdebug.floatRFActivityCounter += 1
    const.FLAG_WRITEBACK_COMPLETED = True
    const.FLAG_WRITEBACK_EXECUTED = True
    mem.regObsolete[rdKey] -= 1

def writebackFMove_DP(binary):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    utilFunc.setRegValueSIMDFP(rdKey, mem.writeBackBuffer[0])
    armdebug.floatRFActivityCounter += 1
    const.FLAG_WRITEBACK_COMPLETED = True
    const.FLAG_WRITEBACK_EXECUTED = True
    mem.regObsolete[rdKey] -= 1