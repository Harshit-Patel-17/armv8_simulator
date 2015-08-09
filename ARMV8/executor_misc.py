'''
Created on Aug 8, 2014

@author: abhiagar90
'''
import utilFunc
import armdebug
import mem
import const
    
def execADR(binary):
    rdKey=binary[-5:]
    regnum=utilFunc.uInt(rdKey)
    mem.ALUResultBuffer = mem.operand1Buffer + mem.operand2Buffer
    mem.ALUResultBuffer = utilFunc.intToBinary(mem.ALUResultBuffer, 64)
    mem.regValueAvailableInALU[regnum] = True
    const.FLAG_INST_EXECUTED = True
    
def execADRP(binary):
    rdKey=binary[-5:]
    regnum=utilFunc.uInt(rdKey)
    mem.ALUResultBuffer = mem.operand1Buffer + mem.operand2Buffer
    mem.ALUResultBuffer = utilFunc.intToBinary(mem.ALUResultBuffer, 64)
    mem.regValueAvailableInALU[regnum] = True
    const.FLAG_INST_EXECUTED = True

def execNOP(binary):
    const.FLAG_INST_EXECUTED = True