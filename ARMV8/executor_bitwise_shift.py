#author swarnadeep

import utilFunc

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
	operandRegister1 = utilFunc.getRegKeyByStringKey(hexcode[22:27])
	operandRegister2 = utilFunc.getRegKeyByStringKey(hexcode[11:16])

	reg1Value = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')
	reg2Value = utilFunc.getRegValueByStringkey(hexcode[11:16],'0')

	shiftAmountBinary = binary[16:22]
	shiftAmount =int(shiftAmountBinary, 2)

	shiftType = binary[8:10]

	if(datasize == 32):
		registerType = "w"
		reg1Value = reg1Value[32:64]
		reg2Value = reg2Value[32:64]
	else:
		registerType = "x"

	if(shiftType == "00"): #LSL
		shiftedValue = utilFunc.lsl(reg2Value, shiftAmount)
	elif(shiftType == "01"): #LSR
		shiftedValue = utilFunc.lsr(reg2Value, shiftedValue)
	elif(shiftType == "10"): #ASR
		shiftedValue = utilFunc.asr(reg2Value, shiftedValue)
	else: #ROR
		shiftedValue = utilFunc.ror(reg2Value, shiftedValue)

	resultBinary = utilFunc.logical_and(reg1Value, shiftedValue)

	if(setFlags):
		utilFunc.setFlagsFromResult(resultBinary)
		command = "BICS "
	else:
		command = "BIC "

	resultBinary = resultBinary.zfill(64)

	instr = command + registerType + str(destRegister) + ", " + registerType + str(operandRegister1) + ", " + registerType + str(operandRegister2) + shiftType + str(shiftAmount)

	utilFunc.finalize(destRegister, resultBinary, instr, '0')