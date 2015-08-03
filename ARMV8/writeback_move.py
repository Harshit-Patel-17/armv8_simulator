'''
Created on Aug 8, 2014

@author: harinder
'''
import const
import utilFunc
import mem


def writebackMov_iwi32(binary):
    mov_imm(binary, "MOV w", '1', 32)
    
def writebackMov_iwi64(binary):
    mov_imm(binary, "MOV x", '1', 64)
    
def writebackMov_wi32(binary):
    mov_imm(binary, "MOV w", '0', 32)
    
def writebackMov_wi64(binary):
    mov_imm(binary, "MOV x", '0', 64)
    
def mov_imm(binary, instr, inverted, N):   
    ''' 
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    const.FLAG_OPFETCH_EXECUTED = True
    const.FLAG_OP_FETCHED = True

    hw = binary[9:11]
    pos = utilFunc.uInt(hw+'0000')
    
    imm16 = binary[11:27]
    result = (imm16+'0'*pos).zfill(N)
    if(inverted == '1'):
        result = utilFunc.negate(result)
    instr = instr + str(rdKey)+", #"+utilFunc.binaryToHexStr(result)
    utilFunc.finalize(rdKey, result.zfill(const.REG_SIZE), instr, '0')
    '''
    const.FLAG_WRITEBACK_EXECUTED = True

def mov_reg(binary, N):
    '''
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rmKey = utilFunc.getRegKeyByStringKey(binary[11:16])

    const.FLAG_OPFETCH_EXECUTED = True
    if(mem.regObsolete[rmKey] == True):
        return
    else:
        const.FLAG_OP_FETCHED = True

    rmVal = utilFunc.getRegValueByStringkey(binary[11:16], '0')
    if(N == 32):
        rmVal = rmVal[32:64]
        r = 'w'
    elif(N == 64):
        r = 'x'
    instr = "MOV "+r+str(rdKey)+", "+r+str(rmKey)
    utilFunc.finalize(rdKey, rmVal.zfill(const.REG_SIZE), instr, '0')
    '''
    const.FLAG_WRITEBACK_EXECUTED = True

def writebackMov_r32(binary):
    mov_reg(binary, 32)
    
def writebackMov_r64(binary):
    mov_reg(binary, 64)
                           
                           
def mov_bmi(binary, N):
    '''
    inst = 'MOV '
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    const.FLAG_OPFETCH_EXECUTED = True
    const.FLAG_OP_FETCHED = True
    
    if(N == 32):
        r = 'w'
    else:
        r = 'x'
    inst += r + str(rdKey)
    
    
    immr = binary[10:16]
    imms = binary[16:22]
    immN = binary[9]
    
    imm, temp = utilFunc.decodeBitMasks(immN, imms, immr, N)
    inst += ', #' + utilFunc.binaryToHexStr(imm)
    result = utilFunc.logical_or('0'*N,imm).zfill(const.REG_SIZE)
    utilFunc.finalize(rdKey, result, inst, '1')
    '''
    const.FLAG_WRITEBACK_EXECUTED = True
    
def writebackMov_bmi32(binary):
    mov_bmi(binary, 32)
    
def writebackMov_bmi64(binary):
    mov_bmi(binary, 64)
