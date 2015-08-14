'''
@author: harinder
'''
import utilFunc
import mem
import const
import config
import armdebug


def op_i(binary, N, instr, sub_op, setFlags):
    const.FLAG_INST_EXECUTED = True    
    if(const.FLAG_EXECUTION_COMPLETED == False and const.EXECUTION_COUNTER == 0):
        const.EXECUTION_COUNTER = config.latency['IntALU']
    
    if(const.EXECUTION_COUNTER != 0):
        armdebug.intALUActivityCounter += 1
        const.EXECUTION_COUNTER -= 1
        
    if(const.EXECUTION_COUNTER == 0):
        const.FLAG_EXECUTION_COMPLETED = True
        if(armdebug.pipelineStages[3] != '--------'):
            return
    else:
        return
    
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    mem.ALUResultBuffer, mem.isSPBuffer = utilFunc.addSub(rdKey, mem.operand1Buffer, mem.operand2Buffer, sub_op, N, setFlags, 0)
    mem.ALUResultBuffer = mem.ALUResultBuffer.zfill(const.REG_SIZE)
    mem.regValueAvailableInALU[rdKey] = True
    const.FLAG_INST_EXECUTED = True

def execAdd_i32(binary):
    op_i(binary, 32, "ADD", '0', '0')

def execAdds_i32(binary):
    op_i(binary, 32, "ADDS", '0', '1')
    
def execSub_i32(binary):
    op_i(binary, 32, "SUB", '1', '0')
    
def execSubs_i32(binary):
    op_i(binary, 32, "SUBS", '1', '1')
    
def execAdd_i64(binary):
    op_i(binary, 64, "ADD", '0', '0')
    
def execAdds_i64(binary):
    op_i(binary, 64, "ADDS", '0', '1') 
    
def execSub_i64(binary):
    op_i(binary, 64, "SUB", '1', '0')
    
def execSubs_i64(binary): 
    op_i(binary, 64, "SUBS", '1', '1')
    
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


    
def op_sr(binary, N, instr, sub_op, setFlags):
    const.FLAG_INST_EXECUTED = True    
    if(const.FLAG_EXECUTION_COMPLETED == False and const.EXECUTION_COUNTER == 0):
        const.EXECUTION_COUNTER = config.latency['IntALU']
    
    if(const.EXECUTION_COUNTER != 0):
        armdebug.intALUActivityCounter += 1
        const.EXECUTION_COUNTER -= 1
        
    if(const.EXECUTION_COUNTER == 0):
        const.FLAG_EXECUTION_COMPLETED = True
        if(armdebug.pipelineStages[3] != '--------'):
            return
    else:
        return
    
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    mem.ALUResultBuffer,mem.isSPBuffer = utilFunc.addSub(rdKey, mem.operand1Buffer, mem.operand2Buffer, sub_op, N, setFlags, 0) #isSp ignored
    mem.ALUResultBuffer = mem.ALUResultBuffer.zfill(const.REG_SIZE)
    mem.regValueAvailableInALU[rdKey] = True
    const.FLAG_INST_EXECUTED = True

def execAdd_sr32(binary):
    op_sr(binary, 32, "ADD", '0', '0')
    
def execAdds_sr32(binary):
    op_sr(binary, 32, "ADDS", '0', '1')
    
def execSub_sr32(binary):
    op_sr(binary, 32, "SUB", '1', '0')
    
def execSubs_sr32(binary):
    op_sr(binary, 32, "SUBS", '1', '1')
    
def execAdd_sr64(binary):
    op_sr(binary, 64, "ADD", '0', '0')
    
def execAdds_sr64(binary):
    op_sr(binary, 64, "ADDS", '0', '1')
    
def execSub_sr64(binary):
    op_sr(binary, 64, "SUB", '1', '0')
    
def execSubs_sr64(binary): 
    op_sr(binary, 64, "SUBS", '1', '1')
    
    
def op_er(binary, N, instr, sub_op, setFlags):
    const.FLAG_INST_EXECUTED = True    
    if(const.FLAG_EXECUTION_COMPLETED == False and const.EXECUTION_COUNTER == 0):
        const.EXECUTION_COUNTER = config.latency['IntALU']
    
    if(const.EXECUTION_COUNTER != 0):
        armdebug.intALUActivityCounter += 1
        const.EXECUTION_COUNTER -= 1
        
    if(const.EXECUTION_COUNTER == 0):
        const.FLAG_EXECUTION_COMPLETED = True
        if(armdebug.pipelineStages[3] != '--------'):
            return
    else:
        return
    
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    mem.ALUResultBuffer, mem.isSPBuffer = utilFunc.addSub(rdKey, mem.operand1Buffer, mem.operand2Buffer, sub_op, N, setFlags, 0)
    mem.ALUResultBuffer = mem.ALUResultBuffer.zfill(const.REG_SIZE)
    mem.regValueAvailableInALU[rdKey] = True
    const.FLAG_INST_EXECUTED = True


# Add Subtract - Extended register
def execAdd_er32(binary):
    op_er(binary, 32, "ADD", '0', '0')
    
def execAdds_er32(binary):
    op_er(binary, 32, "ADDS", '0', '1')
    
def execSub_er32(binary):
    op_er(binary, 32, "SUB", '1', '0')
    
def execSubs_er32(binary):
    op_er(binary, 32, "SUBS", '1', '1')
    
def execAdd_er64(binary):
    op_er(binary, 64, "ADD", '0', '0')
    
def execAdds_er64(binary):
    op_er(binary, 64, "ADDS", '0', '1')
    
def execSub_er64(binary):
    op_er(binary, 64, "SUB", '1', '0')
    
def execSubs_er64(binary): 
    op_er(binary, 64, "SUBS", '1', '1')
    
