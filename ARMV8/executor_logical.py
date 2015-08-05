'''
Created on Aug 8, 2014

@author: harinder
'''

import utilFunc
import mem
import const

def op_i(binary, N):
    mem.ALUResultBuffer = utilFunc.logical_and(mem.operand1Buffer,mem.operand2Buffer).zfill(const.REG_SIZE)
    const.FLAG_INST_EXECUTED = True

def execAnd_i32(binary):
    op_i(binary, 32)
    
    
def execAnd_i64(binary):
    op_i(binary, 64)
    
    
def execAnd_sr32(binary):
    mem.ALUResultBuffer = utilFunc.logical_and(mem.operand1Buffer,mem.operand2Buffer).zfill(const.REG_SIZE)
    const.FLAG_INST_EXECUTED = True
    
def execAnd_sr64(binary):
    mem.ALUResultBuffer = utilFunc.logical_and(mem.operand1Buffer,mem.operand2Buffer).zfill(const.REG_SIZE)
    const.FLAG_INST_EXECUTED = True
