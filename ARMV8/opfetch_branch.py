'''
Created on Aug 8, 2014

@author: abhishek
'''

import utilFunc
import const
import mem
#from utilFunc import uInt, signExtend, getRegValueByStringkey
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
    #utilFunc.finalize_simple(inst)
    
def opfetchBCond(binary):
    
    #bits_four=binary[-4:]
    #xx=utilFunc.conditionHolds(bits_four)    
    #if not xx[0]:
    #    return
    
    #inst ='B.'+xx[1]+' OFFSET('
    imm19key=binary[8:27]
    mem.operand1Buffer = imm19key
    #(instpart,offset)=utilFunc.getOffset(imm19key)
    #inst+=instpart+')'
    
    #utilFunc.branchWithOffset(offset) #the magic!
    #utilFunc.finalize_simple(inst)
    const.FLAG_OP_FETCHED = True
    const.FLAG_OPFETCH_EXECUTED = True
    
def opfetchBL(binary):
    inst='BL OFFSET('
    imm26key=binary[-26:]
    
    (instpart,offset)=utilFunc.getOffset(imm26key)
    inst+=instpart+')'
    
    #nextAddr=armdebug.getPC()+4
    nextAddr=armdebug.getPC()
    utilFunc.setRegValue(30, utilFunc.intToBinary(nextAddr, 64), '0')
    utilFunc.branchWithOffset(offset-4)
    armdebug.pipelineStages[0] = ''
    const.FLAG_OP_FETCHED = True
    const.FLAG_OPFETCH_EXECUTED = True
    #utilFunc.finalize_simple(inst)
    
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
    #utilFunc.finalize_simple(inst)
    
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
    #nextAddr=armdebug.getPC()+4
    nextAddr=armdebug.getPC()
    utilFunc.setRegValue(30, utilFunc.intToBinary(nextAddr, 64), '0')
    utilFunc.branchToAddress(int(hexstr,16))
    armdebug.pipelineStages[0] = ''
    #utilFunc.finalize_simple(inst)
    
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
    #print 'address binary: '+str(address_binary)
    hexstr = utilFunc.binaryToHexStr(address_binary)
    if not armdebug.checkIfValidBreakPoint(hexstr):
        print 'Instruction aborted. Invalid instruction address in register.'
        return
    utilFunc.branchToAddress(int(hexstr,16))
    armdebug.pipelineStages[0] = ''
    #utilFunc.finalize_simple(inst)
    
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
    
    mem.operand1Buffer = imm19Key

    '''
    (instpart,offset)=utilFunc.getOffset(imm19Key)
    inst+=instpart+')'
    
    regValue=utilFunc.getRegValueByStringkey(rtKey, '0')
    regValue=regValue[0:width]#since CBZ_32
    if bool:
        if regValue=='0'*width:
            utilFunc.branchWithOffset(offset)
    else:
        if regValue!='0'*width:
            utilFunc.branchWithOffset(offset)
    utilFunc.finalize_simple(inst)
    '''