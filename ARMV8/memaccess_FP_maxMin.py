# author swarnadeep

import utilFunc
import const
import mem
import armdebug
import config

def memaccessFMAX_scalar_SP(hexcode):
	executeFMAX_scalar(hexcode,1)

def memaccessFMAX_scalar_DP(hexcode):
	executeFMAX_scalar(hexcode,2)

def memaccessFMAX_vector_2S(hexcode):
	executeFMAX_vector(hexcode,0,0)

def memaccessFMAX_vector_4S(hexcode):
	executeFMAX_vector(hexcode,1,0)

def memaccessFMAX_vector_2D(hexcode):
	executeFMAX_vector(hexcode,1,1)

def memaccessFMIN_scalar_SP(hexcode):
	executeFMIN_scalar(hexcode,1)

def memaccessFMIN_scalar_DP(hexcode):
	executeFMIN_scalar(hexcode,2)

def memaccessFMIN_vector_2S(hexcode):
	executeFMIN_vector(hexcode,0,0)

def memaccessFMIN_vector_4S(hexcode):
	executeFMIN_vector(hexcode,1,0)

def memaccessFMIN_vector_2D(hexcode):
	executeFMIN_vector(hexcode,1,1)

def executeFMAX_scalar(hexcode, precision):
	const.FLAG_MEMACCESS_EXECUTED = True	
	const.FLAG_MEMACCESS_COMPLETED = True
	if(armdebug.pipelineStages[4] != '--------'):
		return
	
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	
	mem.writeBackBuffer[0] = mem.ALUResultBuffer
	mem.regValueAvailableInFloatWB[destRegister] = True
	mem.regValueAvailableInFloatWB_buffer_indices[destRegister] = 0
	mem.isSPWriteBackBuffer = mem.isSPBuffer

def executeFMIN_scalar(hexcode, precision):
	const.FLAG_MEMACCESS_EXECUTED = True	
	const.FLAG_MEMACCESS_COMPLETED = True
	if(armdebug.pipelineStages[4] != '--------'):
		return
	
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])

	mem.writeBackBuffer[0] = mem.ALUResultBuffer
	mem.regValueAvailableInFloatWB[destRegister] = True
	mem.regValueAvailableInFloatWB_buffer_indices[destRegister] = 0
	mem.isSPWriteBackBuffer = mem.isSPBuffer

def executeFMAX_vector(hexcode, Q, size):
	const.FLAG_MEMACCESS_EXECUTED = True	
	const.FLAG_MEMACCESS_COMPLETED = True
	if(armdebug.pipelineStages[4] != '--------'):
		return
	
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])

	mem.writeBackBuffer[0] = mem.ALUResultBuffer
	mem.regValueAvailableInFloatWB[destRegister] = True
	mem.regValueAvailableInFloatWB_buffer_indices[destRegister] = 0
	mem.isSPWriteBackBuffer = mem.isSPBuffer

def executeFMIN_vector(hexcode, Q, size):
	const.FLAG_MEMACCESS_EXECUTED = True	
	const.FLAG_MEMACCESS_COMPLETED = True
	if(armdebug.pipelineStages[4] != '--------'):
		return
	
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])

	mem.writeBackBuffer[0] = mem.ALUResultBuffer
	mem.regValueAvailableInFloatWB[destRegister] = True
	mem.regValueAvailableInFloatWB_buffer_indices[destRegister] = 0
	mem.isSPWriteBackBuffer = mem.isSPBuffer
