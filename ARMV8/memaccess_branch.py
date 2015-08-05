'''
Created on Aug 8, 2014

@author: abhishek
'''

import utilFunc
import mem
import const
import armdebug

def memaccessB(binary):
    mem.writeBackBuffer[0] = mem.ALUResultBuffer
    mem.isSPWriteBackBuffer = mem.isSPBuffer
    const.FLAG_MEMACCESS_EXECUTED = True
    
def memaccessBCond(binary):
    mem.writeBackBuffer[0] = mem.ALUResultBuffer
    mem.isSPWriteBackBuffer = mem.isSPBuffer
    const.FLAG_MEMACCESS_EXECUTED = True
    
def memaccessBL(binary):
    mem.writeBackBuffer[0] = mem.ALUResultBuffer
    mem.isSPWriteBackBuffer = mem.isSPBuffer
    const.FLAG_MEMACCESS_EXECUTED = True
    
def memaccessBR(binary):
    mem.writeBackBuffer[0] = mem.ALUResultBuffer
    mem.isSPWriteBackBuffer = mem.isSPBuffer
    const.FLAG_MEMACCESS_EXECUTED = True
    
def memaccessBLR(binary):
    mem.writeBackBuffer[0] = mem.ALUResultBuffer
    mem.isSPWriteBackBuffer = mem.isSPBuffer
    const.FLAG_MEMACCESS_EXECUTED = True
    
def memaccessRET(binary):
    mem.writeBackBuffer[0] = mem.ALUResultBuffer
    mem.isSPWriteBackBuffer = mem.isSPBuffer
    const.FLAG_MEMACCESS_EXECUTED = True
    
def memaccessCBZ_32(binary):
    CBZClass(binary, 32, True)
    
def memaccessCBNZ_32(binary):
    CBZClass(binary, 32, False)
    
def memaccessCBZ_64(binary):
    CBZClass(binary, 64, True)
    
def memaccessCBNZ_64(binary):
    CBZClass(binary, 64, False)

def CBZClass(binary,width,bool):
    mem.writeBackBuffer[0] = mem.ALUResultBuffer
    mem.isSPWriteBackBuffer = mem.isSPBuffer
    const.FLAG_MEMACCESS_EXECUTED = True