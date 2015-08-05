'''
Created on Aug 8, 2014

@author: abhishek
'''

import utilFunc
import const
import mem
#from utilFunc import uInt, signExtend, getRegValueByStringkey
import armdebug

def execB(binary):
    const.FLAG_INST_EXECUTED = True
    
def execBCond(binary):
    const.FLAG_INST_EXECUTED = True
    bits_four=binary[-4:]
    xx=utilFunc.conditionHolds(bits_four)    
    if not xx[0]:
        return
    
    (instpart,offset)=utilFunc.getOffset(mem.operand1Buffer)
    
    utilFunc.branchWithOffset(offset-8) #the magic!
    armdebug.pipelineStages[0] = ''
    armdebug.pipelineStages[1] = ''
    mem.freeObsoleteRegisters()
    
def execBL(binary):
    const.FLAG_INST_EXECUTED = True
    
def execBR(binary):
    const.FLAG_INST_EXECUTED = True
    
def execBLR(binary):
    const.FLAG_INST_EXECUTED = True
    
def execRET(binary):
    const.FLAG_INST_EXECUTED = True
    
def execCBZ_32(binary):
    CBZClass(binary, 32, True)
    
def execCBNZ_32(binary):
    CBZClass(binary, 32, False)
    
def execCBZ_64(binary):
    CBZClass(binary, 64, True)
    
def execCBNZ_64(binary):
    CBZClass(binary, 64, False)

def CBZClass(binary,width,bool):
    const.FLAG_INST_EXECUTED = True
    rtKey=binary[-5:]

    (instpart,offset)=utilFunc.getOffset(mem.operand1Buffer)
    
    regValue=utilFunc.getRegValueByStringkey(rtKey, '0')
    regValue=regValue[0:width]#since CBZ_32
    if bool:
        if regValue=='0'*width:
            utilFunc.branchWithOffset(offset-8)
            armdebug.pipelineStages[0] = ''
            armdebug.pipelineStages[1] = ''
            mem.freeObsoleteRegisters()
    else:
        if regValue!='0'*width:
            utilFunc.branchWithOffset(offset-8)
            armdebug.pipelineStages[0] = ''
            armdebug.pipelineStages[1] = ''
            mem.freeObsoleteRegisters()