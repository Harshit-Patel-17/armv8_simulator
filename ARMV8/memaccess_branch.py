'''
Created on Aug 8, 2014

@author: abhishek
'''

import utilFunc
import mem
import const
import armdebug

def memaccessB(binary):
    const.FLAG_MEMACCESS_EXECUTED = True    
    const.FLAG_MEMACCESS_COMPLETED = True
    if(armdebug.pipelineStages[4] != '--------'):
        return

    mem.writeBackBuffer[0] = mem.ALUResultBuffer
    mem.isSPWriteBackBuffer = mem.isSPBuffer
    #const.FLAG_MEMACCESS_EXECUTED = True
    #const.FLAG_MEMACCESS_COMPLETED = True
    
def memaccessBCond(binary):
    const.FLAG_MEMACCESS_EXECUTED = True    
    const.FLAG_MEMACCESS_COMPLETED = True
    if(armdebug.pipelineStages[4] != '--------'):
        return

    mem.writeBackBuffer[0] = mem.ALUResultBuffer
    mem.isSPWriteBackBuffer = mem.isSPBuffer
    #const.FLAG_MEMACCESS_EXECUTED = True
    #const.FLAG_MEMACCESS_COMPLETED = True
    
def memaccessBL(binary):
    const.FLAG_MEMACCESS_EXECUTED = True    
    const.FLAG_MEMACCESS_COMPLETED = True
    if(armdebug.pipelineStages[4] != '--------'):
        return

    mem.writeBackBuffer[0] = mem.ALUResultBuffer
    mem.isSPWriteBackBuffer = mem.isSPBuffer
    #const.FLAG_MEMACCESS_EXECUTED = True
    #const.FLAG_MEMACCESS_COMPLETED = True
    
def memaccessBR(binary):
    const.FLAG_MEMACCESS_EXECUTED = True    
    const.FLAG_MEMACCESS_COMPLETED = True
    if(armdebug.pipelineStages[4] != '--------'):
        return

    mem.writeBackBuffer[0] = mem.ALUResultBuffer
    mem.isSPWriteBackBuffer = mem.isSPBuffer
    #const.FLAG_MEMACCESS_EXECUTED = True
    #const.FLAG_MEMACCESS_COMPLETED = True
    
def memaccessBLR(binary):
    const.FLAG_MEMACCESS_EXECUTED = True    
    const.FLAG_MEMACCESS_COMPLETED = True
    if(armdebug.pipelineStages[4] != '--------'):
        return

    mem.writeBackBuffer[0] = mem.ALUResultBuffer
    mem.isSPWriteBackBuffer = mem.isSPBuffer
    #const.FLAG_MEMACCESS_EXECUTED = True
    #const.FLAG_MEMACCESS_COMPLETED = True
    
def memaccessRET(binary):
    const.FLAG_MEMACCESS_EXECUTED = True    
    const.FLAG_MEMACCESS_COMPLETED = True
    if(armdebug.pipelineStages[4] != '--------'):
        return

    mem.writeBackBuffer[0] = mem.ALUResultBuffer
    mem.isSPWriteBackBuffer = mem.isSPBuffer
    #const.FLAG_MEMACCESS_EXECUTED = True
    #const.FLAG_MEMACCESS_COMPLETED = True
    
def memaccessCBZ_32(binary):
    CBZClass(binary, 32, True)
    
def memaccessCBNZ_32(binary):
    CBZClass(binary, 32, False)
    
def memaccessCBZ_64(binary):
    CBZClass(binary, 64, True)
    
def memaccessCBNZ_64(binary):
    CBZClass(binary, 64, False)

def CBZClass(binary,width,bool):
    const.FLAG_MEMACCESS_EXECUTED = True    
    const.FLAG_MEMACCESS_COMPLETED = True
    if(armdebug.pipelineStages[4] != '--------'):
        return

    mem.writeBackBuffer[0] = mem.ALUResultBuffer
    mem.isSPWriteBackBuffer = mem.isSPBuffer
    #const.FLAG_MEMACCESS_EXECUTED = True
    #const.FLAG_MEMACCESS_COMPLETED = True