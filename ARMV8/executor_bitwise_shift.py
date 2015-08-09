#author swarnadeep

import utilFunc
import mem
import const

def execBitwiseShift_32(hexcode):
	executeBitwiseShiftRegister(hexcode, 32, 0)

def execBitwiseShift_64(hexcode):
	executeBitwiseShiftRegister(hexcode, 64, 0)

def execBitwiseShiftSetFlags_32(hexcode):
	executeBitwiseShiftRegister(hexcode, 32, 1)

def execBitwiseShiftSetFlags_64(hexcode):
	executeBitwiseShiftRegister(hexcode, 64, 1)

def executeBitwiseShiftRegister(hexcode, datasize, setFlags):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])

	shiftAmountBinary = hexcode[16:22]
	shiftAmount =int(shiftAmountBinary, 2)

	shiftType = hexcode[8:10]

	if(shiftType == "00"): #LSL
		shiftedValue = utilFunc.lsl(mem.operand2Buffer, shiftAmount)
	elif(shiftType == "01"): #LSR
		shiftedValue = utilFunc.lsr(mem.operand2Buffer, shiftAmount)
	elif(shiftType == "10"): #ASR
		shiftedValue = utilFunc.asr(mem.operand2Buffer, shiftAmount)
	else: #ROR
		shiftedValue = utilFunc.ror(mem.operand2Buffer, shiftAmount)
		
	negatedShiftedValue = utilFunc.negate(shiftedValue)
	resultBinary = utilFunc.logical_and(mem.operand1Buffer, negatedShiftedValue)

	if(setFlags):
		flags = resultBinary[0] + utilFunc.isZero(resultBinary) + '00'
		utilFunc.setFlags(flags)
		command = "BICS "
	else:
		command = "BIC "

	resultBinary = resultBinary.zfill(64)

	mem.ALUResultBuffer = resultBinary
	mem.regValueAvailableInALU[destRegister] = True
	const.FLAG_INST_EXECUTED = True