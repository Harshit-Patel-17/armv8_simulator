import utilFunc

#executes multiplation of two unsigned numbers.Takes as input the hex code for the UMULL instruction
def execMul(hexcode):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	operandRegister1 = utilFunc.getRegKeyByStringKey(hexcode[22:27])
	operandRegister2 = utilFunc.getRegKeyByStringKey(hexcode[11:16])

	instruction = "UMULL " + "x" + str(destRegister) + ", w" + str(operandRegister1) + ", w" + str(operandRegister2)

	reg1Value = utilFunc.getRegValueByStringkey(hexcode[22:27],'1')
	reg2Value = utilFunc.getRegValueByStringkey(hexcode[11:16],'1')

	unsigned_multiplication = int(reg1Value,2) * int(reg2Value,2)
	resultBinary = ("{0:b}".format(unsigned_multiplication))
	resultBinary.zfill(64)

	utilFunc.finalize(destRegister, resultBinary, instruction, '1')
