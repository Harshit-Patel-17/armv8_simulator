#author swarnadeep

import utilFunc
import const

#CRC checksum with second source operand being 8 bits
def executeCRC32B(hexcode):
	executeCRCChecksum(hexcode, "CRC32B", 8)

#CRC checksum with second source operand being 16 bits
def executeCRC32H(hexcode):
	executeCRCChecksum(hexcode, "CRC32H", 16)

#CRC checksum with second source operand being 32 bits
def executeCRC32W(hexcode):
	executeCRCChecksum(hexcode, "CRC32W", 32)

#utility function to calculate the CRC checksum
def executeCRCChecksum(hexcode, command, inputSize):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	operandRegister1 = utilFunc.getRegKeyByStringKey(hexcode[22:27])
	operandRegister2 = utilFunc.getRegKeyByStringKey(hexcode[11:16])

	accumulator = utilFunc.getRegValueByStringkey(hexcode[22:27],'1')
	value = utilFunc.getRegValueByStringkey(hexcode[11:16],'1')

	tempAccumulator = utilFunc.negate(accumulator).zfill(32+inputSize)
	tempValue = utilFunc.negate(value).zfill(32+size)

	xorValue = utilFunc.calculateXor(tempAccumulator, tempValue)

	for i in range((31+inputSize), 31, -1):
		if(xorValue[i] == '1'):
			xorValue[0:(i+1)] = utilFunc.calculateXor(xorValue[0:(i+1)],const.CRC_Polynomial.zfill(i+1))

	answer = xorValue[0:32]

	instruction = command + "x" + str(destRegister) + ", w" + str(operandRegister1) + ", w" + str(operandRegister2)

	utilFunc.finalize(destRegister, answer, instruction, '1')
