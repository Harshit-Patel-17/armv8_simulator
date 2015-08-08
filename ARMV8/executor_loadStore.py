'''
Created on Aug 8, 2014

@author: harinder
'''
import const
import utilFunc
import armdebug
import mem

def helper_l(binary, instr):    
    mem.ALUResultBuffer = mem.operand1Buffer + mem.operand2Buffer
    const.FLAG_INST_EXECUTED = True

#---Load Register (Literal)---
def execLDR_l32(binary):    
    helper_l(binary, 'LDR w')

def execLDR_l64(binary):
    helper_l(binary, 'LDR x')
    
def execLDRSW_l(binary):
    helper_l(binary, 'LDRSW x')
    
 

def helper_rp_posti(binary, instr):
    helper_rp(True, True, binary, instr)
    
def helper_rp_prei(binary, instr):
    helper_rp(True, False, binary, instr)
    
def helper_rp_offset(binary, instr):
    helper_rp(False, False, binary, instr)
    
def helper_rp(wback, postIndex, binary, instr):     
    if not(postIndex):
        mem.ALUResultBuffer = mem.operand1Buffer + mem.operand2Buffer
    else:
        mem.ALUResultBuffer = mem.operand1Buffer
    const.FLAG_INST_EXECUTED = True
    
#---Load/Store Register-Pair (Post-Indexed)---    
def execSTP_rp_posti_32(binary):
    helper_rp_posti(binary, 'STP')
    
def execLDP_rp_posti_32(binary):
    helper_rp_posti(binary, 'LDP')
    
def execSTP_rp_posti_64(binary):
    helper_rp_posti(binary, 'STP')
    
def execLDP_rp_posti_64(binary):
    helper_rp_posti(binary, 'LDP')
     
#---Load/Store Register-Pair (Post-Indexed)---    
def execSTP_rp_prei_32(binary):
    helper_rp_prei(binary, 'STP')
    
def execLDP_rp_prei_32(binary):
    helper_rp_prei(binary, 'LDP')
    
def execSTP_rp_prei_64(binary):
    helper_rp_prei(binary, 'STP')
    
def execLDP_rp_prei_64(binary):
    helper_rp_prei(binary, 'LDP')


#---Load/Store Register-Pair (Post-Indexed)---    
def execSTP_rp_offset_32(binary):
    helper_rp_offset(binary, 'LDP')
    
def execLDP_rp_offset_32(binary):
    helper_rp_offset(binary, 'LDP')
    
def execSTP_rp_offset_64(binary):
    helper_rp_offset(binary, 'STP')
    
def execLDP_rp_offset_64(binary):
    helper_rp_offset(binary, 'LDP')


    
#---Load/Store Register (Post-Indexed Immediate)---    
def execSTR_reg_posti_32(binary):
    helper_reg_posti(binary, 'STR w')
    
def execLDR_reg_posti_32(binary):
    helper_reg_posti(binary, 'LDR w')
    
def execLDRSW_reg_posti(binary):
    helper_reg_posti(binary, 'LDRSW x')
    
def execSTR_reg_posti_64(binary):
    helper_reg_posti(binary, 'STR x')

def execLDR_reg_posti_64(binary):
    helper_reg_posti(binary, 'LDR x')

def execLDRB_reg_posti(binary):
    helper_reg_posti(binary, 'LDRB w')

def execLDRH_reg_posti(binary):
    helper_reg_posti(binary, 'LDRH w')

def execLDRSB_reg_posti_32(binary):
    helper_reg_posti(binary, 'LDRSB w')

def execLDRSB_reg_posti_64(binary):
    helper_reg_posti(binary, 'LDRSB x')


#---Load/Store Register (Pre-Indexed Immediate)---    
def execSTR_reg_prei_32(binary):
    helper_reg_prei(binary, 'STR w')
    
def execLDR_reg_prei_32(binary):
    helper_reg_prei(binary, 'LDR w')
    
def execLDRSW_reg_prei(binary):
    helper_reg_prei(binary, 'LDRS x')
    
def execSTR_reg_prei_64(binary):
    helper_reg_prei(binary, 'STR x')

def execLDR_reg_prei_64(binary):
    helper_reg_prei(binary, 'LDR x')

def execLDRB_reg_prei(binary):
    helper_reg_prei(binary, 'LDRB w')

def execLDRH_reg_prei(binary):
    helper_reg_prei(binary, 'LDRH w')

def execLDRSB_reg_prei_32(binary):
    helper_reg_prei(binary, 'LDRSB w')

def execLDRSB_reg_prei_64(binary):
    helper_reg_prei(binary, 'LDRSB x')


#---Load/Store Register (Unsigned Offset)---    
def execSTR_reg_unsignedOffset_32(binary):
    helper_reg_unsignedOffset(binary, 'STR w')
    
def execLDR_reg_unsignedOffset_32(binary):
    helper_reg_unsignedOffset(binary, 'LDR w')
    
def execLDRSW_reg_unsignedOffset(binary):
    helper_reg_unsignedOffset(binary, 'LDRSW x')
    
def execSTR_reg_unsignedOffset_64(binary):
    helper_reg_unsignedOffset(binary, 'STR x')

def execLDR_reg_unsignedOffset_64(binary):
    helper_reg_unsignedOffset(binary, 'LDR x')

def execLDRB_reg_unsignedOffset(binary):
    helper_reg_unsignedOffset(binary, 'LDRB w')

def execLDRH_reg_unsignedOffset(binary):
    helper_reg_unsignedOffset(binary, 'LDRH w')

def execLDRSB_reg_unsignedOffset_32(binary):
    helper_reg_unsignedOffset(binary, 'LDRSB w')

def execLDRSB_reg_unsignedOffset_64(binary):
    helper_reg_unsignedOffset(binary, 'LDRSB x')



#---Load/Store Register (Register offset)---    
def execSTR_reg_offset_32(binary):
    helper_reg(binary, 'STR w')
    
def execLDR_reg_offset_32(binary):
    helper_reg(binary, 'LDR w')
    
def execLDRSW_reg_offset(binary):
    helper_reg(binary, 'LDRSW x')
    
def execSTR_reg_offset_64(binary):
    helper_reg(binary, 'STR x')

def execLDR_reg_offset_64(binary):
    helper_reg(binary, 'LDR x')

def execLDRB_reg_offset(binary):
    helper_reg(binary, 'LDRB w')

def execLDRH_reg_offset(binary):
    helper_reg(binary, 'LDRH w')

def execLDRSB_reg_offset_32(binary):
    helper_reg(binary, 'LDRSB w')

def execLDRSB_reg_offset_64(binary):
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
    if not(postIndex):
        mem.ALUResultBuffer = mem.operand1Buffer + mem.operand2Buffer
    else:
        mem.ALUResultBuffer = mem.operand1Buffer
    const.FLAG_INST_EXECUTED = True