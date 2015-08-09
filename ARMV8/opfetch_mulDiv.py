#author swarnadeep

import utilFunc
import mem
import const

#executes multiplation of two unsigned numbers.Takes as input the hex code for the UMULL instruction
def opfetchMul(hexcode):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	operandRegister1 = utilFunc.getRegKeyByStringKey(hexcode[22:27])
	operandRegister2 = utilFunc.getRegKeyByStringKey(hexcode[11:16])
	
	const.FLAG_OPFETCH_EXECUTED = True
	if(mem.regObsolete[operandRegister1] == False and mem.regObsolete[operandRegister2] == False):
		const.FLAG_OP_FETCHED = True
		reg1Value = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')
		reg2Value = utilFunc.getRegValueByStringkey(hexcode[11:16],'0')
	elif(const.FLAG_DATA_FORWARDING):
		forwardedValues = mem.findForwardedValues(operandRegister1, operandRegister2)
		if(forwardedValues[0] != None and forwardedValues[1] != None):
			const.FLAG_OP_FETCHED = True
			reg1Value = forwardedValues[0]
			reg2Value = forwardedValues[1]
		else:
			return
	else:
		return
	
	mem.regObsolete[destRegister] = True
	mem.regObsolete_last_modified_indices.append(destRegister)

	instruction = "UMULL " + "x" + str(destRegister) + ", w" + str(operandRegister1) + ", w" + str(operandRegister2)

	#reg1Value = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')
	#reg2Value = utilFunc.getRegValueByStringkey(hexcode[11:16],'0')
	
	mem.operand1Buffer = reg1Value
	mem.operand2Buffer = reg2Value

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

	const.FLAG_OPFETCH_EXECUTED = True
	if(mem.regObsolete[operandRegister1] == False and mem.regObsolete[operandRegister2] == False):
		const.FLAG_OP_FETCHED = True
		reg1Value = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')
		reg2Value = utilFunc.getRegValueByStringkey(hexcode[11:16],'0')
	elif(const.FLAG_DATA_FORWARDING):
		forwardedValues = mem.findForwardedValues(operandRegister1, operandRegister2)
		if(forwardedValues[0] != None and forwardedValues[1] != None):
			const.FLAG_OP_FETCHED = True
			reg1Value = forwardedValues[0]
			reg2Value = forwardedValues[1]
		else:
			return
	else:
		return
	
	mem.regObsolete[destRegister] = True
	mem.regObsolete_last_modified_indices.append(destRegister)

	#reg1Value = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')
	#reg2Value = utilFunc.getRegValueByStringkey(hexcode[11:16],'0')
	
	if(datasize == 32):
		reg1Value = reg1Value[32:64]
		reg2Value = reg2Value[32:64]

	mem.operand1Buffer = reg1Value
	mem.operand2Buffer = reg2Value