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

#executes conditional compare negative immediate for 32 bit registers
def memaccessConditionalCompareNegative_i32(hexcode):
	execConditionalCompareNegativeImmediate(hexcode, 32)

#executes conditional compare negative immediate for 64 bit registers
def memaccessConditionalCompareNegative_i64(hexcode):
	execConditionalCompareNegativeImmediate(hexcode, 64)

#executes conditional compare negative register for 32 bits
def memaccessConditionalCompareNegative_r32(hexcode):
	execConditionalCompareNegativeRegister(hexcode, 32)

#executes conditional compare negative register for 64 bits
def memaccessConditionalCompareNegative_r64(hexcode):
	execConditionalCompareNegativeRegister(hexcode, 64)

#utility function for conditional set
def executeConditionalSet(hexcode, datasize):
	const.FLAG_MEMACCESS_EXECUTED = True    
	const.FLAG_MEMACCESS_COMPLETED = True
	if(armdebug.pipelineStages[4] != '--------'):
		return

	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])

	mem.writeBackBuffer[0] = mem.ALUResultBuffer
	mem.regValueAvailableInWB[destRegister] = True
	mem.regValueAvailableInWB_buffer_indices[destRegister] = 0
	mem.isSPWriteBackBuffer = mem.isSPBuffer
	#const.FLAG_MEMACCESS_EXECUTED = True
	#const.FLAG_MEMACCESS_COMPLETED = True

#utility function for conditional select inverse
def executeConditionalSelectInverse(hexcode, datasize):
	const.FLAG_MEMACCESS_EXECUTED = True    
	const.FLAG_MEMACCESS_COMPLETED = True
	if(armdebug.pipelineStages[4] != '--------'):
		return

	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])

	mem.writeBackBuffer[0] = mem.ALUResultBuffer
	mem.regValueAvailableInWB[destRegister] = True
	mem.regValueAvailableInWB_buffer_indices[destRegister] = 0
	mem.isSPWriteBackBuffer = mem.isSPBuffer
	#const.FLAG_MEMACCESS_EXECUTED = True
	#const.FLAG_MEMACCESS_COMPLETED = True


#utility function for conditional select negate
def executeConditionalSelectNegate(hexcode, datasize):
	const.FLAG_MEMACCESS_EXECUTED = True    
	const.FLAG_MEMACCESS_COMPLETED = True
	if(armdebug.pipelineStages[4] != '--------'):
		return

	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])

	mem.writeBackBuffer[0] = mem.ALUResultBuffer
	mem.regValueAvailableInWB[destRegister] = True
	mem.regValueAvailableInWB_buffer_indices[destRegister] = 0
	mem.isSPWriteBackBuffer = mem.isSPBuffer
	#const.FLAG_MEMACCESS_EXECUTED = True
	#const.FLAG_MEMACCESS_COMPLETED = True

#utility function for conditional select increment
def executeConditionalSelectIncrement(hexcode, datasize):
	const.FLAG_MEMACCESS_EXECUTED = True    
	const.FLAG_MEMACCESS_COMPLETED = True
	if(armdebug.pipelineStages[4] != '--------'):
		return

	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	mem.writeBackBuffer[0] = mem.ALUResultBuffer
	mem.regValueAvailableInWB[destRegister] = True
	mem.regValueAvailableInWB_buffer_indices[destRegister] = 0
	mem.isSPWriteBackBuffer = mem.isSPBuffer
	#const.FLAG_MEMACCESS_EXECUTED = True
	#const.FLAG_MEMACCESS_COMPLETED = True


#utility function for conditional compare negative immediate
def execConditionalCompareNegativeImmediate(hexcode, datasize):
	const.FLAG_MEMACCESS_EXECUTED = True    
	const.FLAG_MEMACCESS_COMPLETED = True
	if(armdebug.pipelineStages[4] != '--------'):
		return

	mem.writeBackBuffer[0] = mem.ALUResultBuffer
	mem.isSPWriteBackBuffer = mem.isSPBuffer
	#const.FLAG_MEMACCESS_EXECUTED = True
	#const.FLAG_MEMACCESS_COMPLETED = True

#utility function for conditional compare negative register
def execConditionalCompareNegativeRegister(hexcode, datasize):
	const.FLAG_MEMACCESS_EXECUTED = True    
	const.FLAG_MEMACCESS_COMPLETED = True
	if(armdebug.pipelineStages[4] != '--------'):
		return

	mem.writeBackBuffer[0] = mem.ALUResultBuffer
	mem.isSPWriteBackBuffer = mem.isSPBuffer
	#const.FLAG_MEMACCESS_EXECUTED = True
	#const.FLAG_MEMACCESS_COMPLETED = True
