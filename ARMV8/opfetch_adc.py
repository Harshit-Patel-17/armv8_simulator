#author swarnadeep

import utilFunc
import mem
import const

#executes add with carry for 32 bits
def opfetchADC_32(hexcode):
	execADC(hexcode, 32)

#executes add with carry for 64 bits
def opfetchADC_64(hexcode):
	execADC(hexcode, 64)

#utility function for adding with carry
def execADC(hexcode, datasize):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	operandRegister1 = utilFunc.getRegKeyByStringKey(hexcode[22:27])
	operandRegister2 = utilFunc.getRegKeyByStringKey(hexcode[11:16])

	regValue1 = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')
	regValue2 = utilFunc.getRegValueByStringkey(hexcode[11:16],'0')

	if(datasize == 32):
		registerType = "w"
		regValue1 = regValue1[32:64]
		regValue2 = regValue2[32:64]
	else:
		datasize = "x"
		
	if(mem.regObsolete[operandRegister1] == False and mem.regObsolete[operandRegister2] == False):
		const.FLAG_OP_FETCHED = True
		mem.operand1Buffer = regValue1
		mem.operand2Buffer = regValue2
		mem.regObsolete[destRegister] = True
		mem.regObsolete_last_modified_indices.append(destRegister)
	const.FLAG_OPFETCH_EXECUTED = True
	'''
	carryFlag = utilFunc.get_C_flag()
	resultBinary, isSP = utilFunc.addSub(destRegister, regValue1, regValue2, '0', datasize, '0', carryFlag)

	utilFunc.finalize(destRegister, resultBinary, "ADC", isSP)
	'''
