'''
Created on Aug 8, 2014

@author: harinder
'''

import utilFunc
import mem
import const

def op_i(binary, N):
    mem.writeBackBuffer[0] = mem.ALUResultBuffer
    mem.isSPWriteBackBuffer = mem.isSPBuffer
    const.FLAG_MEMACCESS_EXECUTED = True

def memaccessAnd_i32(binary):
    op_i(binary, 32)
    
    
def memaccessAnd_i64(binary):
    op_i(binary, 64)
    
    
def memaccessAnd_sr32(binary):
    mem.writeBackBuffer[0] = mem.ALUResultBuffer
    mem.isSPWriteBackBuffer = mem.isSPBuffer
    const.FLAG_MEMACCESS_EXECUTED = True
    
def memaccessAnd_sr64(binary):
    mem.writeBackBuffer[0] = mem.ALUResultBuffer
    mem.isSPWriteBackBuffer = mem.isSPBuffer
    const.FLAG_MEMACCESS_EXECUTED = True
