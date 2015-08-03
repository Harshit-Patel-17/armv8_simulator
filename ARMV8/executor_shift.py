'''
@author: harinder
'''


import utilFunc
import mem
import const


# Helper function
def getFields_r(binary):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    rmKey = utilFunc.getRegKeyByStringKey(binary[11:16])
    rnVal = utilFunc.getRegValueByStringkey(binary[22:27], '0')
    rmVal = utilFunc.getRegValueByStringkey(binary[11:16], '0')
    return rdKey, rnKey, rmKey, rnVal, rmVal


def execAsr_r32(binary):
    #rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)
    #instr = 'ASR w' + str(rdKey) + ", w" + str(rnKey) + ", w" + str(rmKey)
    mem.ALUResultBuffer = '0' * 32 + utilFunc.asr(mem.operand1Buffer[32:64], int(mem.operand2Buffer[59:64], 2))
    #utilFunc.finalize(rdKey, rd, instr, '0')
    const.FLAG_INST_EXECUTED = True
                       
def execLsl_r32(binary):
    #rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)
    #instr = 'LSL w' + str(rdKey) + ", w" + str(rnKey) + ", w" + str(rmKey)
    mem.ALUResultBuffer = '0' * 32 + utilFunc.lsl(mem.operand1Buffer[32:64], int(mem.operand2Buffer[59:64], 2))
    #utilFunc.finalize(rdKey, rd, instr, '0')
    const.FLAG_INST_EXECUTED = True
    
def execLsr_r32(binary):
    #rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)
    #instr = 'LSR w' + str(rdKey) + ", w" + str(rnKey) + ", w" + str(rmKey)
    mem.ALUResultBuffer = '0' * 32 + utilFunc.lsr(mem.operand1Buffer[32:64], int(mem.operand2Buffer[59:64], 2))
    #utilFunc.finalize(rdKey, rd, instr, '0')
    const.FLAG_INST_EXECUTED = True
    
def execAsr_r64(binary):
    #rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)
    #instr = 'ASR x' + str(rdKey) + ", x" + str(rnKey) + ", x" + str(rmKey)
    mem.ALUResultBuffer = utilFunc.asr(mem.operand1Buffer, int(mem.operand2Buffer[58:64], 2))
    #utilFunc.finalize(rdKey, rd, instr, '0')
    const.FLAG_INST_EXECUTED = True 
                       
def execLsl_r64(binary):
    #rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)
    #instr = 'LSL x' + str(rdKey) + ", x" + str(rnKey) + ", x" + str(rmKey)
    mem.ALUResultBuffer = utilFunc.lsl(mem.operand1Buffer, int(mem.operand2Buffer[58:64], 2))
    #utilFunc.finalize(rdKey, rd, instr, '0')
    const.FLAG_INST_EXECUTED = True
    
def execLsr_r64(binary):
    #rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)
    #instr = 'LSR x' + str(rdKey) + ", x" + str(rnKey) + ", x" + str(rmKey)
    mem.ALUResultBuffer = utilFunc.lsr(mem.operand1Buffer, int(mem.operand2Buffer[58:64], 2))
    #utilFunc.finalize(rdKey, rd, instr, '0')
    const.FLAG_INST_EXECUTED = True
    
# Immediate operations
def execAsr_i32(binary):    
    rdKey, rnKey, rnVal, immr, imms = getFields_i(binary)
    if(imms == '011111'):
        shiftVal = int(immr,2)
        #instr = 'ASR w' + str(rdKey) + ", w" + str(rnKey) + ", #" + str(shiftVal)
        mem.ALUResultBuffer = '0' * 32 + utilFunc.asr(mem.operand1Buffer[32:64], shiftVal)
        #utilFunc.finalize(rdKey, rd, instr, '0')
    const.FLAG_INST_EXECUTED = True
    
def execAsr_i64(binary):
    rdKey, rnKey, rnVal, immr, imms = getFields_i(binary)
    if(imms == '111111'):
        shiftVal = int(immr,2)
        #instr = 'ASR x' + str(rdKey) + ", x" + str(rnKey) + ", #" + str(shiftVal)
        mem.ALUResultBuffer = utilFunc.asr(mem.operand1Buffer, shiftVal)
        #utilFunc.finalize(rdKey, rd, instr, '0')
    const.FLAG_INST_EXECUTED = True
                       
def execLslLsr_i32(binary):
    rdKey, rnKey, rnVal, immr, imms = getFields_i(binary)
    immrVal = int(immr,2)
    immsVal = int(imms,2)
    if(imms == '011111'):
        #LSR
        shiftVal = immrVal
        #instr = 'LSR w' + str(rdKey) + ", w" + str(rnKey) + ", #" + str(shiftVal)
        mem.ALUResultBuffer = '0' * 32 + utilFunc.lsr(mem.operand1Buffer[32:64], shiftVal)
    elif(immrVal == immsVal+1):
        #LSL
        shiftVal = 63-immsVal
        #instr = 'LSL w' + str(rdKey) + ", w" + str(rnKey) + ", #" + str(shiftVal)
        mem.ALUResultBuffer = '0' * 32 + utilFunc.lsl(mem.operand1Buffer[32:64], shiftVal)
    #utilFunc.finalize(rdKey, rd, instr, '0')
    const.FLAG_INST_EXECUTED = True
    
def execLslLsr_i64(binary):
    rdKey, rnKey, rnVal, immr, imms = getFields_i(binary)
    immrVal = int(immr,2)
    immsVal = int(imms,2)
    if(imms == '111111'):
        #LSR
        shiftVal = immrVal
        #instr = 'LSR x' + str(rdKey) + ", x" + str(rnKey) + ", #" + str(shiftVal)
        mem.ALUResultBuffer = utilFunc.lsr(mem.operand1Buffer, shiftVal)
    elif(immrVal == immsVal+1):
        #LSL
        shiftVal = 63-immsVal
        #instr = 'LSL x' + str(rdKey) + ", x" + str(rnKey) + ", #" + str(shiftVal)
        mem.ALUResultBuffer = utilFunc.lsl(mem.operand1Buffer, shiftVal)
    #utilFunc.finalize(rdKey, rd, instr, '0')
    const.FLAG_INST_EXECUTED = True

# Helper function
def getFields_i(binary):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    immr = binary[10:16]
    imms = binary[16:22]
    rnVal = utilFunc.getRegValueByStringkey(binary[22:27], '0')
    return rdKey, rnKey, rnVal, immr, imms
