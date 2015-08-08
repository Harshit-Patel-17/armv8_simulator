'''
Created on Aug 8, 2014

@author: harinder
'''

import utilFunc
import mem
import const

def op_i(binary, N):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])

    utilFunc.setRegValue(rdKey, mem.writeBackBuffer[0], '1')
    const.FLAG_WRITEBACK_EXECUTED = True
    mem.regObsolete[rdKey] = False

def writebackAnd_i32(binary):
    op_i(binary, 32)
    
    
def writebackAnd_i64(binary):
    op_i(binary, 64)

def writebackAnds_i32(binary):
    op_i(binary, 32)

def writebackAnds_i32(binary):
    op_i(binary, 64)
    
    
def writebackAnd_sr32(binary):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])

    utilFunc.setRegValue(rdKey, mem.writeBackBuffer[0], '0')
    const.FLAG_WRITEBACK_EXECUTED = True
    mem.regObsolete[rdKey] = False
    
def writebackAnd_sr64(binary):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])

    utilFunc.setRegValue(rdKey, mem.writeBackBuffer[0], '0')
    const.FLAG_WRITEBACK_EXECUTED = True
    mem.regObsolete[rdKey] = False

def writebackAnds_sr32(binary):
    writebackAnd_sr32(binary)
    
def writebackAnds_sr64(binary):
    writebackAnd_sr64(binary)
    
