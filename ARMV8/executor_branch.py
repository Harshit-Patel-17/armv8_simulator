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
    '''
    inst ='B OFFSET('
    imm26key=binary[6:32]
    
    (instpart,offset)=utilFunc.getOffset(imm26key)
    inst+=instpart+')'
    
    utilFunc.branchWithOffset(offset) #the magic!
    utilFunc.finalize_simple(inst)
    '''
    
def execBCond(binary):
    const.FLAG_INST_EXECUTED = True
    bits_four=binary[-4:]
    xx=utilFunc.conditionHolds(bits_four)    
    if not xx[0]:
        return
    
    #inst ='B.'+xx[1]+' OFFSET('
    #imm19key=binary[8:27]
    
    (instpart,offset)=utilFunc.getOffset(mem.operand1Buffer)
    #inst+=instpart+')'
    
    utilFunc.branchWithOffset(offset-8) #the magic!
    armdebug.pipelineStages[0] = ''
    armdebug.pipelineStages[1] = ''
    mem.freeObsoleteRegisters()
    #utilFunc.finalize_simple(inst)
    
def execBL(binary):
    const.FLAG_INST_EXECUTED = True
    '''
    inst='BL OFFSET('
    imm26key=binary[-26:]
    
    (instpart,offset)=utilFunc.getOffset(imm26key)
    inst+=instpart+')'
    
    nextAddr=armdebug.getPC()+4
    utilFunc.setRegValue(30, utilFunc.intToBinary(nextAddr, 64), '0')
    utilFunc.branchWithOffset(offset)
    utilFunc.finalize_simple(inst)
    '''
    
def execBR(binary):
    const.FLAG_INST_EXECUTED = True
    '''
    inst = 'BR X'
    rnKey=binary[22:27]
    address_binary=utilFunc.getRegValueByStringkey(rnKey, '0')
    regnum=utilFunc.uInt(rnKey)
    inst+=str(regnum)
    hexstr = utilFunc.binaryToHexStr(address_binary)
    if not armdebug.checkIfValidBreakPoint(hexstr):
        utilFunc.finalize_simple('Instruction aborted. Invalid instruction address in register.')
        return
    utilFunc.branchToAddress(int(hexstr,16))
    utilFunc.finalize_simple(inst)
    '''
    
def execBLR(binary):
    const.FLAG_INST_EXECUTED = True
    '''
    inst='BLR X'
    rnKey=binary[22:27]
    address_binary=utilFunc.getRegValueByStringkey(rnKey, '0')
    regnum=utilFunc.uInt(rnKey)
    inst+=str(regnum)
    hexstr = utilFunc.binaryToHexStr(address_binary)
    if not armdebug.checkIfValidBreakPoint(hexstr):
        utilFunc.finalize_simple('Instruction aborted. Invalid instruction address in register.')
        return
    nextAddr=armdebug.getPC()+4
    utilFunc.setRegValue(30, utilFunc.intToBinary(nextAddr, 64), '0')
    utilFunc.branchToAddress(int(hexstr,16))
    utilFunc.finalize_simple(inst)
    '''
    
def execRET(binary):
    const.FLAG_INST_EXECUTED = True
    '''
    inst = 'RET X'
    rnKey=binary[22:27]
    address_binary=utilFunc.getRegValueByStringkey(rnKey, '0')
    regnum=utilFunc.uInt(rnKey)
    inst+=str(regnum)
    #print 'address binary: '+str(address_binary)
    hexstr = utilFunc.binaryToHexStr(address_binary)
    if not armdebug.checkIfValidBreakPoint(hexstr):
        utilFunc.finalize_simple('Instruction aborted. Invalid instruction address in register.')
        return
    utilFunc.branchToAddress(int(hexstr,16))
    utilFunc.finalize_simple(inst)
    '''
    
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
    '''
    inst='CBZ '
    char=''
    if width==64:
        char='X'
    else:
        char='W'
    inst+=char
    regnum=utilFunc.uInt(rtKey)
    inst+=str(regnum)+', OFFSET('
    imm19Key=binary[8:27]
    '''

    (instpart,offset)=utilFunc.getOffset(mem.operand1Buffer)
    #inst+=instpart+')'
    
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
    #utilFunc.finalize_simple(inst)