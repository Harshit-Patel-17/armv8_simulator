'''
@author: harinder
'''


import utilFunc
import mem
import const
import config
import armdebug


# Helper function
def getFields_r(binary):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    rmKey = utilFunc.getRegKeyByStringKey(binary[11:16])
    rnVal = utilFunc.getRegValueByStringkey(binary[22:27], '0')
    rmVal = utilFunc.getRegValueByStringkey(binary[11:16], '0')
    return rdKey, rnKey, rmKey, rnVal, rmVal


def execAsr_r32(binary):
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
    mem.ALUResultBuffer = '0' * 32 + utilFunc.asr(mem.operand1Buffer[32:64], int(mem.operand2Buffer[59:64], 2))
    mem.ALUResultBuffer = mem.ALUResultBuffer.zfill(const.REG_SIZE)
    mem.regValueAvailableInALU[rdKey] = True
    #const.FLAG_INST_EXECUTED = True
                       
def execLsl_r32(binary):
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
    mem.ALUResultBuffer = '0' * 32 + utilFunc.lsl(mem.operand1Buffer[32:64], int(mem.operand2Buffer[59:64], 2))
    mem.ALUResultBuffer = mem.ALUResultBuffer.zfill(const.REG_SIZE)
    mem.regValueAvailableInALU[rdKey] = True
    #const.FLAG_INST_EXECUTED = True
    
def execLsr_r32(binary):
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
    mem.ALUResultBuffer = '0' * 32 + utilFunc.lsr(mem.operand1Buffer[32:64], int(mem.operand2Buffer[59:64], 2))
    mem.ALUResultBuffer = mem.ALUResultBuffer.zfill(const.REG_SIZE)
    mem.regValueAvailableInALU[rdKey] = True
    #const.FLAG_INST_EXECUTED = True
    
def execAsr_r64(binary):
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
    mem.ALUResultBuffer = utilFunc.asr(mem.operand1Buffer, int(mem.operand2Buffer[58:64], 2))
    mem.ALUResultBuffer = mem.ALUResultBuffer.zfill(const.REG_SIZE)
    mem.regValueAvailableInALU[rdKey] = True
    #const.FLAG_INST_EXECUTED = True 
                       
def execLsl_r64(binary):
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
    mem.ALUResultBuffer = utilFunc.lsl(mem.operand1Buffer, int(mem.operand2Buffer[58:64], 2))
    mem.ALUResultBuffer = mem.ALUResultBuffer.zfill(const.REG_SIZE)
    mem.regValueAvailableInALU[rdKey] = True
    #const.FLAG_INST_EXECUTED = True
    
def execLsr_r64(binary):
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
    mem.ALUResultBuffer = utilFunc.lsr(mem.operand1Buffer, int(mem.operand2Buffer[58:64], 2))
    mem.ALUResultBuffer = mem.ALUResultBuffer.zfill(const.REG_SIZE)
    mem.regValueAvailableInALU[rdKey] = True
    #const.FLAG_INST_EXECUTED = True
    
# Immediate operations
def execAsr_i32(binary):  
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
      
    rdKey, rnKey, rnVal, immr, imms = getFields_i(binary)
    if(imms == '011111'):
        shiftVal = int(immr,2)
        mem.ALUResultBuffer = '0' * 32 + utilFunc.asr(mem.operand1Buffer[32:64], shiftVal)
        mem.ALUResultBuffer = mem.ALUResultBuffer.zfill(const.REG_SIZE)
        mem.regValueAvailableInALU[rdKey] = True
    #const.FLAG_INST_EXECUTED = True
    
def execAsr_i64(binary):
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
    
    rdKey, rnKey, rnVal, immr, imms = getFields_i(binary)
    if(imms == '111111'):
        shiftVal = int(immr,2)
        mem.ALUResultBuffer = utilFunc.asr(mem.operand1Buffer, shiftVal)
        mem.ALUResultBuffer = mem.ALUResultBuffer.zfill(const.REG_SIZE)
        mem.regValueAvailableInALU[rdKey] = True
    #const.FLAG_INST_EXECUTED = True
                       
def execLslLsr_i32(binary):
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
    
    rdKey, rnKey, rnVal, immr, imms = getFields_i(binary)
    immrVal = int(immr,2)
    immsVal = int(imms,2)
    if(imms == '011111'):
        #LSR
        shiftVal = immrVal
        mem.ALUResultBuffer = '0' * 32 + utilFunc.lsr(mem.operand1Buffer[32:64], shiftVal)
        mem.ALUResultBuffer = mem.ALUResultBuffer.zfill(const.REG_SIZE)
        mem.regValueAvailableInALU[rdKey] = True
    elif(immrVal == immsVal+1):
        #LSL
        shiftVal = 63-immsVal
        mem.ALUResultBuffer = '0' * 32 + utilFunc.lsl(mem.operand1Buffer[32:64], shiftVal)
        mem.ALUResultBuffer = mem.ALUResultBuffer.zfill(const.REG_SIZE)
        mem.regValueAvailableInALU[rdKey] = True
    #const.FLAG_INST_EXECUTED = True
    
def execLslLsr_i64(binary):
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
    
    rdKey, rnKey, rnVal, immr, imms = getFields_i(binary)
    immrVal = int(immr,2)
    immsVal = int(imms,2)
    if(imms == '111111'):
        #LSR
        shiftVal = immrVal
        mem.ALUResultBuffer = utilFunc.lsr(mem.operand1Buffer, shiftVal)
        mem.ALUResultBuffer = mem.ALUResultBuffer.zfill(const.REG_SIZE)
        mem.regValueAvailableInALU[rdKey] = True
    elif(immrVal == immsVal+1):
        #LSL
        shiftVal = 63-immsVal
        mem.ALUResultBuffer = utilFunc.lsl(mem.operand1Buffer, shiftVal)
        mem.ALUResultBuffer = mem.ALUResultBuffer.zfill(const.REG_SIZE)
        mem.regValueAvailableInALU[rdKey] = True
    #const.FLAG_INST_EXECUTED = True

# Helper function
def getFields_i(binary):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    immr = binary[10:16]
    imms = binary[16:22]
    rnVal = utilFunc.getRegValueByStringkey(binary[22:27], '0')
    return rdKey, rnKey, rnVal, immr, imms
