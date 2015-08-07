import utilFunc
import mem
import const


def writeback_i(binary, N, instr, sub_op, setFlags):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    
    if(rdKey != 31): #if CMN instruction,discard the result
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

    if(rdKey != 31): #if CMN instruction,discard the result
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

    if(rdKey != 31): #if CMN instruction,discard the result
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
    
