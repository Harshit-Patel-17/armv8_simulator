'''
Created on Aug 8, 2014

@author: abhishek
'''

import utilFunc
import const
import mem
import armdebug

def opfetchB(binary):
    inst ='B OFFSET('
    imm26key=binary[6:32]
    
    (instpart,offset)=utilFunc.getOffset(imm26key)
    inst+=instpart+')'
    
    utilFunc.branchWithOffset(offset-4) #the magic!
    armdebug.pipelineStages[0] = ''
    const.FLAG_OP_FETCHED = True
    const.FLAG_OPFETCH_EXECUTED = True
    
def opfetchBCond(binary):
    imm19key=binary[8:27]
    mem.operand1Buffer = imm19key
    const.FLAG_OP_FETCHED = True
    const.FLAG_OPFETCH_EXECUTED = True
    
def opfetchBL(binary):
    inst='BL OFFSET('
    imm26key=binary[-26:]
    
    (instpart,offset)=utilFunc.getOffset(imm26key)
    inst+=instpart+')'
    
    nextAddr=armdebug.getPC()
    utilFunc.setRegValue(30, utilFunc.intToBinary(nextAddr, 64), '0')
    utilFunc.branchWithOffset(offset-4)
    armdebug.pipelineStages[0] = ''
    const.FLAG_OP_FETCHED = True
    const.FLAG_OPFETCH_EXECUTED = True
    
def opfetchBR(binary):
    inst = 'BR X'
    rnKey=binary[22:27]
    
    const.FLAG_OPFETCH_EXECUTED = True
    #Check whether stalls are required or not
    if(mem.regObsolete[utilFunc.getRegKeyByStringKey(rnKey)] == False):
        const.FLAG_OP_FETCHED = True
    else:
        return
    
    address_binary=utilFunc.getRegValueByStringkey(rnKey, '0')
    regnum=utilFunc.uInt(rnKey)
    inst+=str(regnum)
    hexstr = utilFunc.binaryToHexStr(address_binary)
    if not armdebug.checkIfValidBreakPoint(hexstr):
        print 'Instruction aborted. Invalid instruction address in register.'
        return
    utilFunc.branchToAddress(int(hexstr,16))
    armdebug.pipelineStages[0] = ''
    
def opfetchBLR(binary):
    inst='BLR X'
    rnKey=binary[22:27]
    
    const.FLAG_OPFETCH_EXECUTED = True
    #Check whether stalls are required or not
    if(mem.regObsolete[rnKey] == False):
        const.FLAG_OP_FETCHED = True
    else:
        return
    
    address_binary=utilFunc.getRegValueByStringkey(rnKey, '0')
    regnum=utilFunc.uInt(rnKey)
    inst+=str(regnum)
    hexstr = utilFunc.binaryToHexStr(address_binary)
    if not armdebug.checkIfValidBreakPoint(hexstr):
        print 'Instruction aborted. Invalid instruction address in register.'
        return
    nextAddr=armdebug.getPC()
    utilFunc.setRegValue(30, utilFunc.intToBinary(nextAddr, 64), '0')
    utilFunc.branchToAddress(int(hexstr,16))
    armdebug.pipelineStages[0] = ''
    
def opfetchRET(binary):
    inst = 'RET X'
    rnKey=binary[22:27]
    
    const.FLAG_OPFETCH_EXECUTED = True
    #Check whether stalls are required or not
    if(mem.regObsolete[utilFunc.getRegKeyByStringKey(rnKey)] == False):
        const.FLAG_OP_FETCHED = True
    else:
        return
    
    address_binary=utilFunc.getRegValueByStringkey(rnKey, '0')
    regnum=utilFunc.uInt(rnKey)
    inst+=str(regnum)

    hexstr = utilFunc.binaryToHexStr(address_binary)
    if not armdebug.checkIfValidBreakPoint(hexstr):
        print 'Instruction aborted. Invalid instruction address in register.'
        return
    utilFunc.branchToAddress(int(hexstr,16))
    armdebug.pipelineStages[0] = ''
    
def opfetchCBZ_32(binary):
    CBZClass(binary, 32, True)
    
def opfetchCBNZ_32(binary):
    CBZClass(binary, 32, False)
    
def opfetchCBZ_64(binary):
    CBZClass(binary, 64, True)
    
def opfetchCBNZ_64(binary):
    CBZClass(binary, 64, False)

def CBZClass(binary,width,bool):
    rtKey=binary[-5:]
    
    const.FLAG_OPFETCH_EXECUTED = True
    #Check whether stalls are required or not
    if(mem.regObsolete[utilFunc.getRegKeyByStringKey(rtKey)] == False):
        const.FLAG_OP_FETCHED = True
    else:
        return
    
    imm19Key=binary[8:27]
    
    mem.operand1Buffer = imm19Key