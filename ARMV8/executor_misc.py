'''
Created on Aug 8, 2014

@author: abhiagar90
'''
import utilFunc
import armdebug
import mem
import const
    
def execADR(binary):
    '''
    inst='ADR X'
    rdKey=binary[-5:]
    regnum=utilFunc.uInt(rdKey)
    inst+=str(regnum)+', OFFSET('
    immLo=binary[1:3]
    immHi=binary[8:27]
    imm=immHi+immLo
    (inst_part,offset)=utilFunc.getOffsetWithoutTimes(imm)
    inst+=inst_part+')'
    nextAddr=utilFunc.PCwithOffset(offset)#as our PC implementation is wrong till now
    utilFunc.setRegValue(regnum, utilFunc.intToBinary(nextAddr, 64), '0')
    utilFunc.finalize_simple(inst)
    '''
    mem.ALUResultBuffer = mem.operand1Buffer + mem.operand2Buffer
    const.FLAG_INST_EXECUTED = True
    
def execADRP(binary):
    '''
    inst='ADRP X'
    rdKey=binary[-5:]
    regnum=utilFunc.uInt(rdKey)
    inst+=str(regnum)+', OFFSET('
    immLo=binary[1:3]
    immHi=binary[8:27]
    imm=immHi+immLo+'0'*12
    (inst_part,offset)=utilFunc.getOffsetWithoutTimes(imm)
    inst+=inst_part+')'
    nextAddr=utilFunc.PCwithPageOffset(12,offset)#as our PC implementation is wrong till now
    utilFunc.setRegValue(regnum, utilFunc.intToBinary(nextAddr, 64), '0')
    utilFunc.finalize_simple(inst)
    '''
    mem.ALUResultBuffer = mem.operand1Buffer + mem.operand2Buffer
    const.FLAG_INST_EXECUTED = True

def execNOP(binary):
    const.FLAG_INST_EXECUTED = True
    #utilFunc.finalize_simple("NOP")