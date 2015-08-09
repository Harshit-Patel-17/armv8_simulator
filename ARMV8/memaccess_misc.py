'''
Created on Aug 8, 2014

@author: abhiagar90
'''
import utilFunc
import armdebug
import mem
import const
    
def memaccessADR(binary):
    rdKey=binary[-5:]
    regnum=utilFunc.uInt(rdKey)
    mem.writeBackBuffer[0] = mem.ALUResultBuffer
    mem.regValueAvailableInWB[regnum] = True
    mem.regValueAvailableInWB_buffer_indices[regnum] = 0
    mem.isSPWriteBackBuffer = mem.isSPBuffer
    const.FLAG_MEMACCESS_EXECUTED = True

def memaccessADRP(binary):
    rdKey=binary[-5:]
    regnum=utilFunc.uInt(rdKey)
    mem.writeBackBuffer[0] = mem.ALUResultBuffer
    mem.regValueAvailableInWB[regnum] = True
    mem.regValueAvailableInWB_buffer_indices[regnum] = 0
    mem.isSPWriteBackBuffer = mem.isSPBuffer
    const.FLAG_MEMACCESS_EXECUTED = True

def memaccessNOP(binary):
    mem.writeBackBuffer[0] = mem.ALUResultBuffer
    mem.isSPWriteBackBuffer = mem.isSPBuffer
    const.FLAG_MEMACCESS_EXECUTED = True