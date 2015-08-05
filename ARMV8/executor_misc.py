'''
Created on Aug 8, 2014

@author: abhiagar90
'''
import utilFunc
import armdebug
import mem
import const
    
def execADR(binary):
    mem.ALUResultBuffer = mem.operand1Buffer + mem.operand2Buffer
    const.FLAG_INST_EXECUTED = True
    
def execADRP(binary):
    mem.ALUResultBuffer = mem.operand1Buffer + mem.operand2Buffer
    const.FLAG_INST_EXECUTED = True

def execNOP(binary):
    const.FLAG_INST_EXECUTED = True