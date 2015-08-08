'''
Created on Aug 8, 2014

@author: harinder
'''
import const
import utilFunc
import armdebug
import mem

def helper_l(binary, instr):
    rtKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    opc = binary[0:2]
    signed = False
    
    if(opc == '00'):
        size = 4
    elif(opc == '01'):
        size = 8
    elif(opc == '10'):
        size = 4
        signed = True
        
    dataSize = size * 8
    
    data = utilFunc.fetchFromMemory(mem.ALUResultBuffer, dataSize)
    
    const.FLAG_MEMACCESS_EXECUTED = True
    
    if(data == const.TRAP):
            print "HEY!!! There seems to be a problem - memory location can not be accessed"
            print "Moving ahead without executing the instruction"
            armdebug.pipelineStages[3] = '--------'
            return
    
    if(signed):
        data = utilFunc.signExtend(data, 64)
    mem.writeBackBuffer[0] = data.zfill(64)
    

#---Load Register (Literal)---
def memaccessLDR_l32(binary):    
    helper_l(binary, 'LDR w')

def memaccessLDR_l64(binary):
    helper_l(binary, 'LDR x')
    
def memaccessLDRSW_l(binary):
    helper_l(binary, 'LDRSW x')
    
 

def helper_rp_posti(binary, instr):
    helper_rp(True, True, binary, instr)
    
def helper_rp_prei(binary, instr):
    helper_rp(True, False, binary, instr)
    
def helper_rp_offset(binary, instr):
    helper_rp(False, False, binary, instr)
    
def helper_rp(wback, postIndex, binary, instr):
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

    signed = (opc[1] != '0')
    scale = 2 + utilFunc.uInt(opc[0])
     
    dataSize = 8 << scale
    offset = utilFunc.lsl(utilFunc.signExtend(imm7, 64), scale)
    offset = utilFunc.sInt(offset, 64)
     
    dbytes = dataSize / 8;
    
    const.FLAG_MEMACCESS_EXECUTED = True
     
    if(memOp == const.MEM_OP_STORE):
        data1 = utilFunc.getRegValueByStringkey(binary[27:32], '0')
        data2 = utilFunc.getRegValueByStringkey(binary[17:22], '0')  
        utilFunc.storeToMemory(data1, mem.ALUResultBuffer, dataSize)
        utilFunc.storeToMemory(data2, mem.ALUResultBuffer + dbytes, dataSize)
             
    elif(memOp == const.MEM_OP_LOAD):
        data1 = utilFunc.fetchFromMemory(mem.ALUResultBuffer, dataSize)
        data2 = utilFunc.fetchFromMemory(mem.ALUResultBuffer + dbytes, dataSize)
        
        if(data1 == const.TRAP or data2 == const.TRAP):
            print "HEY!!! There seems to be a problem - memory location can not be accessed"
            print "Moving ahead without executing the instruction"
            armdebug.pipelineStages[3] = '--------'
            return
        
        if(signed):
            data1 = utilFunc.signExtend(data1, 64)
            data2 = utilFunc.signExtend(data2, 64)

        mem.writeBackBuffer[0] = data1.zfill(64)
        mem.writeBackBuffer[1] = data2.zfill(64)     
     
    if(wback):       
        if postIndex:
            mem.ALUResultBuffer = mem.ALUResultBuffer + offset
        mem.writeBackBuffer[2] = utilFunc.intToBinary(mem.ALUResultBuffer, 64)            
    
    
#---Load/Store Register-Pair (Post-Indexed)---    
def memaccessSTP_rp_posti_32(binary):
    helper_rp_posti(binary, 'STP')
    
def memaccessLDP_rp_posti_32(binary):
    helper_rp_posti(binary, 'LDP')
    
def memaccessSTP_rp_posti_64(binary):
    helper_rp_posti(binary, 'STP')
    
def memaccessLDP_rp_posti_64(binary):
    helper_rp_posti(binary, 'LDP')
     
#---Load/Store Register-Pair (Post-Indexed)---    
def memaccessSTP_rp_prei_32(binary):
    helper_rp_prei(binary, 'STP')
    
def memaccessLDP_rp_prei_32(binary):
    helper_rp_prei(binary, 'LDP')
    
def memaccessSTP_rp_prei_64(binary):
    helper_rp_prei(binary, 'STP')
    
def memaccessLDP_rp_prei_64(binary):
    helper_rp_prei(binary, 'LDP')


#---Load/Store Register-Pair (Post-Indexed)---    
def memaccessSTP_rp_offset_32(binary):
    helper_rp_offset(binary, 'LDP')
    
def memaccessLDP_rp_offset_32(binary):
    helper_rp_offset(binary, 'LDP')
    
def memaccessSTP_rp_offset_64(binary):
    helper_rp_offset(binary, 'STP')
    
def memaccessLDP_rp_offset_64(binary):
    helper_rp_offset(binary, 'LDP')


    
#---Load/Store Register (Post-Indexed Immediate)---    
def memaccessSTR_reg_posti_32(binary):
    helper_reg_posti(binary, 'STR w')
    
def memaccessLDR_reg_posti_32(binary):
    helper_reg_posti(binary, 'LDR w')
    
def memaccessLDRSW_reg_posti(binary):
    helper_reg_posti(binary, 'LDRSW x')
    
def memaccessSTR_reg_posti_64(binary):
    helper_reg_posti(binary, 'STR x')

def memaccessLDR_reg_posti_64(binary):
    helper_reg_posti(binary, 'LDR x')

def memaccessLDRB_reg_posti(binary):
    helper_reg_posti(binary, 'LDRB w')

def memaccessLDRH_reg_posti(binary):
    helper_reg_posti(binary, 'LDRH w')

def memaccessLDRSB_reg_posti_32(binary):
    helper_reg_posti(binary, 'LDRSB w')

def memaccessLDRSB_reg_posti_64(binary):
    helper_reg_posti(binary, 'LDRSB x')


#---Load/Store Register (Pre-Indexed Immediate)---    
def memaccessSTR_reg_prei_32(binary):
    helper_reg_prei(binary, 'STR w')
    
def memaccessLDR_reg_prei_32(binary):
    helper_reg_prei(binary, 'LDR w')
    
def memaccessLDRSW_reg_prei(binary):
    helper_reg_prei(binary, 'LDRS x')
    
def memaccessSTR_reg_prei_64(binary):
    helper_reg_prei(binary, 'STR x')

def memaccessLDR_reg_prei_64(binary):
    helper_reg_prei(binary, 'LDR x')

def memaccessLDRB_reg_prei(binary):
    helper_reg_prei(binary, 'LDRB w')

def memaccessLDRH_reg_prei(binary):
    helper_reg_prei(binary, 'LDRH w')

def memaccessLDRSB_reg_prei_32(binary):
    helper_reg_prei(binary, 'LDRSB w')

def memaccessLDRSB_reg_prei_64(binary):
    helper_reg_prei(binary, 'LDRSB x')


#---Load/Store Register (Unsigned Offset)---    
def memaccessSTR_reg_unsignedOffset_32(binary):
    helper_reg_unsignedOffset(binary, 'STR w')
    
def memaccessLDR_reg_unsignedOffset_32(binary):
    helper_reg_unsignedOffset(binary, 'LDR w')
    
def memaccessLDRSW_reg_unsignedOffset(binary):
    helper_reg_unsignedOffset(binary, 'LDRSW x')
    
def memaccessSTR_reg_unsignedOffset_64(binary):
    helper_reg_unsignedOffset(binary, 'STR x')

def memaccessLDR_reg_unsignedOffset_64(binary):
    helper_reg_unsignedOffset(binary, 'LDR x')

def memaccessLDRB_reg_unsignedOffset(binary):
    helper_reg_unsignedOffset(binary, 'LDRB w')

def memaccessLDRH_reg_unsignedOffset(binary):
    helper_reg_unsignedOffset(binary, 'LDRH w')

def memaccessLDRSB_reg_unsignedOffset_32(binary):
    helper_reg_unsignedOffset(binary, 'LDRSB w')

def memaccessLDRSB_reg_unsignedOffset_64(binary):
    helper_reg_unsignedOffset(binary, 'LDRSB x')



#---Load/Store Register (Register offset)---    
def memaccessSTR_reg_offset_32(binary):
    helper_reg(binary, 'STR w')
    
def memaccessLDR_reg_offset_32(binary):
    helper_reg(binary, 'LDR w')
    
def memaccessLDRSW_reg_offset(binary):
    helper_reg(binary, 'LDRSW x')
    
def memaccessSTR_reg_offset_64(binary):
    helper_reg(binary, 'STR x')

def memaccessLDR_reg_offset_64(binary):
    helper_reg(binary, 'LDR x')

def memaccessLDRB_reg_offset(binary):
    helper_reg(binary, 'LDRB w')

def memaccessLDRH_reg_offset(binary):
    helper_reg(binary, 'LDRH w')

def memaccessLDRSB_reg_offset_32(binary):
    helper_reg(binary, 'LDRSB w')

def memaccessLDRSB_reg_offset_64(binary):
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
    if(opc[0] == '0'):
        if(opc[1] == '1'):
            memOp = const.MEM_OP_LOAD
        else:
            memOp = const.MEM_OP_STORE
        if(size == '11'):
            regSize = 64
        else:
            regSize = 32
        signed = False
    else:
        if(size == '11'):
            memOp = const.MEM_OP_PREFETCH
        else:
            memOp = const.MEM_OP_LOAD
            if opc[1] == '1':
                regSize = 32
            else:
                regSize = 64
            signed = True
            
    dataSize = 8 << scale
    
    const.FLAG_MEMACCESS_EXECUTED = True
        
    if(memOp == const.MEM_OP_STORE):
        data = utilFunc.getRegValueByStringkey(binary[27:32], '0')
        utilFunc.storeToMemory(data, mem.ALUResultBuffer, dataSize)
            
    elif(memOp == const.MEM_OP_LOAD):
        data = utilFunc.fetchFromMemory(mem.ALUResultBuffer, dataSize)
        if(data == const.TRAP):
            print "HEY!!! There seems to be a problem - memory location can not be accessed"
            print "Moving ahead without executing the instruction"
            armdebug.pipelineStages[3] = '--------'            
            return   
        if(signed):
            data = utilFunc.signExtend(data, regSize)
        else:
            data = utilFunc.zeroExtend(data, regSize)
    
        mem.writeBackBuffer[0] = data.zfill(64)
        
    if(wback):
        if postIndex:
            mem.ALUResultBuffer = mem.ALUResultBuffer + offset
        mem.writeBackBuffer[2] = utilFunc.intToBinary(mem.ALUResultBuffer, 64)
