#author swarnadeep

import utilFunc
import mem
import const

#executes multiplation of two unsigned numbers.Takes as input the hex code for the UMULL instruction
def opfetchMul(hexcode):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	operandRegister1 = utilFunc.getRegKeyByStringKey(hexcode[22:27])
	operandRegister2 = utilFunc.getRegKeyByStringKey(hexcode[11:16])

	instruction = "UMULL " + "x" + str(destRegister) + ", w" + str(operandRegister1) + ", w" + str(operandRegister2)

	reg1Value = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')
	reg2Value = utilFunc.getRegValueByStringkey(hexcode[11:16],'0')
	
	if(mem.regObsolete[operandRegister1] == False and mem.regObsolete[operandRegister2] == False):
		const.FLAG_OP_FETCHED = True
		mem.operand1Buffer = reg1Value
		mem.operand2Buffer = reg2Value
		mem.regObsolete[destRegister] = True
		mem.regObsolete_last_modified_indices.append(destRegister)
	const.FLAG_OPFETCH_EXECUTED = True

	#unsigned_multiplication = int(reg1Value,2) * int(reg2Value,2)
	#resultBinary = ("{0:b}".format(unsigned_multiplication))
	#resultBinary.zfill(64)

	#utilFunc.finalize(destRegister, resultBinary, instruction, '1')

#executes division of two unsigned numbers(32 bit)
def opfetchUnsignedDiv_32(hexcode):
	executeDivision(hexcode, 32, 0)

#executes division of two unsigned numbers(64 bit)
def opfetchUnsignedDiv_64(hexcode):
	executeDivision(hexcode, 64, 0)
#executes division of two signed numbers(32 bit)
def opfetchSignedDiv_32(hexcode):
	executeDivision(hexcode, 32, 1)

#executes division of two signed numbers(64 bit)
def opfetchSignedDiv_64(hexcode):
	executeDivision(hexcode, 64, 1)

#common utility function for dividing two unsigned numbers
def executeDivision(hexcode, datasize, isSignedDivision):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	operandRegister1 = utilFunc.getRegKeyByStringKey(hexcode[22:27])
	operandRegister2 = utilFunc.getRegKeyByStringKey(hexcode[11:16])

	'''
	if(datasize == 32):
		registerType = "w"
	else:
		registerType = "x"
	'''

	reg1Value = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')
	reg2Value = utilFunc.getRegValueByStringkey(hexcode[11:16],'0')
	
	if(datasize == 32):
		reg1Value = reg1Value[32:64]
		reg2Value = reg2Value[32:64]

	if(mem.regObsolete[operandRegister1] == False and mem.regObsolete[operandRegister2] == False):
		const.FLAG_OP_FETCHED = True
		mem.operand1Buffer = reg1Value
		mem.operand2Buffer = reg2Value
		mem.regObsolete[destRegister] = True
		mem.regObsolete_last_modified_indices.append(destRegister)
	const.FLAG_OPFETCH_EXECUTED = True
	'''
	if(int(reg2Value,2) == 0):
		unsigned_division = 0
	else: 
		if(isSignedDivision):
			instructionType = "SDIV "
			signedDivision = utilFunc.sInt(reg1Value, datasize) / utilFunc.sInt(reg2Value, datasize)
			resultBinary = utilFunc.intToBinary(signedDivision, datasize)
		else: 
			instructionType = "UDIV "
			unsigned_division = int(reg1Value,2) / int(reg2Value,2)
			resultBinary = ("{0:b}".format(unsigned_division))

	instruction = instructionType + registerType + str(destRegister) + ", " + registerType + str(operandRegister1) + ", " + registerType + str(operandRegister2)

	resultBinary.zfill(datasize)

	utilFunc.finalize(destRegister, resultBinary, instruction, '1')
	'''
