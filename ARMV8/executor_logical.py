'''
Created on Aug 8, 2014

@author: harinder
'''

import utilFunc
import mem
import const

def op_i(binary, N, setFlags):
    mem.ALUResultBuffer = utilFunc.logical_and(mem.operand1Buffer,mem.operand2Buffer).zfill(const.REG_SIZE)
    if(setFlags):
    	flags = mem.ALUResultBuffer[0] + utilFunc.isZero(mem.ALUResultBuffer) + '00'
    	utilFunc.setFlags(flags)
    const.FLAG_INST_EXECUTED = True

def execAnd_i32(binary):
    op_i(binary, 32, 0)
    
    
def execAnd_i64(binary):
    op_i(binary, 64, 0)

def execAnds_i32(binary):
	op_i(binary, 32, 1)

def execAnds_i64(binary):
	op_i(binary, 64, 1)
    
def execAnd_sr32(binary):
    mem.ALUResultBuffer = utilFunc.logical_and(mem.operand1Buffer,mem.operand2Buffer).zfill(const.REG_SIZE)
    const.FLAG_INST_EXECUTED = True
    
def execAnd_sr64(binary):
    mem.ALUResultBuffer = utilFunc.logical_and(mem.operand1Buffer,mem.operand2Buffer).zfill(const.REG_SIZE)
    const.FLAG_INST_EXECUTED = True

def execAnds_sr32(binary):
    mem.ALUResultBuffer = utilFunc.logical_and(mem.operand1Buffer,mem.operand2Buffer).zfill(const.REG_SIZE)
    flags = mem.ALUResultBuffer[0] + utilFunc.isZero(mem.ALUResultBuffer) + '00'
    utilFunc.setFlags(flags)
    const.FLAG_INST_EXECUTED = True

def execAnds_sr64(binary):
    mem.ALUResultBuffer = utilFunc.logical_and(mem.operand1Buffer,mem.operand2Buffer).zfill(const.REG_SIZE)
    flags = mem.ALUResultBuffer[0] + utilFunc.isZero(mem.ALUResultBuffer) + '00'
    utilFunc.setFlags(flags)
    const.FLAG_INST_EXECUTED = True
