#author swarnadeep

import utilFunc
import mem
import const

#executes add with carry for 32 bits
def execADC_32(hexcode):
	execADC(hexcode, 32)

#executes add with carry for 64 bits
def execADC_64(hexcode):
	execADC(hexcode, 64)

#utility function for adding with carry
def execADC(hexcode, datasize):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	carryFlag = utilFunc.get_C_flag()
	resultBinary, isSP = utilFunc.addSub(destRegister, mem.operand1Buffer, mem.operand2Buffer, '0', datasize, '0', carryFlag)
	mem.ALUResultBuffer = resultBinary.zfill(const.REG_SIZE)
	mem.regValueAvailableInALU[destRegister] = True
	mem.isSPBuffer = isSP
	const.FLAG_INST_EXECUTED = True
	#utilFunc.finalize(destRegister, resultBinary, "ADC", isSP)

