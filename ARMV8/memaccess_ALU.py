#author swarnadeep

import utilFunc
import mem
import const
import armdebug

#executes CLS instruction(32 bit) 
def memaccessCLS_32(hexcode):
	executeCLS(hexcode, 32)

#executes CLS instruction(64 bit)
def memaccessCLS_64(hexcode):
	executeCLS(hexcode, 64)

#executes CLZ instruction(32 bit)
def memaccessCLZ_32(hexcode):
	executeCLZ(hexcode,32)

#executes CLZ instruction(64 bit)
def memaccessCLZ_64(hexcode):
	executeCLZ(hexcode,64)

#utility function for counting the number of leading sign bits
def executeCLS(hexcode, datasize):
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

#utility function for counting the number of leading zero bits
def executeCLZ(hexcode, datasize):
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
