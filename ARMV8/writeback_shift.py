'''
@author: harinder
'''


import utilFunc
import mem
import const
import armdebug

# Helper function
def getFields_r(binary):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    rmKey = utilFunc.getRegKeyByStringKey(binary[11:16])
    rnVal = utilFunc.getRegValueByStringkey(binary[22:27], '0')
    rmVal = utilFunc.getRegValueByStringkey(binary[11:16], '0')
    return rdKey, rnKey, rmKey, rnVal, rmVal


def writebackAsr_r32(binary):
    rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)
    
    utilFunc.setRegValue(rdKey, mem.writeBackBuffer[0], '0')
    armdebug.intRFActivityCounter += 1
    const.FLAG_WRITEBACK_COMPLETED = True
    const.FLAG_WRITEBACK_EXECUTED = True
    mem.regObsolete[rdKey] -= 1 
                       
def writebackLsl_r32(binary):
    rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)

    utilFunc.setRegValue(rdKey, mem.writeBackBuffer[0], '0')
    armdebug.intRFActivityCounter += 1
    const.FLAG_WRITEBACK_COMPLETED = True
    const.FLAG_WRITEBACK_EXECUTED = True
    mem.regObsolete[rdKey] -= 1
    
def writebackLsr_r32(binary):
    rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)

    utilFunc.setRegValue(rdKey, mem.writeBackBuffer[0], '0')
    armdebug.intRFActivityCounter += 1
    const.FLAG_WRITEBACK_COMPLETED = True
    const.FLAG_WRITEBACK_EXECUTED = True
    mem.regObsolete[rdKey] -= 1
    
def writebackAsr_r64(binary):
    rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)

    utilFunc.setRegValue(rdKey, mem.writeBackBuffer[0], '0')
    armdebug.intRFActivityCounter += 1
    const.FLAG_WRITEBACK_COMPLETED = True
    const.FLAG_WRITEBACK_EXECUTED = True
    mem.regObsolete[rdKey] -= 1
                       
def writebackLsl_r64(binary):
    rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)

    utilFunc.setRegValue(rdKey, mem.writeBackBuffer[0], '0')
    armdebug.intRFActivityCounter += 1
    const.FLAG_WRITEBACK_COMPLETED = True
    const.FLAG_WRITEBACK_EXECUTED = True
    mem.regObsolete[rdKey] -= 1
    
def writebackLsr_r64(binary):
    rdKey, rnKey, rmKey, rnVal, rmVal = getFields_r(binary)

    utilFunc.setRegValue(rdKey, mem.writeBackBuffer[0], '0')
    armdebug.intRFActivityCounter += 1
    const.FLAG_WRITEBACK_COMPLETED = True
    const.FLAG_WRITEBACK_EXECUTED = True
    mem.regObsolete[rdKey] -= 1

# Immediate operations
def writebackAsr_i32(binary):    
    rdKey, rnKey, rnVal, immr, imms = getFields_i(binary)
    if(imms == '011111'):
        utilFunc.setRegValue(rdKey, mem.writeBackBuffer[0], '0')
        armdebug.intRFActivityCounter += 1
    const.FLAG_WRITEBACK_COMPLETED = True
    const.FLAG_WRITEBACK_EXECUTED = True
    mem.regObsolete[rdKey] -= 1
    
def writebackAsr_i64(binary):
    rdKey, rnKey, rnVal, immr, imms = getFields_i(binary)
    if(imms == '111111'):
        utilFunc.setRegValue(rdKey, mem.writeBackBuffer[0], '0')
        armdebug.intRFActivityCounter += 1
    const.FLAG_WRITEBACK_COMPLETED = True
    const.FLAG_WRITEBACK_EXECUTED = True
    mem.regObsolete[rdKey] -= 1
                       
def writebackLslLsr_i32(binary):
    rdKey, rnKey, rnVal, immr, imms = getFields_i(binary)

    utilFunc.setRegValue(rdKey, mem.writeBackBuffer[0], '0')
    armdebug.intRFActivityCounter += 1
    const.FLAG_WRITEBACK_COMPLETED = True
    const.FLAG_WRITEBACK_EXECUTED = True
    mem.regObsolete[rdKey] -= 1
    
def writebackLslLsr_i64(binary):
    rdKey, rnKey, rnVal, immr, imms = getFields_i(binary)

    utilFunc.setRegValue(rdKey, mem.writeBackBuffer[0], '0')
    armdebug.intRFActivityCounter += 1
    const.FLAG_WRITEBACK_COMPLETED = True
    const.FLAG_WRITEBACK_EXECUTED = True
    mem.regObsolete[rdKey] -= 1

# Helper function
def getFields_i(binary):
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    immr = binary[10:16]
    imms = binary[16:22]
    rnVal = utilFunc.getRegValueByStringkey(binary[22:27], '0')
    return rdKey, rnKey, rnVal, immr, imms
