import utilFunc
import mem
import const


def memaccess_i(binary, N, instr, sub_op, setFlags):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    mem.writeBackBuffer[0] = mem.ALUResultBuffer
    mem.regValueAvailableInWB[rdKey] = True
    mem.regValueAvailableInWB_buffer_indices[rdKey] = 0
    mem.isSPWriteBackBuffer = mem.isSPBuffer
    const.FLAG_MEMACCESS_EXECUTED = True

def memaccessAdd_i32(binary):
    return memaccess_i(binary, 32, "ADD", '0', '0')

def memaccessAdds_i32(binary):
    return memaccess_i(binary, 32, "ADDS", '0', '1')
    
def memaccessSub_i32(binary):
    return memaccess_i(binary, 32, "SUB", '1', '0')
    
def memaccessSubs_i32(binary):
    return memaccess_i(binary, 32, "SUBS", '1', '1')
    
def memaccessAdd_i64(binary):
    return memaccess_i(binary, 64, "ADD", '0', '0')
    
def memaccessAdds_i64(binary):
    return memaccess_i(binary, 64, "ADDS", '0', '1') 
    
def memaccessSub_i64(binary):
    return memaccess_i(binary, 64, "SUB", '1', '0')
    
def memaccessSubs_i64(binary): 
    return memaccess_i(binary, 64, "SUBS", '1', '1')
    
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


    
def memaccess_sr(binary, N, instr, sub_op, setFlags):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    mem.writeBackBuffer[0] = mem.ALUResultBuffer
    mem.regValueAvailableInWB[rdKey] = True
    mem.regValueAvailableInWB_buffer_indices[rdKey] = 0
    mem.isSPWriteBackBuffer = mem.isSPBuffer
    const.FLAG_MEMACCESS_EXECUTED = True
    
def memaccessAdd_sr32(binary):
    return memaccess_sr(binary, 32, "ADD", '0', '0')
    
def memaccessAdds_sr32(binary):
    return memaccess_sr(binary, 32, "ADDS", '0', '1')
    
def memaccessSub_sr32(binary):
    return memaccess_sr(binary, 32, "SUB", '1', '0')
    
def memaccessSubs_sr32(binary):
    return memaccess_sr(binary, 32, "SUBS", '1', '1')
    
def memaccessAdd_sr64(binary):
    return memaccess_sr(binary, 64, "ADD", '0', '0')
    
def memaccessAdds_sr64(binary):
    return memaccess_sr(binary, 64, "ADDS", '0', '1')
    
def memaccessSub_sr64(binary):
    return memaccess_sr(binary, 64, "SUB", '1', '0')
    
def memaccessSubs_sr64(binary): 
    return memaccess_sr(binary, 64, "SUBS", '1', '1')
    
    
def memaccess_er(binary, N, instr, sub_op, setFlags):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    mem.writeBackBuffer[0] = mem.ALUResultBuffer
    mem.regValueAvailableInWB[rdKey] = True
    mem.regValueAvailableInWB_buffer_indices[rdKey] = 0
    mem.isSPWriteBackBuffer = mem.isSPBuffer
    const.FLAG_MEMACCESS_EXECUTED = True
       

# Add Subtract - Extended register
def memaccessAdd_er32(binary):
    memaccess_er(binary, 32, "ADD", '0', '0')
    
def memaccessAdds_er32(binary):
    memaccess_er(binary, 32, "ADDS", '0', '1')
    
def memaccessSub_er32(binary):
    memaccess_er(binary, 32, "SUB", '1', '0')
    
def memaccessSubs_er32(binary):
    memaccess_er(binary, 32, "SUBS", '1', '1')
    
def memaccessAdd_er64(binary):
    memaccess_er(binary, 64, "ADD", '0', '0')
    
def memaccessAdds_er64(binary):
    memaccess_er(binary, 64, "ADDS", '0', '1')
    
def memaccessSub_er64(binary):
    memaccess_er(binary, 64, "SUB", '1', '0')
    
def memaccessSubs_er64(binary): 
    memaccess_er(binary, 64, "SUBS", '1', '1')
    
