import utilFunc
import mem
import const


def writeback_i(binary, N, instr, sub_op, setFlags):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    '''
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    rnVal = utilFunc.getRegValueByStringkey(binary[22:27],'1')
    if(N == 32):
        rnVal = rnVal[32:64]
        r = 'w'
    elif(N == 64):
        r = 'x'
    imm12 = binary[10:22]
    shiftType = binary[8:10]
    instr += " " + r + str(rdKey) + ", " + r + str(rnKey) + ", #" + utilFunc.binaryToHexStr(imm12) + ", LSL"
    if shiftType == "00":
        imm12 = imm12.zfill(N)
        instr = instr + " #0"
    elif shiftType == "01":
        imm12 = (imm12 + '0' * 12).zfill(N)
        instr = instr + " #12"
    
    mem.regObsolete[rdKey] = True
    if(mem.regObsolete[rnKey] == False):
        const.FLAG_OP_FETCHED = True
        mem.operand1Buffer = rnVal
        mem.operand2Buffer = imm12
    const.FLAG_writeback_EXECUTED = True
    '''
    
    utilFunc.setRegValue(rdKey, mem.writeBackBuffer[0].zfill(const.REG_SIZE), mem.isSPWriteBackBuffer)
    const.FLAG_WRITEBACK_EXECUTED = True
    mem.regObsolete[rdKey] = False

def writebackAdd_i32(binary):
    return writeback_i(binary, 32, "ADD", '0', '0')

def writebackAdds_i32(binary):
    return writeback_i(binary, 32, "ADDS", '0', '1')
    
def writebackSub_i32(binary):
    return writeback_i(binary, 32, "SUB", '1', '0')
    
def writebackSubs_i32(binary):
    return writeback_i(binary, 32, "SUBS", '1', '1')
    
def writebackAdd_i64(binary):
    return writeback_i(binary, 64, "ADD", '0', '0')
    
def writebackAdds_i64(binary):
    return writeback_i(binary, 64, "ADDS", '0', '1') 
    
def writebackSub_i64(binary):
    return writeback_i(binary, 64, "SUB", '1', '0')
    
def writebackSubs_i64(binary): 
    return writeback_i(binary, 64, "SUBS", '1', '1')
    
# fetches the operand2 for shift register operations
def fetchOp2_sr(rmVal, shiftType, amt, instr):
    if shiftType == "00":   
        op2 = utilFunc.lsl(rmVal, amt)
        instr += 'LSL'
    elif shiftType == "01":
        op2 = utilFunc.lsr(rmVal, amt)
        instr += 'LSR'
    elif shiftType == "10":
        op2 = utilFunc.asr(rmVal, amt)
        instr += 'ASR'
    return op2, instr


    
def writeback_sr(binary, N, instr, sub_op, setFlags):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    '''
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    rmkey = utilFunc.getRegKeyByStringKey(binary[11:16])
    imm6 = binary[16:22]
    imm6Val = int(imm6, 2)
    
    rnVal = utilFunc.getRegValueByStringkey(binary[22:27], '0')
    rmVal = utilFunc.getRegValueByStringkey(binary[11:16], '0')
    if(N == 32):
        rnVal = rnVal[32:64]
        rmVal = rmVal[32:64]
        r = 'w'
    elif(N == 64):
        r = 'x'  
    shiftType = binary[8:10]
    instr += " " + r + str(rdKey) + ", " + r + str(rnKey) + ", " + r + str(rmkey) + ", "
    op2, instr = fetchOp2_sr(rmVal, shiftType, imm6Val, instr)
    instr += " #" + str(imm6Val)
    mem.regObsolete[rdKey] = True
    if(mem.regObsolete[rnKey] == False and mem.regObsolete[rmkey] == False):
        const.FLAG_OP_FETCHED = True
        mem.operand1Buffer = rnVal
        mem.operand2Buffer = op2
    const.FLAG_writeback_EXECUTED = True
    '''
    utilFunc.setRegValue(rdKey, mem.writeBackBuffer[0].zfill(const.REG_SIZE), '0')
    const.FLAG_WRITEBACK_EXECUTED = True
    mem.regObsolete[rdKey] = False
    
def writebackAdd_sr32(binary):
    return writeback_sr(binary, 32, "ADD", '0', '0')
    
def writebackAdds_sr32(binary):
    return writeback_sr(binary, 32, "ADDS", '0', '1')
    
def writebackSub_sr32(binary):
    return writeback_sr(binary, 32, "SUB", '1', '0')
    
def writebackSubs_sr32(binary):
    return writeback_sr(binary, 32, "SUBS", '1', '1')
    
def writebackAdd_sr64(binary):
    return writeback_sr(binary, 64, "ADD", '0', '0')
    
def writebackAdds_sr64(binary):
    return writeback_sr(binary, 64, "ADDS", '0', '1')
    
def writebackSub_sr64(binary):
    return writeback_sr(binary, 64, "SUB", '1', '0')
    
def writebackSubs_sr64(binary): 
    return writeback_sr(binary, 64, "SUBS", '1', '1')
    
    
def writeback_er(binary, N, instr, sub_op, setFlags):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    '''
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    rmkey = utilFunc.getRegKeyByStringKey(binary[11:16])
    option = binary[16:19]
    imm3 = binary[19:22]
    shift = int(imm3, 2)
    
    rnVal = utilFunc.getRegValueByStringkey(binary[22:27], '1')
    rmVal = utilFunc.getRegValueByStringkey(binary[11:16], '0')
    if(N == 32):
        rnVal = rnVal[32:64]
        rmVal = rmVal[32:64]
        r = 'w'
    elif(N == 64):
        r = 'x'
        if(option[1:3] == '11'):
            rmToPrint = 'x'
        else:
            rmToPrint = 'w'
    instr += " " + r + str(rdKey) + ", " + r + str(rnKey) + ", " + rmToPrint + str(rmkey) + ", "
    op2, instr = utilFunc.extendReg(rmVal, shift, option, instr, N)
    instr += " #" + str(shift)
    
    mem.regObsolete[rdKey] = True
    if(mem.regObsolete[rnKey] == False and mem.regObsolete[rmkey] == False):
        const.FLAG_OP_FETCHED = True
        mem.operand1Buffer = rnVal
        mem.operand2Buffer = op2
    const.FLAG_writeback_EXECUTED = True
    '''
    utilFunc.setRegValue(rdKey, mem.writeBackBuffer[0].zfill(const.REG_SIZE), mem.isSPWriteBackBuffer)
    const.FLAG_WRITEBACK_EXECUTED = True
    mem.regObsolete[rdKey] = False
       

# Add Subtract - Extended register
def writebackAdd_er32(binary):
    writeback_er(binary, 32, "ADD", '0', '0')
    
def writebackAdds_er32(binary):
    writeback_er(binary, 32, "ADDS", '0', '1')
    
def writebackSub_er32(binary):
    writeback_er(binary, 32, "SUB", '1', '0')
    
def writebackSubs_er32(binary):
    writeback_er(binary, 32, "SUBS", '1', '1')
    
def writebackAdd_er64(binary):
    writeback_er(binary, 64, "ADD", '0', '0')
    
def writebackAdds_er64(binary):
    writeback_er(binary, 64, "ADDS", '0', '1')
    
def writebackSub_er64(binary):
    writeback_er(binary, 64, "SUB", '1', '0')
    
def writebackSubs_er64(binary): 
    writeback_er(binary, 64, "SUBS", '1', '1')
    
