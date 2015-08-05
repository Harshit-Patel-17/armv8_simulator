'''
@author: harinder
'''


import utilFunc
import mem
import const


# Helper function
def getFields_r(binary):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    rmKey = utilFunc.getRegKeyByStringKey(binary[11:16])
    rnVal = utilFunc.getRegValueByStringkey(binary[22:27], '0')
    rmVal = utilFunc.getRegValueByStringkey(binary[11:16], '0')
    return rdKey, rnKey, rmKey, rnVal, rmVal


def opfetchAsr_r32(binary):
    rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)
    if(mem.regObsolete[rnKey] == False and mem.regObsolete[rmKey] == False):
        const.FLAG_OP_FETCHED = True
        mem.operand1Buffer = rnVal
        mem.operand2Buffer = rmVal
        mem.regObsolete[rdKey] = True
        mem.regObsolete_last_modified_indices.append(rdKey)
    const.FLAG_OPFETCH_EXECUTED = True
                       
def opfetchLsl_r32(binary):
    rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)
    if(mem.regObsolete[rnKey] == False and mem.regObsolete[rmKey] == False):
        const.FLAG_OP_FETCHED = True
        mem.operand1Buffer = rnVal
        mem.operand2Buffer = rmVal
        mem.regObsolete[rdKey] = True
        mem.regObsolete_last_modified_indices.append(rdKey)
    const.FLAG_OPFETCH_EXECUTED = True
    
def opfetchLsr_r32(binary):
    rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)
    if(mem.regObsolete[rnKey] == False and mem.regObsolete[rmKey] == False):
        const.FLAG_OP_FETCHED = True
        mem.operand1Buffer = rnVal
        mem.operand2Buffer = rmVal
        mem.regObsolete[rdKey] = True
        mem.regObsolete_last_modified_indices.append(rdKey)
    const.FLAG_OPFETCH_EXECUTED = True
    
def opfetchAsr_r64(binary):
    rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)
    if(mem.regObsolete[rnKey] == False and mem.regObsolete[rmKey] == False):
        const.FLAG_OP_FETCHED = True
        mem.operand1Buffer = rnVal
        mem.operand2Buffer = rmVal
        mem.regObsolete[rdKey] = True
        mem.regObsolete_last_modified_indices.append(rdKey)
    const.FLAG_OPFETCH_EXECUTED = True
                       
def opfetchLsl_r64(binary):
    rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)
    if(mem.regObsolete[rnKey] == False and mem.regObsolete[rmKey] == False):
        const.FLAG_OP_FETCHED = True
        mem.operand1Buffer = rnVal
        mem.operand2Buffer = rmVal
        mem.regObsolete[rdKey] = True
        mem.regObsolete_last_modified_indices.append(rdKey)
    const.FLAG_OPFETCH_EXECUTED = True
    
def opfetchLsr_r64(binary):
    rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)
    if(mem.regObsolete[rnKey] == False and mem.regObsolete[rmKey] == False):
        const.FLAG_OP_FETCHED = True
        mem.operand1Buffer = rnVal
        mem.operand2Buffer = rmVal
        mem.regObsolete[rdKey] = True
        mem.regObsolete_last_modified_indices.append(rdKey)
    const.FLAG_OPFETCH_EXECUTED = True

# Immediate operations
def opfetchAsr_i32(binary):    
    rdKey, rnKey, rnVal, immr, imms = getFields_i(binary)
    if(mem.regObsolete[rnKey] == False):
        const.FLAG_OP_FETCHED = True
        mem.operand1Buffer = rnVal
        mem.operand2Buffer = immr
        mem.regObsolete[rdKey] = True
        mem.regObsolete_last_modified_indices.append(rdKey)
    const.FLAG_OPFETCH_EXECUTED = True
    
def opfetchAsr_i64(binary):
    rdKey, rnKey, rnVal, immr, imms = getFields_i(binary)
    if(mem.regObsolete[rnKey] == False):
        const.FLAG_OP_FETCHED = True
        mem.operand1Buffer = rnVal
        mem.operand2Buffer = immr
        mem.regObsolete[rdKey] = True
        mem.regObsolete_last_modified_indices.append(rdKey)
    const.FLAG_OPFETCH_EXECUTED = True
                       
def opfetchLslLsr_i32(binary):
    rdKey, rnKey, rnVal, immr, imms = getFields_i(binary)
    if(mem.regObsolete[rnKey] == False):
        const.FLAG_OP_FETCHED = True
        mem.operand1Buffer = rnVal
        mem.operand2Buffer = immr
        mem.regObsolete[rdKey] = True
        mem.regObsolete_last_modified_indices.append(rdKey)
    const.FLAG_OPFETCH_EXECUTED = True
    
def opfetchLslLsr_i64(binary):
    rdKey, rnKey, rnVal, immr, imms = getFields_i(binary)
    if(mem.regObsolete[rnKey] == False):
        const.FLAG_OP_FETCHED = True
        mem.operand1Buffer = rnVal
        mem.operand2Buffer = immr
        mem.regObsolete[rdKey] = True
        mem.regObsolete_last_modified_indices.append(rdKey)
    const.FLAG_OPFETCH_EXECUTED = True

# Helper function
def getFields_i(binary):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    immr = binary[10:16]
    imms = binary[16:22]
    rnVal = utilFunc.getRegValueByStringkey(binary[22:27], '0')
    return rdKey, rnKey, rnVal, immr, imms
