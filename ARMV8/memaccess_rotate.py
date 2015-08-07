#author swarnadeep

import utilFunc
import mem
import const

# immediate rotate 32 bit
def memaccessRotate_i32(hexcode):
	execRotateImmediate(hexcode, 32)

#immediate rotate 64 bit
def memaccessRotate_i64(hexcode):
	execRotateImmediate(hexcode, 64)

#register rotate 32 bit
def memaccessRotate_r32(hexcode):
	execRotateRegister(hexcode, 32)

#register rotate 64 bit
def memaccessRotate_r64(hexcode):
	execRotateRegister(hexcode, 64)

#utility function for rotation by an immediate value
def execRotateImmediate(hexcode, datasize):
	'''
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	operandRegister1 = utilFunc.getRegKeyByStringKey(hexcode[22:27])
	operandRegister2 = utilFunc.getRegKeyByStringKey(hexcode[11:16])

	reg1Value = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')
	reg2Value = utilFunc.getRegValueByStringkey(hexcode[11:16],'0')

	if(datasize == 32):
		registerType = "w"
		reg1Value = reg1Value[32:64]
		reg2Value = reg2Value[32:64]
	else:
		registerType = "x"

	assert reg1Value == reg2Value

	immediate = hexcode[16:22]
	immediate = int(immediate,2)
	resultBinary = utilFunc.rotateRightByBits(reg1Value,immediate,datasize)

	instruction = "ROR " + registerType + str(destRegister) + ", " + registerType + str(operandRegister1) + ", #" + str(immediate)
	utilFunc.finalize(destRegister, resultBinary, instruction, '1')
	'''
	mem.writeBackBuffer[0] = mem.ALUResultBuffer
	mem.isSPWriteBackBuffer = mem.isSPBuffer
	const.FLAG_MEMACCESS_EXECUTED = True

#utility function for rotaton by a number stored in a register
def execRotateRegister(hexcode, datasize):
	'''
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	operandRegister1 = utilFunc.getRegKeyByStringKey(hexcode[22:27])
	operandRegister2 = utilFunc.getRegKeyByStringKey(hexcode[11:16])

	reg1Value = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')
	reg2Value = utilFunc.getRegValueByStringkey(hexcode[11:16],'0')

	if(datasize == 32):
		registerType = "w"
		reg1Value = reg1Value[32:64]
		reg2Value = reg2Value[32:64]
	else:
		registerType = "x"

	bitsToBeRotated = int(reg2Value,2) % datasize

	resultBinary = utilFunc.rotateRightByBits(reg1Value,bitsToBeRotated,datasize)

	instruction = "ROR " + registerType + str(destRegister) + ", " + registerType + str(operandRegister1) + ", " + registerType + str(operandRegister2)
	utilFunc.finalize(destRegister, resultBinary, instruction, '1')
	'''
	mem.writeBackBuffer[0] = mem.ALUResultBuffer
	mem.isSPWriteBackBuffer = mem.isSPBuffer
	const.FLAG_MEMACCESS_EXECUTED = True