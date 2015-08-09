#author swarnadeep

import utilFunc
import mem
import const

#executes multiplation of two unsigned numbers.Takes as input the hex code for the UMULL instruction
def execMul(hexcode):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])

	unsigned_multiplication = int(mem.operand1Buffer,2) * int(mem.operand2Buffer,2)
	resultBinary = ("{0:b}".format(unsigned_multiplication))
	resultBinary = resultBinary.zfill(64)
	mem.ALUResultBuffer = resultBinary
	mem.regValueAvailableInALU[destRegister] = True
	const.FLAG_INST_EXECUTED = True

#executes division of two unsigned numbers(32 bit)
def execUnsignedDiv_32(hexcode):
	executeDivision(hexcode, 32, 0)

#executes division of two unsigned numbers(64 bit)
def execUnsignedDiv_64(hexcode):
	executeDivision(hexcode, 64, 0)
#executes division of two signed numbers(32 bit)
def execSignedDiv_32(hexcode):
	executeDivision(hexcode, 32, 1)

#executes division of two signed numbers(64 bit)
def execSignedDiv_64(hexcode):
	executeDivision(hexcode, 64, 1)

#common utility function for dividing two unsigned numbers
def executeDivision(hexcode, datasize, isSignedDivision):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])

	if(int(mem.operand2Buffer,2) == 0):
		resultBinary = ''
	else: 
		if(isSignedDivision):
			#instructionType = "SDIV "
			signedDivision = utilFunc.sInt(mem.operand1Buffer, datasize) / utilFunc.sInt(mem.operand2Buffer, datasize)
			resultBinary = utilFunc.intToBinary(signedDivision, datasize)
		else: 
			#instructionType = "UDIV "
			unsigned_division = int(mem.operand1Buffer,2) / int(mem.operand2Buffer,2)
			resultBinary = ("{0:b}".format(unsigned_division))

	resultBinary = resultBinary.zfill(64)
	mem.ALUResultBuffer = resultBinary
	mem.regValueAvailableInALU[destRegister] = True
	const.FLAG_INST_EXECUTED = True
