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

def writebackFMove_32toSP(binary):
    execFMOVE_general(binary,'0','00','00','111')

def writebackFMove_SPto32(binary):
    execFMOVE_general(binary,'0','00','00','110')

def writebackFMove_64toDP(binary):
    execFMOVE_general(binary,'1','01','00','111')

def writebackFMove_64to128(binary):
    execFMOVE_general(binary,'1','10','01','111')

def writebackFMove_DPto64(binary):
    execFMOVE_general(binary,'1','01','00','110')

def writebackFMove_128to64(binary):
    execFMOVE_general(binary,'1','10','01','110')

def execFMOVE_general(binary,sf,typeBits,rmode,opcode):
    destRegister = utilFunc.getRegKeyByStringKey(binary[27:32])

    if(opcode[2] == '1'):
        utilFunc.setRegValueSIMDFP(destRegister, mem.writeBackBuffer[0])
        armdebug.floatRFActivityCounter += 1
        mem.regFloatObsolete[destRegister] -= 1
    else:
        utilFunc.setRegValue(destRegister, mem.writeBackBuffer[0], '0')
        armdebug.intRFActivityCounter += 1
        mem.regObsolete[destRegister] -= 1
    
    const.FLAG_WRITEBACK_COMPLETED = True
    const.FLAG_WRITEBACK_EXECUTED = True

def writebackFMove_iSP(binary):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    utilFunc.setRegValueSIMDFP(rdKey, mem.writeBackBuffer[0])
    armdebug.floatRFActivityCounter += 1
    const.FLAG_WRITEBACK_COMPLETED = True
    const.FLAG_WRITEBACK_EXECUTED = True
    mem.regFloatObsolete[rdKey] -= 1

def writebackFMove_iDP(binary):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    utilFunc.setRegValueSIMDFP(rdKey, mem.writeBackBuffer[0])
    armdebug.floatRFActivityCounter += 1
    const.FLAG_WRITEBACK_COMPLETED = True
    const.FLAG_WRITEBACK_EXECUTED = True
    mem.regFloatObsolete[rdKey] -= 1

def writebackFMove_regSP(binary):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    utilFunc.setRegValueSIMDFP(rdKey, mem.writeBackBuffer[0])
    armdebug.floatRFActivityCounter += 1
    const.FLAG_WRITEBACK_COMPLETED = True
    const.FLAG_WRITEBACK_EXECUTED = True
    mem.regFloatObsolete[rdKey] -= 1

def writebackFMove_regDP(binary):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    utilFunc.setRegValueSIMDFP(rdKey, mem.writeBackBuffer[0])
    armdebug.floatRFActivityCounter += 1
    const.FLAG_WRITEBACK_COMPLETED = True
    const.FLAG_WRITEBACK_EXECUTED = True
    mem.regFloatObsolete[rdKey] -= 1