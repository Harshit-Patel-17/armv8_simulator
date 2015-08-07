#author swarnadeep

import utilFunc
import const
import mem

#returns if the given condition is satisfied or not
#note for cset the lsb of the condition is inverted
def isConditionSatisfiedFunction(condition, isLsbInverted):
	isConditionSatisfied = 0

	if((condition == "0001" and isLsbInverted) or (condition == "0000" and not(isLsbInverted))): #EQ
		isConditionSatisfied = (utilFunc.get_Z_flag() == '1')
	elif((condition == "0000" and isLsbInverted) or (condition == "0001" and not(isLsbInverted))): #NE
		isConditionSatisfied = (utilFunc.get_Z_flag() == '0')
	elif((condition == "0011" and isLsbInverted) or (condition == "0010" and not(isLsbInverted))): #CS
		isConditionSatisfied = (utilFunc.get_C_flag() == '1')
	elif((condition == "0010" and isLsbInverted) or (condition == "0011" and not(isLsbInverted))): #CC
		isConditionSatisfied = (utilFunc.get_C_flag() == '0')
	elif((condition == "0101" and isLsbInverted) or (condition == "0100" and not(isLsbInverted))): #MI
		isConditionSatisfied = (utilFunc.get_N_flag() == '1')
	elif((condition == "0100" and isLsbInverted) or (condition == "0101" and not(isLsbInverted))): #PL
		isConditionSatisfied = (utilFunc.get_N_flag() == '0')
	elif((condition == "0111" and isLsbInverted) or (condition == "0110" and not(isLsbInverted))): #VS
		isConditionSatisfied = (utilFunc.get_V_flag() == '1')
	elif((condition == "0110" and isLsbInverted) or (condition == "0111" and not(isLsbInverted))): #VE
		isConditionSatisfied = (utilFunc.get_V_flag() == '0')
	elif((condition == "1001" and isLsbInverted) or (condition == "1000" and not(isLsbInverted))): #HI
		isConditionSatisfied = (utilFunc.get_C_flag() == '1' and utilFunc.get_Z_flag() == '0')
	elif((condition == "1000" and isLsbInverted) or (condition == "1001" and not(isLsbInverted))): #LS
		isConditionSatisfied = (utilFunc.get_C_flag() == '0' or utilFunc.get_Z_flag() == '1')
	elif((condition == "1011" and isLsbInverted) or (condition == "1010" and not(isLsbInverted))): #GE
		isConditionSatisfied = (utilFunc.get_N_flag() == utilFunc.get_V_flag())
	elif((condition == "1010" and isLsbInverted) or (condition == "1011" and not(isLsbInverted))): #LT
		isConditionSatisfied = (utilFunc.get_N_flag() != utilFunc.get_V_flag())
	elif((condition == "1101" and isLsbInverted) or (condition == "1100" and not(isLsbInverted))): #GT
		isConditionSatisfied = (utilFunc.get_Z_flag() == '0' and utilFunc.get_N_flag() == utilFunc.get_V_flag())
	elif((condition == "1100" and isLsbInverted) or (condition == "1101" and not(isLsbInverted))): #LE 
		isConditionSatisfied = (utilFunc.get_Z_flag() == '1' or utilFunc.get_N_flag() != utilFunc.get_V_flag())

	return isConditionSatisfied

#executes conditional set for 32 bit registers
def memaccessConditionalSet_32(hexcode):
	executeConditionalSet(hexcode, 32)

#executes conditional set for 64 bit registers
def memaccessConditionalSet_64(hexcode):
	executeConditionalSet(hexcode,64)

#executes select conditional inverse for 32 bit registers
def memaccessConditionalSelectInverse_32(hexcode):
	executeConditionalSelectInverse(hexcode,32)

#executes select conditional inverse for 64 bit registers
def memaccessConditionalSelectInverse_64(hexcode):
	executeConditionalSelectInverse(hexcode,64)

#executes select conditional negate for 64 bit registers
def memaccessConditionalSelectNegation_32(hexcode):
	executeConditionalSelectNegate(hexcode,32)

#executes select conditional negate for 64 bit registers
def memaccessConditionalSelectNegation_64(hexcode):
	executeConditionalSelectNegate(hexcode,64)

#executes conditional select increment for 32 bit registers
def memaccessConditionalSelectIncrement_32(hexcode):
	executeConditionalSelectIncrement(hexcode,32)

#executes conditional select increment for 64 bit registers
def memaccessConditionalSelectIncrement_64(hexcode):
	executeConditionalSelectIncrement(hexcode,64)

#utility function for conditional set
def executeConditionalSet(hexcode, datasize):
	'''
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	condition = hexcode[16:20]

	isConditionSatisfied = isConditionSatisfiedFunction(condition, 1)

	resultBinary = ("{0:b}".format(isConditionSatisfied))
	resultBinary.zfill(datasize)

	if(datasize == 32):
		registerType = "w"
	else:
		registerType = "x"

	instruction = "CSET " + registerType + str(destRegister) + ", " + const.CONDITIONS_MAP_LSB_INVERTED[condition]

	utilFunc.finalize(destRegister, resultBinary, instruction, '1')
	'''
	mem.writeBackBuffer[0] = mem.ALUResultBuffer
	mem.isSPWriteBackBuffer = mem.isSPBuffer
	const.FLAG_MEMACCESS_EXECUTED = True

#utility function for conditional select inverse
def executeConditionalSelectInverse(hexcode, datasize):
	'''
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	operandRegister1 = utilFunc.getRegKeyByStringKey(hexcode[22:27])
	operandRegister2 = utilFunc.getRegKeyByStringKey(hexcode[11:16])

	reg1Value = utilFunc.getRegValueByStringkey(hexcode[22:27],'1')
	reg2Value = utilFunc.getRegValueByStringkey(hexcode[11:16],'1')

	condition = hexcode[16:20]

	isLsbInverted = 0

	if(operandRegister1 == operandRegister2):
		command = "CINV "
		isLsbInverted = 1
	else:
		command = "CSINV "

	if(isConditionSatisfiedFunction(condition, isLsbInverted)):
		if(command == "CINV "):
			reg1Value = utilFunc.negate(reg1Value)
		reg1Value = int(reg1Value, 2)
		resultBinary = ("{0:b}".format(reg1Value))
	else:
		if(command == "CSINV "):
			reg2Value = utilFunc.negate(reg2Value)
		reg2Value = int(reg2Value, 2)
		resultBinary = ("{0:b}".format(reg2Value))

	if(datasize == 32):
		registerType = "w"
	else:
		registerType = "x"

	if(command == "CINV "):
		instruction = command + registerType + str(destRegister) +", " + registerType + str(operandRegister1) + ", " + const.CONDITIONS_MAP_LSB_INVERTED[condition]
	else: 
		instruction = command + registerType + str(destRegister) +", " + registerType + str(operandRegister1) + ", " + registerType + str(operandRegister2) + ", " + const.CONDITIONS_MAP[condition]

	utilFunc.finalize(destRegister, resultBinary, instruction, '1')
	'''
	mem.writeBackBuffer[0] = mem.ALUResultBuffer
	mem.isSPWriteBackBuffer = mem.isSPBuffer
	const.FLAG_MEMACCESS_EXECUTED = True


#utility function for conditional select negate
def executeConditionalSelectNegate(hexcode, datasize):
	'''
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	operandRegister1 = utilFunc.getRegKeyByStringKey(hexcode[22:27])
	operandRegister2 = utilFunc.getRegKeyByStringKey(hexcode[11:16])

	reg1Value = utilFunc.getRegValueByStringkey(hexcode[22:27],'1')
	reg2Value = utilFunc.getRegValueByStringkey(hexcode[11:16],'1')

	condition = hexcode[16:20]

	isLsbInverted = 0

	if(operandRegister1 == operandRegister2):
		command = "CNEG "
		isLsbInverted = 1
	else:
		command = "CSNEG "

	if(isConditionSatisfiedFunction(condition, isLsbInverted)):
		if(command == "CNEG "):
			reg1Value = utilFunc.negate(reg1Value)
		reg1Value = int(reg1Value, 2)
		if(command == "CNEG "):
			reg1Value = reg1Value + 1
		resultBinary = ("{0:b}".format(reg1Value))
	else:
		if(command == "CSNEG "):
			reg2Value = utilFunc.negate(reg2Value)
		reg2Value = int(reg2Value, 2)
		if(command == "CSNEG "):
			reg2Value = reg2Value + 1
		resultBinary = ("{0:b}".format(reg2Value))
	
	if(datasize == 32):
		registerType = "w"
	else:
		registerType = "x"

	if(command == "CNEG "):
		instruction = command + registerType + str(destRegister) +", " + registerType + str(operandRegister1) + ", " + const.CONDITIONS_MAP_LSB_INVERTED[condition]
	else: 
		instruction = command + registerType + str(destRegister) +", " + registerType + str(operandRegister1) + ", " + registerType + str(operandRegister2) + ", " + const.CONDITIONS_MAP[condition]

	utilFunc.finalize(destRegister, resultBinary, instruction, '1')
	'''
	mem.writeBackBuffer[0] = mem.ALUResultBuffer
	mem.isSPWriteBackBuffer = mem.isSPBuffer
	const.FLAG_MEMACCESS_EXECUTED = True

#utility function for conditional select increment
def executeConditionalSelectIncrement(hexcode, datasize):
	mem.writeBackBuffer[0] = mem.ALUResultBuffer
	mem.isSPWriteBackBuffer = mem.isSPBuffer
	const.FLAG_MEMACCESS_EXECUTED = True

