# author swarnadeep

import utilFunc
import mem
import const
import armdebug

# executes Move Wide with Keep for 32 bits
def memaccessMoveK_32(hexcode):
	executeMoveWideWithKeep(hexcode,32)

# executes Move Wide with Keep for 64 bits
def memaccessMoveK_64(hexcode):
	executeMoveWideWithKeep(hexcode,64)

# executes Move Wide with Not for 32 bits
def memaccessMoveN_32(hexcode):
	executeMoveWideWithNot(hexcode, 32)

# executes Move Wide with Not for 64 bits
def memaccessMoveN_64(hexcode):
	executeMoveWideWithNot(hexcode, 64)

# executes Move Wide with Zero for 32 bits
def memaccessMoveZ_32(hexcode):
	executeMoveWideWithZero(hexcode, 32)

# executes Move Wide with Zero for 64 bits
def memaccessMoveZ_64(hexcode):
	executeMoveWideWithZero(hexcode, 64)

# utility function for Move Wide with Keep
def executeMoveWideWithKeep(hexcode, datasize):
	const.FLAG_MEMACCESS_EXECUTED = True    
	const.FLAG_MEMACCESS_COMPLETED = True
	if(armdebug.pipelineStages[4] != '--------'):
		return
	
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])

	mem.writeBackBuffer[0] = mem.ALUResultBuffer
	mem.regValueAvailableInWB[destRegister] = True
	mem.regValueAvailableInWB_buffer_indices[destRegister] = 0
	mem.isSPWriteBackBuffer = mem.isSPBuffer

# utility function for Move Wide with Not
def executeMoveWideWithNot(hexcode, datasize):
	const.FLAG_MEMACCESS_EXECUTED = True    
	const.FLAG_MEMACCESS_COMPLETED = True
	if(armdebug.pipelineStages[4] != '--------'):
		return
	
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	
	mem.writeBackBuffer[0] = mem.ALUResultBuffer
	mem.regValueAvailableInWB[destRegister] = True
	mem.regValueAvailableInWB_buffer_indices[destRegister] = 0
	mem.isSPWriteBackBuffer = mem.isSPBuffer

# utility function for Move Wide with Zero
def executeMoveWideWithZero(hexcode, datasize):
	const.FLAG_MEMACCESS_EXECUTED = True    
	const.FLAG_MEMACCESS_COMPLETED = True
	if(armdebug.pipelineStages[4] != '--------'):
		return
	
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	
	mem.writeBackBuffer[0] = mem.ALUResultBuffer
	mem.regValueAvailableInWB[destRegister] = True
	mem.regValueAvailableInWB_buffer_indices[destRegister] = 0
	mem.isSPWriteBackBuffer = mem.isSPBuffer