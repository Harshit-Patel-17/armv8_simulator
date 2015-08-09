#author swarnadeep

import utilFunc
import mem
import const

#executes add with carry for 32 bits
def memaccessADC_32(hexcode):
	execADC(hexcode, 32)

#executes add with carry for 64 bits
def memaccessADC_64(hexcode):
	execADC(hexcode, 64)

#utility function for adding with carry
def execADC(hexcode, datasize):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	'''
	operandRegister1 = utilFunc.getRegKeyByStringKey(hexcode[22:27])
	operandRegister2 = utilFunc.getRegKeyByStringKey(hexcode[11:16])

	reg1Value = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')
	reg2Value = utilFunc.getRegValueByStringkey(hexcode[11:16],'0')

	if(datasize == 32):
		registerType = "w"
		regValue1 = regValue1[32:64]
		regValue2 = regValue2[32:64]
	else:
		datasize = "x"

	carryFlag = utilFunc.get_C_flag()
	resultBinary, isSP = utilFunc.addSub(destRegister, regValue1, regValue2, '0', datasize, '0', carryFlag)

	utilFunc.finalize(destRegister, resultBinary, "ADC", isSP)
	'''
	mem.writeBackBuffer[0] = mem.ALUResultBuffer
	mem.regValueAvailableInWB[destRegister] = True
	mem.regValueAvailableInWB_buffer_indices[destRegister] = 0
	mem.isSPWriteBackBuffer = mem.isSPBuffer
	const.FLAG_MEMACCESS_EXECUTED = True

