# author swarnadeep

import utilFunc

# executes Move Wide with Keep for 32 bits
def execMoveK_32(hexcode):
	executeMoveWideWithKeep(hexcode,32)

# executes Move Wide with Keep for 64 bits
def execMoveK_64(hexcode):
	executeMoveWideWithKeep(hexcode,64)

# executes Move Wide with Not for 32 bits
def execMoveN_32(hexcode):
	executeMoveWideWithNot(hexcode, 32)

# executes Move Wide with Not for 64 bits
def execMoveN_64(hexcode):
	executeMoveWideWithNot(hexcode, 64)

# executes Move Wide with Zero for 32 bits
def execMoveN_32(hexcode):
	executeMoveWideWithZero(hexcode, 32)

# executes Move Wide with Zero for 64 bits
def execMoveN_64(hexcode):
	executeMoveWideWithZero(hexcode, 64)

# utility function for Move Wide with Keep
def executeMoveWideWithKeep(hexcode, datasize):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	immediate = binary[11:27]

	position = binary[9:11]
	position = int(position, 2)*16

	destRegisterValue = utilFunc.getRegValueByStringkey(hexcode[27:32],'0')

	if(datasize == 32):
		destRegisterValue = destRegisterValue[32:64]

	destRegisterValue = destRegisterValue[0:(datasize-position-16)] + immediate + destRegisterValue[(datasize-position):datasize]

	utilFunc.setRegValue(destRegister, destRegisterValue, '0')

# utility function for Move Wide with Not
def executeMoveWideWithNot(hexcode, datasize):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	immediate = binary[11:27]

	position = binary[9:11]
	position = int(position, 2)*16

	resultBinary = "0"*datasize

	resultBinary = resultBinary[0:(datasize-position-16)] + immediate + resultBinary[(datasize-position):datasize]

	resultBinary = utilFunc.negate(resultBinary)

	utilFunc.setRegValue(destRegister, resultBinary, '0')

# utility function for Move Wide with Zero
def executeMoveWideWithNot(hexcode, datasize):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	immediate = binary[11:27]

	position = binary[9:11]
	position = int(position, 2)*16

	resultBinary = "0"*datasize

	resultBinary = resultBinary[0:(datasize-position-16)] + immediate + resultBinary[(datasize-position):datasize]

	utilFunc.setRegValue(destRegister, resultBinary, '0')