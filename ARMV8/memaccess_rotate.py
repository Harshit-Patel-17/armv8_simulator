#author swarnadeep

import utilFunc
import mem
import const
import armdebug

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

#utility function for rotaton by a number stored in a register
def execRotateRegister(hexcode, datasize):
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