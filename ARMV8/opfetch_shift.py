'''
@author: harinder
'''


import utilFunc
import mem
import const
import armdebug

# Helper function
def getFields_r(binary):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    rmKey = utilFunc.getRegKeyByStringKey(binary[11:16])
    rnVal = utilFunc.getRegValueByStringkey(binary[22:27], '0')
    rmVal = utilFunc.getRegValueByStringkey(binary[11:16], '0')
    return rdKey, rnKey, rmKey, rnVal, rmVal


def opfetchAsr_r32(binary):
    const.FLAG_OPFETCH_EXECUTED = True
    if(armdebug.pipelineStages[2] != '--------'):
        return
    
    rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)
    if(mem.regObsolete[rnKey] == 0 and mem.regObsolete[rmKey] == 0):
        const.FLAG_OP_FETCHED = True
        mem.operand1Buffer = rnVal
        mem.operand2Buffer = rmVal
        armdebug.intRFActivityCounter += 2
    elif(const.FLAG_DATA_FORWARDING):
        forwardedValues = mem.findForwardedValues(rnKey, rmKey)
        if(forwardedValues[0] == None and mem.regObsolete[rnKey] != 0):
            return
        if(forwardedValues[1] == None and mem.regObsolete[rmKey] != 0):
            return
        const.FLAG_OP_FETCHED = True
        mem.operand1Buffer = rnVal
        mem.operand2Buffer = rmVal
        if(forwardedValues[0] != None):
            mem.operand1Buffer = forwardedValues[0]
        if(forwardedValues[1] != None):
            mem.operand2Buffer = forwardedValues[1]
        if(None in forwardedValues):
            armdebug.intRFActivityCounter += 1
    else:
        return
    
    mem.regObsolete[rdKey] += 1
    mem.regObsolete_last_modified_indices.append(rdKey)
                       
def opfetchLsl_r32(binary):
    const.FLAG_OPFETCH_EXECUTED = True
    if(armdebug.pipelineStages[2] != '--------'):
        return
    
    rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)
    if(mem.regObsolete[rnKey] == 0 and mem.regObsolete[rmKey] == 0):
        const.FLAG_OP_FETCHED = True
        mem.operand1Buffer = rnVal
        mem.operand2Buffer = rmVal
        armdebug.intRFActivityCounter += 2
    elif(const.FLAG_DATA_FORWARDING):
        forwardedValues = mem.findForwardedValues(rnKey, rmKey)
        if(forwardedValues[0] == None and mem.regObsolete[rnKey] != 0):
            return
        if(forwardedValues[1] == None and mem.regObsolete[rmKey] != 0):
            return
        const.FLAG_OP_FETCHED = True
        mem.operand1Buffer = rnVal
        mem.operand2Buffer = rmVal
        if(forwardedValues[0] != None):
            mem.operand1Buffer = forwardedValues[0]
        if(forwardedValues[1] != None):
            mem.operand2Buffer = forwardedValues[1]
        if(None in forwardedValues):
            armdebug.intRFActivityCounter += 1
    else:
        return
    
    mem.regObsolete[rdKey] += 1
    mem.regObsolete_last_modified_indices.append(rdKey)
    
def opfetchLsr_r32(binary):
    const.FLAG_OPFETCH_EXECUTED = True
    if(armdebug.pipelineStages[2] != '--------'):
        return
    
    rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)
    if(mem.regObsolete[rnKey] == 0 and mem.regObsolete[rmKey] == 0):
        const.FLAG_OP_FETCHED = True
        mem.operand1Buffer = rnVal
        mem.operand2Buffer = rmVal
        armdebug.intRFActivityCounter += 2
    elif(const.FLAG_DATA_FORWARDING):
        forwardedValues = mem.findForwardedValues(rnKey, rmKey)
        if(forwardedValues[0] == None and mem.regObsolete[rnKey] != 0):
            return
        if(forwardedValues[1] == None and mem.regObsolete[rmKey] != 0):
            return
        const.FLAG_OP_FETCHED = True
        mem.operand1Buffer = rnVal
        mem.operand2Buffer = rmVal
        if(forwardedValues[0] != None):
            mem.operand1Buffer = forwardedValues[0]
        if(forwardedValues[1] != None):
            mem.operand2Buffer = forwardedValues[1]
        if(None in forwardedValues):
            armdebug.intRFActivityCounter += 1
    else:
        return
    
    mem.regObsolete[rdKey] += 1
    mem.regObsolete_last_modified_indices.append(rdKey)
    
def opfetchAsr_r64(binary):
    const.FLAG_OPFETCH_EXECUTED = True
    if(armdebug.pipelineStages[2] != '--------'):
        return
    
    rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)
    if(mem.regObsolete[rnKey] == 0 and mem.regObsolete[rmKey] == 0):
        const.FLAG_OP_FETCHED = True
        mem.operand1Buffer = rnVal
        mem.operand2Buffer = rmVal
        armdebug.intRFActivityCounter += 2
    elif(const.FLAG_DATA_FORWARDING):
        forwardedValues = mem.findForwardedValues(rnKey, rmKey)
        if(forwardedValues[0] == None and mem.regObsolete[rnKey] != 0):
            return
        if(forwardedValues[1] == None and mem.regObsolete[rmKey] != 0):
            return
        const.FLAG_OP_FETCHED = True
        mem.operand1Buffer = rnVal
        mem.operand2Buffer = rmVal
        if(forwardedValues[0] != None):
            mem.operand1Buffer = forwardedValues[0]
        if(forwardedValues[1] != None):
            mem.operand2Buffer = forwardedValues[1]
        if(None in forwardedValues):
            armdebug.intRFActivityCounter += 1
    else:
        return
    
    mem.regObsolete[rdKey] += 1
    mem.regObsolete_last_modified_indices.append(rdKey)
                       
def opfetchLsl_r64(binary):
    const.FLAG_OPFETCH_EXECUTED = True
    if(armdebug.pipelineStages[2] != '--------'):
        return
    
    rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)
    if(mem.regObsolete[rnKey] == 0 and mem.regObsolete[rmKey] == 0):
        const.FLAG_OP_FETCHED = True
        mem.operand1Buffer = rnVal
        mem.operand2Buffer = rmVal
        armdebug.intRFActivityCounter += 2
    elif(const.FLAG_DATA_FORWARDING):
        forwardedValues = mem.findForwardedValues(rnKey, rmKey)
        if(forwardedValues[0] == None and mem.regObsolete[rnKey] != 0):
            return
        if(forwardedValues[1] == None and mem.regObsolete[rmKey] != 0):
            return
        const.FLAG_OP_FETCHED = True
        mem.operand1Buffer = rnVal
        mem.operand2Buffer = rmVal
        if(forwardedValues[0] != None):
            mem.operand1Buffer = forwardedValues[0]
        if(forwardedValues[1] != None):
            mem.operand2Buffer = forwardedValues[1]
        if(None in forwardedValues):
            armdebug.intRFActivityCounter += 1
    else:
        return
    
    mem.regObsolete[rdKey] += 1
    mem.regObsolete_last_modified_indices.append(rdKey)
    
def opfetchLsr_r64(binary):
    const.FLAG_OPFETCH_EXECUTED = True
    if(armdebug.pipelineStages[2] != '--------'):
        return
    
    rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)
    if(mem.regObsolete[rnKey] == 0 and mem.regObsolete[rmKey] == 0):
        const.FLAG_OP_FETCHED = True
        mem.operand1Buffer = rnVal
        mem.operand2Buffer = rmVal
        armdebug.intRFActivityCounter += 2
    elif(const.FLAG_DATA_FORWARDING):
        forwardedValues = mem.findForwardedValues(rnKey, rmKey)
        if(forwardedValues[0] == None and mem.regObsolete[rnKey] != 0):
            return
        if(forwardedValues[1] == None and mem.regObsolete[rmKey] != 0):
            return
        const.FLAG_OP_FETCHED = True
        mem.operand1Buffer = rnVal
        mem.operand2Buffer = rmVal
        if(forwardedValues[0] != None):
            mem.operand1Buffer = forwardedValues[0]
        if(forwardedValues[1] != None):
            mem.operand2Buffer = forwardedValues[1]
        if(None in forwardedValues):
            armdebug.intRFActivityCounter += 1
    else:
        return
    
    mem.regObsolete[rdKey] += 1
    mem.regObsolete_last_modified_indices.append(rdKey)

# Immediate operations
def opfetchAsr_i32(binary):
    const.FLAG_OPFETCH_EXECUTED = True
    if(armdebug.pipelineStages[2] != '--------'):
        return
        
    rdKey, rnKey, rnVal, immr, imms = getFields_i(binary)
    if(mem.regObsolete[rnKey] == 0):
        const.FLAG_OP_FETCHED = True
        mem.operand1Buffer = rnVal
        mem.operand2Buffer = immr
        armdebug.intRFActivityCounter += 1
    elif(const.FLAG_DATA_FORWARDING):
        forwardedValues = mem.findForwardedValues(rnKey)
        if(forwardedValues[0] != None):
            const.FLAG_OP_FETCHED = True
            mem.operand1Buffer = forwardedValues[0]
            mem.operand2Buffer = immr
        else:
            return
    else:
        return
    
    mem.regObsolete[rdKey] += 1
    mem.regObsolete_last_modified_indices.append(rdKey)
    
def opfetchAsr_i64(binary):
    const.FLAG_OPFETCH_EXECUTED = True
    if(armdebug.pipelineStages[2] != '--------'):
        return
    
    rdKey, rnKey, rnVal, immr, imms = getFields_i(binary)
    if(mem.regObsolete[rnKey] == 0):
        const.FLAG_OP_FETCHED = True
        mem.operand1Buffer = rnVal
        mem.operand2Buffer = immr
        armdebug.intRFActivityCounter += 1
    elif(const.FLAG_DATA_FORWARDING):
        forwardedValues = mem.findForwardedValues(rnKey)
        if(forwardedValues[0] != None):
            const.FLAG_OP_FETCHED = True
            mem.operand1Buffer = forwardedValues[0]
            mem.operand2Buffer = immr
        else:
            return
    else:
        return
    
    mem.regObsolete[rdKey] += 1
    mem.regObsolete_last_modified_indices.append(rdKey)
                       
def opfetchLslLsr_i32(binary):
    const.FLAG_OPFETCH_EXECUTED = True
    if(armdebug.pipelineStages[2] != '--------'):
        return
    
    rdKey, rnKey, rnVal, immr, imms = getFields_i(binary)
    if(mem.regObsolete[rnKey] == 0):
        const.FLAG_OP_FETCHED = True
        mem.operand1Buffer = rnVal
        mem.operand2Buffer = immr
        armdebug.intRFActivityCounter += 1
    elif(const.FLAG_DATA_FORWARDING):
        forwardedValues = mem.findForwardedValues(rnKey)
        if(forwardedValues[0] != None):
            const.FLAG_OP_FETCHED = True
            mem.operand1Buffer = forwardedValues[0]
            mem.operand2Buffer = immr
        else:
            return
    else:
        return
    
    mem.regObsolete[rdKey] += 1
    mem.regObsolete_last_modified_indices.append(rdKey)
    
def opfetchLslLsr_i64(binary):
    const.FLAG_OPFETCH_EXECUTED = True
    if(armdebug.pipelineStages[2] != '--------'):
        return
    
    rdKey, rnKey, rnVal, immr, imms = getFields_i(binary)
    if(mem.regObsolete[rnKey] == 0):
        const.FLAG_OP_FETCHED = True
        mem.operand1Buffer = rnVal
        mem.operand2Buffer = immr
        armdebug.intRFActivityCounter += 1
    elif(const.FLAG_DATA_FORWARDING):
        forwardedValues = mem.findForwardedValues(rnKey)
        if(forwardedValues[0] != None):
            const.FLAG_OP_FETCHED = True
            mem.operand1Buffer = forwardedValues[0]
            mem.operand2Buffer = immr
        else:
            return
    else:
        return
    
    mem.regObsolete[rdKey] += 1
    mem.regObsolete_last_modified_indices.append(rdKey)

# Helper function
def getFields_i(binary):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    immr = binary[10:16]
    imms = binary[16:22]
    rnVal = utilFunc.getRegValueByStringkey(binary[22:27], '0')
    return rdKey, rnKey, rnVal, immr, imms
