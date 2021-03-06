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
def writebackConditionalSet_32(hexcode):
	executeConditionalSet(hexcode, 32)

#executes conditional set for 64 bit registers
def writebackConditionalSet_64(hexcode):
	executeConditionalSet(hexcode,64)

#executes select conditional inverse for 32 bit registers
def writebackConditionalSelectInverse_32(hexcode):
	executeConditionalSelectInverse(hexcode,32)

#executes select conditional inverse for 64 bit registers
def writebackConditionalSelectInverse_64(hexcode):
	executeConditionalSelectInverse(hexcode,64)

#executes select conditional negate for 64 bit registers
def writebackConditionalSelectNegation_32(hexcode):
	executeConditionalSelectNegate(hexcode,32)

#executes select conditional negate for 64 bit registers
def writebackConditionalSelectNegation_64(hexcode):
	executeConditionalSelectNegate(hexcode,64)

#executes conditional select increment for 32 bit registers
def writebackConditionalSelectIncrement_32(hexcode):
	executeConditionalSelectIncrement(hexcode,32)

#executes conditional select increment for 64 bit registers
def writebackConditionalSelectIncrement_64(hexcode):
	executeConditionalSelectIncrement(hexcode,64)

#executes conditional compare negative immediate for 32 bit registers
def writebackConditionalCompareNegative_i32(hexcode):
	execConditionalCompareNegativeImmediate(hexcode, 32)

#executes conditional compare negative immediate for 64 bit registers
def writebackConditionalCompareNegative_i64(hexcode):
	execConditionalCompareNegativeImmediate(hexcode, 64)

#executes conditional compare negative register for 32 bits
def writebackConditionalCompareNegative_r32(hexcode):
	execConditionalCompareNegativeRegister(hexcode, 32)

#executes conditional compare negative register for 64 bits
def writebackConditionalCompareNegative_r64(hexcode):
	execConditionalCompareNegativeRegister(hexcode, 64)

#utility function for conditional set
def executeConditionalSet(hexcode, datasize):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])

	utilFunc.setRegValue(destRegister, mem.writeBackBuffer[0], '0')
	armdebug.intRFActivityCounter += 1
	const.FLAG_WRITEBACK_COMPLETED = True
	const.FLAG_WRITEBACK_EXECUTED = True
	mem.regObsolete[destRegister] -= 1

#utility function for conditional select inverse
def executeConditionalSelectInverse(hexcode, datasize):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])

	utilFunc.setRegValue(destRegister, mem.writeBackBuffer[0], '0')
	armdebug.intRFActivityCounter += 1
	const.FLAG_WRITEBACK_COMPLETED = True
	const.FLAG_WRITEBACK_EXECUTED = True
	mem.regObsolete[destRegister] -= 1


#utility function for conditional select negate
def executeConditionalSelectNegate(hexcode, datasize):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])

	utilFunc.setRegValue(destRegister, mem.writeBackBuffer[0], '0')
	armdebug.intRFActivityCounter += 1
	const.FLAG_WRITEBACK_COMPLETED = True
	const.FLAG_WRITEBACK_EXECUTED = True
	mem.regObsolete[destRegister] -= 1


#utility function for conditional select increment
def executeConditionalSelectIncrement(hexcode, datasize):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	utilFunc.setRegValue(destRegister, mem.writeBackBuffer[0], mem.isSPWriteBackBuffer)
	armdebug.intRFActivityCounter += 1
	const.FLAG_WRITEBACK_COMPLETED = True
	const.FLAG_WRITEBACK_EXECUTED = True
	mem.regObsolete[destRegister] -= 1

#utility function for conditional compare negative immediate
def execConditionalCompareNegativeImmediate(hexcode, datasize):
	const.FLAG_WRITEBACK_COMPLETED = True
	const.FLAG_WRITEBACK_EXECUTED = True

#utility function for conditional compare negative register
def execConditionalCompareNegativeRegister(hexcode, datasize):
	const.FLAG_WRITEBACK_COMPLETED = True
	const.FLAG_WRITEBACK_EXECUTED = True
