'''
Created on Aug 8, 2014

@author: harinder
'''

import utilFunc
import mem
import const
import armdebug

def op_i(binary, N):
    const.FLAG_MEMACCESS_EXECUTED = True    
    const.FLAG_MEMACCESS_COMPLETED = True
    if(armdebug.pipelineStages[4] != '--------'):
        return
    
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    mem.writeBackBuffer[0] = mem.ALUResultBuffer
    mem.regValueAvailableInWB[rdKey] = True
    mem.regValueAvailableInWB_buffer_indices[rdKey] = 0
    mem.isSPWriteBackBuffer = mem.isSPBuffer
    #const.FLAG_MEMACCESS_EXECUTED = True
    #const.FLAG_MEMACCESS_COMPLETED = True

def memaccessAnd_i32(binary):
    op_i(binary, 32)
    
    
def memaccessAnd_i64(binary):
    op_i(binary, 64)

def memaccessAnds_i32(binary):
    op_i(binary, 32)

def memaccessAnds_i64(binary):
    op_i(binary, 64)
    
    
def memaccessAnd_sr32(binary):
    const.FLAG_MEMACCESS_EXECUTED = True    
    const.FLAG_MEMACCESS_COMPLETED = True
    if(armdebug.pipelineStages[4] != '--------'):
        return
    
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    mem.writeBackBuffer[0] = mem.ALUResultBuffer
    mem.regValueAvailableInWB[rdKey] = True
    mem.regValueAvailableInWB_buffer_indices[rdKey] = 0
    mem.isSPWriteBackBuffer = mem.isSPBuffer
    #const.FLAG_MEMACCESS_EXECUTED = True
    #const.FLAG_MEMACCESS_COMPLETED = True
    
def memaccessAnd_sr64(binary):
    const.FLAG_MEMACCESS_EXECUTED = True    
    const.FLAG_MEMACCESS_COMPLETED = True
    if(armdebug.pipelineStages[4] != '--------'):
        return
    
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    mem.writeBackBuffer[0] = mem.ALUResultBuffer
    mem.regValueAvailableInWB[rdKey] = True
    mem.regValueAvailableInWB_buffer_indices[rdKey] = 0
    mem.isSPWriteBackBuffer = mem.isSPBuffer
    #const.FLAG_MEMACCESS_EXECUTED = True
    #const.FLAG_MEMACCESS_COMPLETED = True

def memaccessAnds_sr32(binary):
    memaccessAnd_sr32(binary)
    
def memaccessAnds_sr64(binary):
    memaccessAnd_sr64(binary)