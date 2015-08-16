'''
Created on Aug 8, 2014

@author: harinder
'''
import const
import utilFunc
import mem
import armdebug

def opfetchMov_iwi32(binary):
    mov_imm(binary, "MOV w", '1', 32)
    
def opfetchMov_iwi64(binary):
    mov_imm(binary, "MOV x", '1', 64)
    
def opfetchMov_wi32(binary):
    mov_imm(binary, "MOV w", '0', 32)
    
def opfetchMov_wi64(binary):
    mov_imm(binary, "MOV x", '0', 64)
    
def mov_imm(binary, instr, inverted, N):  
    const.FLAG_OPFETCH_EXECUTED = True
    if(armdebug.pipelineStages[2] != '--------'):
        return
      
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    hw = binary[9:11]
    pos = utilFunc.uInt(hw+'0000')
    
    imm16 = binary[11:27]
    result = (imm16+'0'*pos).zfill(N)
    
    const.FLAG_OP_FETCHED = True
    mem.operand1Buffer = result
    mem.regObsolete[rdKey] += 1
    mem.regObsolete_last_modified_indices.append(rdKey)

def mov_reg(binary, N):
    const.FLAG_OPFETCH_EXECUTED = True
    if(armdebug.pipelineStages[2] != '--------'):
        return
    
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rmKey = utilFunc.getRegKeyByStringKey(binary[11:16])
    
    if(mem.regObsolete[rmKey] == 0):
        const.FLAG_OP_FETCHED = True
        rmVal = utilFunc.getRegValueByStringkey(binary[11:16],'0')
        armdebug.intRFActivityCounter += 1
    elif(const.FLAG_DATA_FORWARDING):
        forwardedValues = mem.findForwardedValues(rmKey)
        if(forwardedValues[0] != None):
            const.FLAG_OP_FETCHED = True
            rmVal = forwardedValues[0]
        else:
            return
    else:
        return
    
    mem.regObsolete[rdKey] += 1
    mem.regObsolete_last_modified_indices.append(rdKey)

    #rmVal = utilFunc.getRegValueByStringkey(binary[11:16], '0')
    
    if(N == 32):
        rmVal = rmVal[32:64]
        r = 'w'
    elif(N == 64):
        r = 'x'
     
    mem.operand1Buffer = rmVal.zfill(const.REG_SIZE)    

def opfetchMov_r32(binary):
    mov_reg(binary, 32)
    
def opfetchMov_r64(binary):
    mov_reg(binary, 64)
                           
                           
def mov_bmi(binary, N):
    const.FLAG_OPFETCH_EXECUTED = True
    if(armdebug.pipelineStages[2] != '--------'):
        return
    
    inst = 'MOV '
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    
    immr = binary[10:16]
    imms = binary[16:22]
    immN = binary[9]
    
    imm, temp = utilFunc.decodeBitMasks(immN, imms, immr, N)
    
    const.FLAG_OP_FETCHED = True
    mem.operand1Buffer = imm
    mem.regObsolete[rdKey] += 1
    mem.regObsolete_last_modified_indices.append(rdKey)
    
def opfetchMov_bmi32(binary):
    mov_bmi(binary, 32)
    
def opfetchMov_bmi64(binary):
    mov_bmi(binary, 64)

#------------------- floating point moves----------------

def opfetchFMove_SP(binary):
    const.FLAG_OPFETCH_EXECUTED = True
    if(armdebug.pipelineStages[2] != '--------'):
        return
    
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    
    const.FLAG_OP_FETCHED = True
    
    mem.regObsolete[rdKey] += 1
    mem.regObsolete_last_modified_indices.append(rdKey)


def opfetchFMove_DP(binary):
    const.FLAG_OPFETCH_EXECUTED = True
    if(armdebug.pipelineStages[2] != '--------'):
        return
    
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    
    const.FLAG_OP_FETCHED = True
    
    mem.regObsolete[rdKey] += 1
    mem.regObsolete_last_modified_indices.append(rdKey)
