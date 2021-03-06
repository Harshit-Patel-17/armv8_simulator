#author swarnadeep

import utilFunc
import const
import mem
import armdebug

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
def opfetchConditionalSet_32(hexcode):
	executeConditionalSet(hexcode, 32)

#executes conditional set for 64 bit registers
def opfetchConditionalSet_64(hexcode):
	executeConditionalSet(hexcode,64)

#executes select conditional inverse for 32 bit registers
def opfetchConditionalSelectInverse_32(hexcode):
	executeConditionalSelectInverse(hexcode,32)

#executes select conditional inverse for 64 bit registers
def opfetchConditionalSelectInverse_64(hexcode):
	executeConditionalSelectInverse(hexcode,64)

#executes select conditional negate for 64 bit registers
def opfetchConditionalSelectNegation_32(hexcode):
	executeConditionalSelectNegate(hexcode,32)

#executes select conditional negate for 64 bit registers
def opfetchConditionalSelectNegation_64(hexcode):
	executeConditionalSelectNegate(hexcode,64)

#executes conditional select increment for 32 bit registers
def opfetchConditionalSelectIncrement_32(hexcode):
	executeConditionalSelectIncrement(hexcode,32)

#executes conditional select increment for 64 bit registers
def opfetchConditionalSelectIncrement_64(hexcode):
	executeConditionalSelectIncrement(hexcode,64)

#executes conditional compare negative immediate for 32 bit registers
def opfetchConditionalCompareNegative_i32(hexcode):
	execConditionalCompareNegativeImmediate(hexcode, 32)

#executes conditional compare negative immediate for 64 bit registers
def opfetchConditionalCompareNegative_i64(hexcode):
	execConditionalCompareNegativeImmediate(hexcode, 64)

#executes conditional compare negative register for 32 bits
def opfetchConditionalCompareNegative_r32(hexcode):
	execConditionalCompareNegativeRegister(hexcode, 32)

#executes conditional compare negative register for 64 bits
def opfetchConditionalCompareNegative_r64(hexcode):
	execConditionalCompareNegativeRegister(hexcode, 64)

#utility function for conditional set
def executeConditionalSet(hexcode, datasize):
	const.FLAG_OPFETCH_EXECUTED = True
	if(armdebug.pipelineStages[2] != '--------'):
		return
	
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	
	const.FLAG_OP_FETCHED = True
	mem.regObsolete[destRegister] += 1
	mem.regObsolete_last_modified_indices.append(destRegister)

#utility function for conditional select inverse
def executeConditionalSelectInverse(hexcode, datasize):
	const.FLAG_OPFETCH_EXECUTED = True
	if(armdebug.pipelineStages[2] != '--------'):
		return
	
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	operandRegister1 = utilFunc.getRegKeyByStringKey(hexcode[22:27])
	operandRegister2 = utilFunc.getRegKeyByStringKey(hexcode[11:16])
	
	if(mem.regObsolete[operandRegister1] == 0 and mem.regObsolete[operandRegister2] == 0):
		const.FLAG_OP_FETCHED = True
		reg1Value = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')
		reg2Value = utilFunc.getRegValueByStringkey(hexcode[11:16],'0')
		armdebug.intRFActivityCounter += 2
	elif(const.FLAG_DATA_FORWARDING):
		forwardedValues = mem.findForwardedValues(operandRegister1, operandRegister2)
		if(forwardedValues[0] == None and mem.regObsolete[operandRegister1] != 0):
			return
		if(forwardedValues[1] == None and mem.regObsolete[operandRegister2] != 0):
			return
		const.FLAG_OP_FETCHED = True
		reg1Value = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')
		reg2Value = utilFunc.getRegValueByStringkey(hexcode[11:16],'0')
		if(forwardedValues[0] != None):
			reg1Value = forwardedValues[0]
		if(forwardedValues[1] != None):
			reg2Value = forwardedValues[1]
		if(None in forwardedValues):
			armdebug.intRFActivityCounter += 1
	else:
		return
	
	mem.regObsolete[destRegister] += 1
	mem.regObsolete_last_modified_indices.append(destRegister)

	#reg1Value = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')
	#reg2Value = utilFunc.getRegValueByStringkey(hexcode[11:16],'0')
	
	if(datasize == 32):
		reg1Value = reg1Value[32:64]
		reg2Value = reg2Value[32:64]

	mem.operand1Buffer = reg1Value
	mem.operand2Buffer = reg2Value

#utility function for conditional select negate
def executeConditionalSelectNegate(hexcode, datasize):
	const.FLAG_OPFETCH_EXECUTED = True
	if(armdebug.pipelineStages[2] != '--------'):
		return
	
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	operandRegister1 = utilFunc.getRegKeyByStringKey(hexcode[22:27])
	operandRegister2 = utilFunc.getRegKeyByStringKey(hexcode[11:16])
	
	if(mem.regObsolete[operandRegister1] == 0 and mem.regObsolete[operandRegister2] == 0):
		const.FLAG_OP_FETCHED = True
		reg1Value = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')
		reg2Value = utilFunc.getRegValueByStringkey(hexcode[11:16],'0')
		armdebug.intRFActivityCounter += 2
	elif(const.FLAG_DATA_FORWARDING):
		forwardedValues = mem.findForwardedValues(operandRegister1, operandRegister2)
		if(forwardedValues[0] == None and mem.regObsolete[operandRegister1] != 0):
			return
		if(forwardedValues[1] == None and mem.regObsolete[operandRegister2] != 0):
			return
		const.FLAG_OP_FETCHED = True
		reg1Value = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')
		reg2Value = utilFunc.getRegValueByStringkey(hexcode[11:16],'0')
		if(forwardedValues[0] != None):
			reg1Value = forwardedValues[0]
		if(forwardedValues[1] != None):
			reg2Value = forwardedValues[1]
		if(None in forwardedValues):
			armdebug.intRFActivityCounter += 1
	else:
		return
	
	mem.regObsolete[destRegister] += 1
	mem.regObsolete_last_modified_indices.append(destRegister)

	#reg1Value = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')
	#reg2Value = utilFunc.getRegValueByStringkey(hexcode[11:16],'0')
	
	if(datasize == 32):
		reg1Value = reg1Value[32:64]
		reg2Value = reg2Value[32:64]
	
	mem.operand1Buffer = reg1Value
	mem.operand2Buffer = reg2Value
	
#utility function for conditional select increment
def executeConditionalSelectIncrement(hexcode, datasize):
	const.FLAG_OPFETCH_EXECUTED = True
	if(armdebug.pipelineStages[2] != '--------'):
		return
	
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	operandRegister1 = utilFunc.getRegKeyByStringKey(hexcode[22:27])
	operandRegister2 = utilFunc.getRegKeyByStringKey(hexcode[11:16])
	
	if(mem.regObsolete[operandRegister1] == 0 and mem.regObsolete[operandRegister2] == 0):
		const.FLAG_OP_FETCHED = True
		reg1Value = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')
		reg2Value = utilFunc.getRegValueByStringkey(hexcode[11:16],'0')
		armdebug.intRFActivityCounter += 2
	elif(const.FLAG_DATA_FORWARDING):
		forwardedValues = mem.findForwardedValues(operandRegister1, operandRegister2)
		if(forwardedValues[0] == None and mem.regObsolete[operandRegister1] != 0):
			return
		if(forwardedValues[1] == None and mem.regObsolete[operandRegister2] != 0):
			return
		const.FLAG_OP_FETCHED = True
		reg1Value = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')
		reg2Value = utilFunc.getRegValueByStringkey(hexcode[11:16],'0')
		if(forwardedValues[0] != None):
			reg1Value = forwardedValues[0]
		if(forwardedValues[1] != None):
			reg2Value = forwardedValues[1]
		if(None in forwardedValues):
			armdebug.intRFActivityCounter += 1
	else:
		return
	
	mem.regObsolete[destRegister] += 1
	mem.regObsolete_last_modified_indices.append(destRegister)

	#reg1Value = utilFunc.getRegValueByStringkey(hexcode[22:27],'1')
	#reg2Value = utilFunc.getRegValueByStringkey(hexcode[11:16],'1')
	
	
	mem.operand1Buffer = reg1Value
	mem.operand2Buffer = reg2Value

#utility function for conditional compare negative immediate
def execConditionalCompareNegativeImmediate(hexcode, datasize):
	const.FLAG_OPFETCH_EXECUTED = True
	if(armdebug.pipelineStages[2] != '--------'):
		return
	
	#flags = hexcode[28:32]
	operandRegister = utilFunc.getRegKeyByStringKey(hexcode[22:27])
	#condition = hexcode[16:20]
	immediateBinary = hexcode[11:16]
	
	if(mem.regObsolete[operandRegister] == 0):
		const.FLAG_OP_FETCHED = True
		regValue = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')
		armdebug.intRFActivityCounter += 1
	elif(const.FLAG_DATA_FORWARDING):
		forwardedValues = mem.findForwardedValues(operandRegister)
		if(forwardedValues[0] != None):
			const.FLAG_OP_FETCHED = True
			regValue = forwardedValues[0]
		else:
			return
	else:
		return
	
	#regValue = utilFunc.getRegValueByStringkey(hexcode[22:27], 0)

	#immediateValue = int(immediateBinary, 2)

	if(datasize == 32):
		registerType = "w"
		regValue = regValue[32:64]
	else:
		datasize = "x"

	mem.operand1Buffer = regValue
	mem.operand2Buffer = immediateBinary.zfill(datasize)

#utility function for conditional compare negative register
def execConditionalCompareNegativeRegister(hexcode, datasize):
	const.FLAG_OPFETCH_EXECUTED = True
	if(armdebug.pipelineStages[2] != '--------'):
		return
	
	#flags = hexcode[28:32]
	operandRegister1 = utilFunc.getRegKeyByStringKey(hexcode[22:27])
	operandRegister2 = utilFunc.getRegKeyByStringKey(hexcode[11:16])
	
	if(mem.regObsolete[operandRegister1] == 0 and mem.regObsolete[operandRegister2] == 0):
		const.FLAG_OP_FETCHED = True
		regValue1 = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')
		regValue2 = utilFunc.getRegValueByStringkey(hexcode[11:16],'0')
		armdebug.intRFActivityCounter += 2
	elif(const.FLAG_DATA_FORWARDING):
		forwardedValues = mem.findForwardedValues(operandRegister1, operandRegister2)
		if(forwardedValues[0] == None and mem.regObsolete[operandRegister1] != 0):
			return
		if(forwardedValues[1] == None and mem.regObsolete[operandRegister2] != 0):
			return
		const.FLAG_OP_FETCHED = True
		regValue1 = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')
		regValue2 = utilFunc.getRegValueByStringkey(hexcode[11:16],'0')
		if(forwardedValues[0] != None):
			regValue1 = forwardedValues[0]
		if(forwardedValues[1] != None):
			regValue2 = forwardedValues[1]
		if(None in forwardedValues):
			armdebug.intRFActivityCounter += 1
	else:
		return

	#condition = hexcode[16:20]

	#regValue1 = utilFunc.getRegValueByStringkey(hexcode[22:27], 0)
	#regValue2 = utilFunc.getRegValueByStringkey(hexcode[11:16], 0)

	if(datasize == 32):
		registerType = "w"
		regValue1 = regValue1[32:64]
		regValue2 = regValue2[32:64]
	else:
		datasize = "x"

	mem.operand1Buffer = regValue1
	mem.operand2Buffer = regValue2