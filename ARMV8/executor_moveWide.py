# author swarnadeep

import utilFunc
import mem
import const
import armdebug
import config

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
def execMoveZ_32(hexcode):
	executeMoveWideWithZero(hexcode, 32)

# executes Move Wide with Zero for 64 bits
def execMoveZ_64(hexcode):
	executeMoveWideWithZero(hexcode, 64)

# utility function for Move Wide with Keep
def executeMoveWideWithKeep(hexcode, datasize):
	const.FLAG_INST_EXECUTED = True	
	if(const.FLAG_EXECUTION_COMPLETED == False and const.EXECUTION_COUNTER == 0):
		const.EXECUTION_COUNTER = config.latency['IntALU']
	
	if(const.EXECUTION_COUNTER != 0):
		armdebug.intALUActivityCounter += 1
		const.EXECUTION_COUNTER -= 1
		
	if(const.EXECUTION_COUNTER == 0):
		const.FLAG_EXECUTION_COMPLETED = True
		if(armdebug.pipelineStages[3] != '--------'):
			return
	else:
		return
	
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	immediate = hexcode[11:27]

	position = int(hexcode[9:11], 2)*16


	mem.ALUResultBuffer = mem.operand1Buffer[0:(datasize-position-16)] + immediate + mem.operand1Buffer[(datasize-position):datasize]
	mem.regValueAvailableInALU[destRegister] = True

# utility function for Move Wide with Not
def executeMoveWideWithNot(hexcode, datasize):
	const.FLAG_INST_EXECUTED = True	
	if(const.FLAG_EXECUTION_COMPLETED == False and const.EXECUTION_COUNTER == 0):
		const.EXECUTION_COUNTER = config.latency['IntALU']
	
	if(const.EXECUTION_COUNTER != 0):
		armdebug.intALUActivityCounter += 1
		const.EXECUTION_COUNTER -= 1
		
	if(const.EXECUTION_COUNTER == 0):
		const.FLAG_EXECUTION_COMPLETED = True
		if(armdebug.pipelineStages[3] != '--------'):
			return
	else:
		return
	
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	immediate = hexcode[11:27]

	position = int(hexcode[9:11], 2)*16

	resultBinary = "0"*datasize

	resultBinary = resultBinary[0:(datasize-position-16)] + immediate + resultBinary[(datasize-position):datasize]

	mem.ALUResultBuffer = utilFunc.negate(resultBinary)
	mem.regValueAvailableInALU[destRegister] = True

# utility function for Move Wide with Zero
def executeMoveWideWithZero(hexcode, datasize):
	const.FLAG_INST_EXECUTED = True	
	if(const.FLAG_EXECUTION_COMPLETED == False and const.EXECUTION_COUNTER == 0):
		const.EXECUTION_COUNTER = config.latency['IntALU']
	
	if(const.EXECUTION_COUNTER != 0):
		armdebug.intALUActivityCounter += 1
		const.EXECUTION_COUNTER -= 1
		
	if(const.EXECUTION_COUNTER == 0):
		const.FLAG_EXECUTION_COMPLETED = True
		if(armdebug.pipelineStages[3] != '--------'):
			return
	else:
		return
	
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	immediate = hexcode[11:27]

	position = int(hexcode[9:11], 2)*16

	resultBinary = "0"*datasize

	mem.ALUResultBuffer = resultBinary[0:(datasize-position-16)] + immediate + resultBinary[(datasize-position):datasize]
	mem.regValueAvailableInALU[destRegister] = True