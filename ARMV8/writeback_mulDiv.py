#author swarnadeep

import utilFunc
import mem
import const
import armdebug

#executes multiplation of two unsigned numbers.Takes as input the hex code for the UMULL instruction
def writebackMul(hexcode):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])

	utilFunc.setRegValue(destRegister, mem.writeBackBuffer[0], '0')
	armdebug.intRFActivityCounter += 1
	const.FLAG_WRITEBACK_COMPLETED = True
	const.FLAG_WRITEBACK_EXECUTED = True
	mem.regObsolete[destRegister] -= 1

#executes division of two unsigned numbers(32 bit)
def writebackUnsignedDiv_32(hexcode):
	executeDivision(hexcode, 32, 0)

#executes division of two unsigned numbers(64 bit)
def writebackUnsignedDiv_64(hexcode):
	executeDivision(hexcode, 64, 0)
#executes division of two signed numbers(32 bit)
def writebackSignedDiv_32(hexcode):
	executeDivision(hexcode, 32, 1)

#executes division of two signed numbers(64 bit)
def writebackSignedDiv_64(hexcode):
	executeDivision(hexcode, 64, 1)

#common utility function for dividing two unsigned numbers
def executeDivision(hexcode, datasize, isSignedDivision):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])

	utilFunc.setRegValue(destRegister, mem.writeBackBuffer[0], '0')
	armdebug.intRFActivityCounter += 1
	const.FLAG_WRITEBACK_COMPLETED = True
	const.FLAG_WRITEBACK_EXECUTED = True
	mem.regObsolete[destRegister] -= 1
