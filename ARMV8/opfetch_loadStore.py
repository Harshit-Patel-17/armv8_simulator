'''
Created on Aug 8, 2014

@author: harinder
'''
import const
import utilFunc
import armdebug
import mem

def helper_l(binary, instr):
    const.FLAG_OPFETCH_EXECUTED = True
    if(armdebug.pipelineStages[2] != '--------'):
        return
    
    rtKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    imm19 = binary[8:27]
        
    offset = utilFunc.signExtend(imm19 + '00', 64)
    offset = utilFunc.sInt(offset, 64)
    
    const.FLAG_OP_FETCHED = True
    mem.operand1Buffer = armdebug.getPC() - 4
    mem.operand2Buffer = offset
    mem.regObsolete[rtKey] = True
    mem.regObsolete_last_modified_index = rtKey
    

#---Load Register (Literal)---
def opfetchLDR_l32(binary):    
    helper_l(binary, 'LDR w')

def opfetchLDR_l64(binary):
    helper_l(binary, 'LDR x')
    
def opfetchLDRSW_l(binary):
    helper_l(binary, 'LDRSW x')
    
 

def helper_rp_posti(binary, instr):
    helper_rp(True, True, binary, instr)
    
def helper_rp_prei(binary, instr):
    helper_rp(True, False, binary, instr)
    
def helper_rp_offset(binary, instr):
    helper_rp(False, False, binary, instr)
    
def helper_rp(wback, postIndex, binary, instr):
    const.FLAG_OPFETCH_EXECUTED = True
    #if(armdebug.pipelineStages[2] != '--------'):
    #    return
    
    rtKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    rt2Key = utilFunc.getRegKeyByStringKey(binary[17:22])
     
    imm7 = binary[10:17]
    l = binary[9]     
    opc = binary[0:2]
     
    if(l == '1'):
        memOp = const.MEM_OP_LOAD
    else:
        memOp = const.MEM_OP_STORE
        
    if(const.FLAG_OP_FETCHED == False and const.OPFETCH_COUNTER == 0):
        if(memOp == const.MEM_OP_STORE):
            const.OPFETCH_COUNTER = 2
    
    scale = 2 + utilFunc.uInt(opc[0])
     
    offset = utilFunc.lsl(utilFunc.signExtend(imm7, 64), scale)
    offset = utilFunc.sInt(offset, 64)
    
    if(memOp == const.MEM_OP_LOAD):
        if(mem.regObsolete[rnKey] == 0):
            armdebug.intRFActivityCounter += 1
            const.FLAG_OP_FETCHED = True
            if(armdebug.pipelineStages[2] != '--------'):
                    return
            address = utilFunc.getRegValueByStringkey(binary[22:27],'1')
        elif(const.FLAG_DATA_FORWARDING):
            forwardedValues = mem.findForwardedValues(rnKey)
            if(armdebug.pipelineStages[2] != '--------' or forwardedValues[0] == None):
                return
            const.FLAG_OP_FETCHED = True
            address = forwardedValues[0]
        else:
            return
        
        mem.regObsolete[rtKey] += 1
        mem.regObsolete_last_modified_indices.append(rtKey)
        mem.regObsolete[rt2Key] += 1
        mem.regObsolete_last_modified_indices.append(rt2Key)
    else:
        if(mem.regObsolete[rnKey] == 0 and mem.regObsolete[rtKey] == 0 and mem.regObsolete[rt2Key] == 0):
            if(const.OPFETCH_COUNTER != 0):
                armdebug.intRFActivityCounter += 1
                const.OPFETCH_COUNTER -= 1
                
            if(const.OPFETCH_COUNTER == 0):
                const.FLAG_OP_FETCHED = True
                if(armdebug.pipelineStages[2] != '--------'):
                    return
            else:
                return
            mem.IF_ID_dataBuffer = []
            mem.IF_ID_dataBuffer.append(utilFunc.getRegValueByStringkey(binary[27:32], '0'))
            mem.IF_ID_dataBuffer.append(utilFunc.getRegValueByStringkey(binary[17:22], '0'))
            address = utilFunc.getRegValueByStringkey(binary[22:27],'1')
        elif(const.FLAG_DATA_FORWARDING):
            forwardedValues = mem.findForwardedValues(rtKey, rt2Key, rnKey)
            if(forwardedValues[0] == None and mem.regObsolete[rtKey] != 0):
                return
            if(forwardedValues[0] == None and mem.regObsolete[rt2Key] != 0):
                return
            if(forwardedValues[1] == None and mem.regObsolete[rnKey] != 0):
                return
            const.FLAG_OP_FETCHED = True
            if(armdebug.pipelineStages[2] != '--------'):
                return
            data1 = utilFunc.getRegValueByStringkey(binary[27:32], '0')
            data2 = utilFunc.getRegValueByStringkey(binary[17:22], '0')
            address = utilFunc.getRegValueByStringkey(binary[22:27],'1')
            forwardedValues = mem.findForwardedValues(rtKey, rt2Key, rnKey)
            if(forwardedValues[0] != None):
                data1 = forwardedValues[0]
            if(forwardedValues[1] != None):
                data2 = forwardedValues[1]
            if(forwardedValues[2] != None):
                address = forwardedValues[2]
            if(None in forwardedValues):
                armdebug.intRFActivityCounter += 1
            mem.IF_ID_dataBuffer = []
            mem.IF_ID_dataBuffer.append(data1)
            mem.IF_ID_dataBuffer.append(data2)
        else:
            return
     
    if(wback):
        mem.regObsolete[rnKey] += 1
        mem.regObsolete_last_modified_indices.append(rnKey)
     
    #address = utilFunc.getRegValueByStringkey(binary[22:27], '1')
    address = utilFunc.uInt(address)
    
    mem.operand1Buffer = address
    mem.operand2Buffer = offset
    
#---Load/Store Register-Pair (Post-Indexed)---    
def opfetchSTP_rp_posti_32(binary):
    helper_rp_posti(binary, 'STP')
    
def opfetchLDP_rp_posti_32(binary):
    helper_rp_posti(binary, 'LDP')
    
def opfetchSTP_rp_posti_64(binary):
    helper_rp_posti(binary, 'STP')
    
def opfetchLDP_rp_posti_64(binary):
    helper_rp_posti(binary, 'LDP')
     
#---Load/Store Register-Pair (Post-Indexed)---    
def opfetchSTP_rp_prei_32(binary):
    helper_rp_prei(binary, 'STP')
    
def opfetchLDP_rp_prei_32(binary):
    helper_rp_prei(binary, 'LDP')
    
def opfetchSTP_rp_prei_64(binary):
    helper_rp_prei(binary, 'STP')
    
def opfetchLDP_rp_prei_64(binary):
    helper_rp_prei(binary, 'LDP')


#---Load/Store Register-Pair (Post-Indexed)---    
def opfetchSTP_rp_offset_32(binary):
    helper_rp_offset(binary, 'LDP')
    
def opfetchLDP_rp_offset_32(binary):
    helper_rp_offset(binary, 'LDP')
    
def opfetchSTP_rp_offset_64(binary):
    helper_rp_offset(binary, 'STP')
    
def opfetchLDP_rp_offset_64(binary):
    helper_rp_offset(binary, 'LDP')


    
#---Load/Store Register (Post-Indexed Immediate)---    
def opfetchSTR_reg_posti_32(binary):
    helper_reg_posti(binary, 'STR w')
    
def opfetchLDR_reg_posti_32(binary):
    helper_reg_posti(binary, 'LDR w')
    
def opfetchLDRSW_reg_posti(binary):
    helper_reg_posti(binary, 'LDRSW x')
    
def opfetchSTR_reg_posti_64(binary):
    helper_reg_posti(binary, 'STR x')

def opfetchLDR_reg_posti_64(binary):
    helper_reg_posti(binary, 'LDR x')

def opfetchLDRB_reg_posti(binary):
    helper_reg_posti(binary, 'LDRB w')

def opfetchLDRH_reg_posti(binary):
    helper_reg_posti(binary, 'LDRH w')

def opfetchLDRSB_reg_posti_32(binary):
    helper_reg_posti(binary, 'LDRSB w')

def opfetchLDRSB_reg_posti_64(binary):
    helper_reg_posti(binary, 'LDRSB x')


#---Load/Store Register (Pre-Indexed Immediate)---    
def opfetchSTR_reg_prei_32(binary):
    helper_reg_prei(binary, 'STR w')
    
def opfetchLDR_reg_prei_32(binary):
    helper_reg_prei(binary, 'LDR w')
    
def opfetchLDRSW_reg_prei(binary):
    helper_reg_prei(binary, 'LDRS x')
    
def opfetchSTR_reg_prei_64(binary):
    helper_reg_prei(binary, 'STR x')

def opfetchLDR_reg_prei_64(binary):
    helper_reg_prei(binary, 'LDR x')

def opfetchLDRB_reg_prei(binary):
    helper_reg_prei(binary, 'LDRB w')

def opfetchLDRH_reg_prei(binary):
    helper_reg_prei(binary, 'LDRH w')

def opfetchLDRSB_reg_prei_32(binary):
    helper_reg_prei(binary, 'LDRSB w')

def opfetchLDRSB_reg_prei_64(binary):
    helper_reg_prei(binary, 'LDRSB x')


#---Load/Store Register (Unsigned Offset)---    
def opfetchSTR_reg_unsignedOffset_32(binary):
    helper_reg_unsignedOffset(binary, 'STR w')
    
def opfetchLDR_reg_unsignedOffset_32(binary):
    helper_reg_unsignedOffset(binary, 'LDR w')
    
def opfetchLDRSW_reg_unsignedOffset(binary):
    helper_reg_unsignedOffset(binary, 'LDRSW x')
    
def opfetchSTR_reg_unsignedOffset_64(binary):
    helper_reg_unsignedOffset(binary, 'STR x')

def opfetchLDR_reg_unsignedOffset_64(binary):
    helper_reg_unsignedOffset(binary, 'LDR x')

def opfetchLDRB_reg_unsignedOffset(binary):
    helper_reg_unsignedOffset(binary, 'LDRB w')

def opfetchLDRH_reg_unsignedOffset(binary):
    helper_reg_unsignedOffset(binary, 'LDRH w')

def opfetchLDRSB_reg_unsignedOffset_32(binary):
    helper_reg_unsignedOffset(binary, 'LDRSB w')

def opfetchLDRSB_reg_unsignedOffset_64(binary):
    helper_reg_unsignedOffset(binary, 'LDRSB x')



#---Load/Store Register (Register offset)---    
def opfetchSTR_reg_offset_32(binary):
    helper_reg(binary, 'STR w')
    
def opfetchLDR_reg_offset_32(binary):
    helper_reg(binary, 'LDR w')
    
def opfetchLDRSW_reg_offset(binary):
    helper_reg(binary, 'LDRSW x')
    
def opfetchSTR_reg_offset_64(binary):
    helper_reg(binary, 'STR x')

def opfetchLDR_reg_offset_64(binary):
    helper_reg(binary, 'LDR x')

def opfetchLDRB_reg_offset(binary):
    helper_reg(binary, 'LDRB w')

def opfetchLDRH_reg_offset(binary):
    helper_reg(binary, 'LDRH w')

def opfetchLDRSB_reg_offset_32(binary):
    helper_reg(binary, 'LDRSB w')

def opfetchLDRSB_reg_offset_64(binary):
    helper_reg(binary, 'LDRSB x')
    

    
def helper_reg_posti(binary, instr):
    rtKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    imm9 = binary[11:20]
    opc = binary[8:10]
    size = binary[0:2]
    wback = True
    postIndex = True
    scale = utilFunc.uInt(size)
    offset = utilFunc.signExtend(imm9, 64)
    offset = utilFunc.sInt(offset, 64)
    instr += str(rtKey) + ", [x" + str(rnKey) + "], #" + str(offset) 
    helper_all(binary, opc, size, wback, postIndex, offset, rtKey, rnKey, scale, instr)

def helper_reg_prei(binary, instr):
    rtKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    imm9 = binary[11:20]
    opc = binary[8:10]
    size = binary[0:2]
    wback = True
    postIndex = False
    scale = utilFunc.uInt(size)
    offset = utilFunc.signExtend(imm9, 64)
    offset = utilFunc.sInt(offset, 64)
    instr += str(rtKey) + ", [x" + str(rnKey) + ", #" + str(offset) + "]!"
    helper_all(binary, opc, size, wback, postIndex, offset, rtKey, rnKey, scale, instr)

def helper_reg_unsignedOffset(binary, instr):
    rtKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    imm12 = binary[10:22]
    opc = binary[8:10]
    size = binary[0:2]
    wback = False
    postIndex = False
    scale = utilFunc.uInt(size)
    offset = utilFunc.lsl(utilFunc.zeroExtend(imm12, 64), scale)
    offset = utilFunc.sInt(offset, 64)
    instr += str(rtKey) + ", [x" + str(rnKey) + ", #" + str(offset) + "]"
    helper_all(binary, opc, size, wback, postIndex, offset, rtKey, rnKey, scale, instr)

def helper_reg(binary, instr):
    rtKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    rmKey = utilFunc.getRegKeyByStringKey(binary[11:16])
    
    rnVal = utilFunc.getRegValueByStringkey(binary[22:27], '1')
    rmVal = utilFunc.getRegValueByStringkey(binary[11:16], '0')
    s = binary[19]
    option = binary[16:19]
    opc = binary[8:10]
    size = binary[0:2]
    
    wback = False
    postIndex = False
    scale = utilFunc.uInt(size)
    if s == '1':
        shift = scale
    else:
        shift = 0
    
    if(option[1:3] == '10'):
        rmToPrint = 'w'
    elif(option[1:3] == '11'):
        rmToPrint = 'x'
        
    instr += str(rtKey) + ", [x" + str(rnKey) + ", " + rmToPrint + str(rmKey) + ", "     
    offset, instr = utilFunc.extendReg(rmVal, shift, option, instr, 64)
    offset = utilFunc.sInt(offset, 64)
    instr += ' #'
    if size == '10':
        if s == '0':
            instr += '0'
        else:
            instr += '2'
            
    if size == '11':
        if s == '0':
            instr += '0'
        else:
            instr += '3'
    instr += ']'
    
    helper_all(binary, opc, size, wback, postIndex, offset, rtKey, rnKey, scale, instr)    

    
def helper_all(binary, opc, size, wback, postIndex, offset, rtKey, rnKey, scale, instr):
    const.FLAG_OPFETCH_EXECUTED = True
    if(armdebug.pipelineStages[2] != '--------'):
        return
    
    if(opc[0] == '0'):
        if(opc[1] == '1'):
            memOp = const.MEM_OP_LOAD
        else:
            memOp = const.MEM_OP_STORE
    else:
        if(size == '11'):
            memOp = const.MEM_OP_PREFETCH
        else:
            memOp = const.MEM_OP_LOAD
    
    if(memOp == const.MEM_OP_LOAD):        
        if(mem.regObsolete[rnKey] == 0):
            const.FLAG_OP_FETCHED = True
            address = utilFunc.getRegValueByStringkey(binary[22:27],'1')
            armdebug.intRFActivityCounter += 1
        elif(const.FLAG_DATA_FORWARDING):
            forwardedValues = mem.findForwardedValues(rnKey)
            if(forwardedValues[0] != None):
                const.FLAG_OP_FETCHED = True
                address = forwardedValues[0]
            else:
                return
        else:
            return
        mem.regObsolete[rtKey] += 1
        mem.regObsolete_last_modified_indices.append(rtKey)
    else:
        if(mem.regObsolete[rnKey] == 0 and mem.regObsolete[rtKey] == 0):
            const.FLAG_OP_FETCHED = True
            data = utilFunc.getRegValueByStringkey(binary[27:32], '0')
            address = utilFunc.getRegValueByStringkey(binary[22:27],'1')
            armdebug.intRFActivityCounter += 1
        elif(const.FLAG_DATA_FORWARDING):
            forwardedValues = mem.findForwardedValues(rtKey, rnKey)
            if(forwardedValues[0] == None and mem.regObsolete[rtKey] != 0):
                return
            if(forwardedValues[1] == None and mem.regObsolete[rnKey] != 0):
                return
            const.FLAG_OP_FETCHED = True
            data = utilFunc.getRegValueByStringkey(binary[27:32], '0')
            address = utilFunc.getRegValueByStringkey(binary[22:27],'1')
            if(forwardedValues[0] != None):
                data = forwardedValues[0]
            if(forwardedValues[1] != None):
                address = forwardedValues[1]
            if(None in forwardedValues):
                armdebug.intRFActivityCounter += 1
            mem.IF_ID_dataBuffer = []
            mem.IF_ID_dataBuffer.append(data)
        else:
            return
    
    if(wback):
        mem.regObsolete[rnKey] += 1
        mem.regObsolete_last_modified_indices.append(rnKey)
    #address = utilFunc.getRegValueByStringkey(binary[22:27], '1')
    address = utilFunc.uInt(address)
    
    mem.operand1Buffer = address
    mem.operand2Buffer = offset