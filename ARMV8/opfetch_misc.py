'''
Created on Aug 8, 2014

@author: abhiagar90
'''
import utilFunc
import armdebug
import mem
import const
    
def opfetchADR(binary):
    inst='ADR X'
    rdKey=binary[-5:]
    regnum=utilFunc.uInt(rdKey)
    inst+=str(regnum)+', OFFSET('
    immLo=binary[1:3]
    immHi=binary[8:27]
    imm=immHi+immLo
    (inst_part,offset)=utilFunc.getOffsetWithoutTimes(imm)
    inst+=inst_part+')'
    
    const.FLAG_OP_FETCHED = True
    mem.operand1Buffer = armdebug.getPC() - 4
    mem.operand2Buffer = offset
    mem.regObsolete[regnum] = True
    mem.regObsolete_last_modified_indices.append(regnum)
    const.FLAG_OPFETCH_EXECUTED = True
    #nextAddr=utilFunc.PCwithOffset(offset)#as our PC implementation is wrong till now
    #utilFunc.setRegValue(regnum, utilFunc.intToBinary(nextAddr, 64), '0')
    #utilFunc.finalize_simple(inst)

def opfetchADRP(binary):
    inst='ADRP X'
    rdKey=binary[-5:]
    regnum=utilFunc.uInt(rdKey)
    inst+=str(regnum)+', OFFSET('
    immLo=binary[1:3]
    immHi=binary[8:27]
    imm=immHi+immLo+'0'*12
    (inst_part,offset)=utilFunc.getOffsetWithoutTimes(imm)
    inst+=inst_part+')'
    
    const.FLAG_OP_FETCHED = True
    operand1 = utilFunc.intToBinary(armdebug.getPC() - 4, 64)
    operand1 = int(operand1[0:52] + '0'*12, 2)
    mem.operand1Buffer = operand1
    mem.operand2Buffer = offset
    mem.regObsolete[regnum] = True
    mem.regObsolete_last_modified_indices.append(regnum)
    const.FLAG_OPFETCH_EXECUTED = True
    
    #nextAddr=utilFunc.PCwithPageOffset(12,offset)#as our PC implementation is wrong till now
    #utilFunc.setRegValue(regnum, utilFunc.intToBinary(nextAddr, 64), '0')
    #utilFunc.finalize_simple(inst)

def opfetchNOP(binary):
    const.FLAG_OP_FETCHED = True
    const.FLAG_OPFETCH_EXECUTED = True
    #utilFunc.finalize_simple("NOP")