#author swarnadeep

import utilFunc
import mem
import const

#executes CLS instruction(32 bit) 
def writebackCLS_32(hexcode):
	executeCLS(hexcode, 32)

#executes CLS instruction(64 bit)
def writebackCLS_64(hexcode):
	executeCLS(hexcode, 64)

#executes CLZ instruction(32 bit)
def writebackCLZ_32(hexcode):
	executeCLZ(hexcode,32)

#executes CLZ instruction(64 bit)
def writebackCLZ_64(hexcode):
	executeCLZ(hexcode,64)

#utility function for counting the number of leading sign bits
def executeCLS(hexcode, datasize):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	'''
	operandRegister = utilFunc.getRegKeyByStringKey(hexcode[22:27])

	regValue = utilFunc.getRegValueByStringkey(hexcode[22:27],'1')

	if(datasize == 32):
		registerType = "w"
		regValue = regValue[32:64]
	else:
		registerType = "x"

	result = utilFunc.countLeadingSignBits(regValue, datasize)
	resultBinary = "{0:b}".format(result)

	instruction = "CLS " + registerType + str(destRegister) + ", " + registerType + str(operandRegister)

	utilFunc.finalize(destRegister, resultBinary, instruction, '1')
	'''
	utilFunc.setRegValue(destRegister, mem.writeBackBuffer[0], '0')
	const.FLAG_WRITEBACK_EXECUTED = True
	mem.regObsolete[destRegister] = False

#utility function for counting the number of leading zero bits
def executeCLZ(hexcode, datasize):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	'''
	operandRegister = utilFunc.getRegKeyByStringKey(hexcode[22:27])

	regValue = utilFunc.getRegValueByStringkey(hexcode[22:27],'1')

	if(datasize == 32):
		registerType = "w"
		regValue = regValue[32:64]
	else:
		registerType = "x"

	result = utilFunc.countLeadingZeroBits(regValue, datasize)
	resultBinary = "{0:b}".format(result)

	instruction = "CLS " + registerType + str(destRegister) + ", " + registerType + str(operandRegister)

	utilFunc.finalize(destRegister, resultBinary, instruction, '1')
	'''
	utilFunc.setRegValue(destRegister, mem.writeBackBuffer[0], '0')
	const.FLAG_WRITEBACK_EXECUTED = True
	mem.regObsolete[destRegister] = False
