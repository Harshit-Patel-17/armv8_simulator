'''
Created on Aug 8, 2014

@author: abhiagar90
'''
import utilFunc
import armdebug
import mem
import const
    
def writebackADR(binary):
    rdKey=binary[-5:]
    regnum=utilFunc.uInt(rdKey)

    utilFunc.setRegValue(regnum, mem.writeBackBuffer[0], '0')
    const.FLAG_WRITEBACK_COMPLETED = True
    const.FLAG_WRITEBACK_EXECUTED = True
    mem.regObsolete[regnum] = False

def writebackADRP(binary):
    rdKey=binary[-5:]
    regnum=utilFunc.uInt(rdKey)

    utilFunc.setRegValue(regnum, mem.writeBackBuffer[0], '0')
    const.FLAG_WRITEBACK_COMPLETED = True
    const.FLAG_WRITEBACK_EXECUTED = True
    mem.regObsolete[regnum] = False

def writebackNOP(binary):
    const.FLAG_WRITEBACK_COMPLETED = True
    const.FLAG_WRITEBACK_EXECUTED = True