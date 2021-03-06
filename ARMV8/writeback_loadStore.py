'''
Created on Aug 8, 2014

@author: harinder
'''
import const
import utilFunc
import mem
import armdebug

def helper_l(binary, instr):
    rtKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    
    utilFunc.setRegValue(rtKey, mem.writeBackBuffer[0], '0')
    armdebug.intRFActivityCounter += 1
    mem.regObsolete[rtKey] -= 1
    const.FLAG_WRITEBACK_COMPLETED = True
    const.FLAG_WRITEBACK_EXECUTED = True
    

#---Load Register (Literal)---
def writebackLDR_l32(binary):    
    helper_l(binary, 'LDR w')

def writebackLDR_l64(binary):
    helper_l(binary, 'LDR x')
    
def writebackLDRSW_l(binary):
    helper_l(binary, 'LDRSW x')
    
 

def helper_rp_posti(binary, instr):
    helper_rp(True, True, binary, instr)
    
def helper_rp_prei(binary, instr):
    helper_rp(True, False, binary, instr)
    
def helper_rp_offset(binary, instr):
    helper_rp(False, False, binary, instr)
    
def helper_rp(wback, postIndex, binary, instr):
    const.FLAG_WRITEBACK_EXECUTED = True    
    if(const.FLAG_WRITEBACK_COMPLETED == False and const.WRITEBACK_COUNTER == 0):
        if(binary[9] == '1'):
            const.WRITEBACK_COUNTER = 2
        else:
            const.WRITEBACK_COUNTER = 1
    
    if(const.WRITEBACK_COUNTER != 0):
        const.WRITEBACK_COUNTER -= 1
        
    if(const.WRITEBACK_COUNTER == 0):
        const.FLAG_WRITEBACK_COMPLETED = True
    
    rtKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    rt2Key = utilFunc.getRegKeyByStringKey(binary[17:22])
     
    l = binary[9]     
     
    if(l == '1'):
        memOp = const.MEM_OP_LOAD
    else:
        memOp = const.MEM_OP_STORE
        
    if(memOp == const.MEM_OP_LOAD):
        if(const.WRITEBACK_COUNTER == 1):
            utilFunc.setRegValue(rtKey, mem.writeBackBuffer[0], '0')
            armdebug.intRFActivityCounter += 1
            mem.regObsolete[rtKey] -= 1
        if(const.WRITEBACK_COUNTER == 0):
            utilFunc.setRegValue(rt2Key, mem.writeBackBuffer[1], '0')
            armdebug.intRFActivityCounter += 1
            mem.regObsolete[rt2Key] -= 1
    
    if(const.WRITEBACK_COUNTER == 0): 
        if(wback):                  
            utilFunc.setRegValue(rnKey, mem.writeBackBuffer[2], '1')
            armdebug.intRFActivityCounter += 1
            mem.regObsolete[rnKey] -= 1
    
    #const.FLAG_WRITEBACK_EXECUTED = True
    
    
#---Load/Store Register-Pair (Post-Indexed)---    
def writebackSTP_rp_posti_32(binary):
    helper_rp_posti(binary, 'STP')
    
def writebackLDP_rp_posti_32(binary):
    helper_rp_posti(binary, 'LDP')
    
def writebackSTP_rp_posti_64(binary):
    helper_rp_posti(binary, 'STP')
    
def writebackLDP_rp_posti_64(binary):
    helper_rp_posti(binary, 'LDP')
     
#---Load/Store Register-Pair (Post-Indexed)---    
def writebackSTP_rp_prei_32(binary):
    helper_rp_prei(binary, 'STP')
    
def writebackLDP_rp_prei_32(binary):
    helper_rp_prei(binary, 'LDP')
    
def writebackSTP_rp_prei_64(binary):
    helper_rp_prei(binary, 'STP')
    
def writebackLDP_rp_prei_64(binary):
    helper_rp_prei(binary, 'LDP')


#---Load/Store Register-Pair (Post-Indexed)---    
def writebackSTP_rp_offset_32(binary):
    helper_rp_offset(binary, 'LDP')
    
def writebackLDP_rp_offset_32(binary):
    helper_rp_offset(binary, 'LDP')
    
def writebackSTP_rp_offset_64(binary):
    helper_rp_offset(binary, 'STP')
    
def writebackLDP_rp_offset_64(binary):
    helper_rp_offset(binary, 'LDP')


    
#---Load/Store Register (Post-Indexed Immediate)---    
def writebackSTR_reg_posti_32(binary):
    helper_reg_posti(binary, 'STR w')
    
def writebackLDR_reg_posti_32(binary):
    helper_reg_posti(binary, 'LDR w')
    
def writebackLDRSW_reg_posti(binary):
    helper_reg_posti(binary, 'LDRSW x')
    
def writebackSTR_reg_posti_64(binary):
    helper_reg_posti(binary, 'STR x')

def writebackLDR_reg_posti_64(binary):
    helper_reg_posti(binary, 'LDR x')

def writebackLDRB_reg_posti(binary):
    helper_reg_posti(binary, 'LDRB w')

def writebackLDRH_reg_posti(binary):
    helper_reg_posti(binary, 'LDRH w')

def writebackLDRSB_reg_posti_32(binary):
    helper_reg_posti(binary, 'LDRSB w')

def writebackLDRSB_reg_posti_64(binary):
    helper_reg_posti(binary, 'LDRSB x')


#---Load/Store Register (Pre-Indexed Immediate)---    
def writebackSTR_reg_prei_32(binary):
    helper_reg_prei(binary, 'STR w')
    
def writebackLDR_reg_prei_32(binary):
    helper_reg_prei(binary, 'LDR w')
    
def writebackLDRSW_reg_prei(binary):
    helper_reg_prei(binary, 'LDRS x')
    
def writebackSTR_reg_prei_64(binary):
    helper_reg_prei(binary, 'STR x')

def writebackLDR_reg_prei_64(binary):
    helper_reg_prei(binary, 'LDR x')

def writebackLDRB_reg_prei(binary):
    helper_reg_prei(binary, 'LDRB w')

def writebackLDRH_reg_prei(binary):
    helper_reg_prei(binary, 'LDRH w')

def writebackLDRSB_reg_prei_32(binary):
    helper_reg_prei(binary, 'LDRSB w')

def writebackLDRSB_reg_prei_64(binary):
    helper_reg_prei(binary, 'LDRSB x')


#---Load/Store Register (Unsigned Offset)---    
def writebackSTR_reg_unsignedOffset_32(binary):
    helper_reg_unsignedOffset(binary, 'STR w')
    
def writebackLDR_reg_unsignedOffset_32(binary):
    helper_reg_unsignedOffset(binary, 'LDR w')
    
def writebackLDRSW_reg_unsignedOffset(binary):
    helper_reg_unsignedOffset(binary, 'LDRSW x')
    
def writebackSTR_reg_unsignedOffset_64(binary):
    helper_reg_unsignedOffset(binary, 'STR x')

def writebackLDR_reg_unsignedOffset_64(binary):
    helper_reg_unsignedOffset(binary, 'LDR x')

def writebackLDRB_reg_unsignedOffset(binary):
    helper_reg_unsignedOffset(binary, 'LDRB w')

def writebackLDRH_reg_unsignedOffset(binary):
    helper_reg_unsignedOffset(binary, 'LDRH w')

def writebackLDRSB_reg_unsignedOffset_32(binary):
    helper_reg_unsignedOffset(binary, 'LDRSB w')

def writebackLDRSB_reg_unsignedOffset_64(binary):
    helper_reg_unsignedOffset(binary, 'LDRSB x')



#---Load/Store Register (Register offset)---    
def writebackSTR_reg_offset_32(binary):
    helper_reg(binary, 'STR w')
    
def writebackLDR_reg_offset_32(binary):
    helper_reg(binary, 'LDR w')
    
def writebackLDRSW_reg_offset(binary):
    helper_reg(binary, 'LDRSW x')
    
def writebackSTR_reg_offset_64(binary):
    helper_reg(binary, 'STR x')

def writebackLDR_reg_offset_64(binary):
    helper_reg(binary, 'LDR x')

def writebackLDRB_reg_offset(binary):
    helper_reg(binary, 'LDRB w')

def writebackLDRH_reg_offset(binary):
    helper_reg(binary, 'LDRH w')

def writebackLDRSB_reg_offset_32(binary):
    helper_reg(binary, 'LDRSB w')

def writebackLDRSB_reg_offset_64(binary):
    helper_reg(binary, 'LDRSB X')
    

    
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
        utilFunc.setRegValue(rtKey, mem.writeBackBuffer[0], '0')
        armdebug.intRFActivityCounter += 1
        mem.regObsolete[rtKey] -= 1
        
    if(wback):
        utilFunc.setRegValue(rnKey, mem.writeBackBuffer[2], '1')
        armdebug.intRFActivityCounter += 1
        mem.regObsolete[rnKey] -= 1
    
    const.FLAG_WRITEBACK_COMPLETED = True
    const.FLAG_WRITEBACK_EXECUTED = True
