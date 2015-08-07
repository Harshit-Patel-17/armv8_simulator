#author swarnadeep

import utilFunc
import const
import mem

#executes CLS instruction(32 bit) 
def opfetchCLS_32(hexcode):
	executeCLS(hexcode, 32)

#executes CLS instruction(64 bit)
def opfetchCLS_64(hexcode):
	executeCLS(hexcode, 64)

#executes CLZ instruction(32 bit)
def opfetchCLZ_32(hexcode):
	executeCLZ(hexcode,32)

#executes CLZ instruction(64 bit)
def opfetchCLZ_64(hexcode):
	executeCLZ(hexcode,64)

#utility function for counting the number of leading sign bits
def executeCLS(hexcode, datasize):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	operandRegister = utilFunc.getRegKeyByStringKey(hexcode[22:27])

	regValue = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')
	
	if(datasize == 32):
		registerType = "w"
		regValue = regValue[32:64]
	else:
		registerType = "x"
	
	if(mem.regObsolete[operandRegister] == False):
		const.FLAG_OP_FETCHED = True
		mem.operand1Buffer = regValue
		mem.regObsolete[destRegister] = True
		mem.regObsolete_last_modified_indices.append(destRegister)
	const.FLAG_OPFETCH_EXECUTED = True
	'''
	result = utilFunc.countLeadingSignBits(regValue, datasize)
	resultBinary = "{0:b}".format(result)

	instruction = "CLS " + registerType + str(destRegister) + ", " + registerType + str(operandRegister)

	utilFunc.finalize(destRegister, resultBinary, instruction, '1')
	'''

#utility function for counting the number of leading zero bits
def executeCLZ(hexcode, datasize):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	operandRegister = utilFunc.getRegKeyByStringKey(hexcode[22:27])

	regValue = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')
	
	if(datasize == 32):
		registerType = "w"
		regValue = regValue[32:64]
	else:
		registerType = "x"

	if(mem.regObsolete[operandRegister] == False):
		const.FLAG_OP_FETCHED = True
		mem.operand1Buffer = regValue
		mem.regObsolete[destRegister] = True
		mem.regObsolete_last_modified_indices.append(destRegister)
	const.FLAG_OPFETCH_EXECUTED = True
	'''
	result = utilFunc.countLeadingZeroBits(regValue, datasize)
	resultBinary = "{0:b}".format(result)

	instruction = "CLS " + registerType + str(destRegister) + ", " + registerType + str(operandRegister)

	utilFunc.finalize(destRegister, resultBinary, instruction, '1')
	'''