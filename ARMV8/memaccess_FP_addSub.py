# author swarnadeep
import utilFunc
import const
import mem
import armdebug

# executes floating point scalar addition for single precision
def memaccessFADD_scalar_SP(hexcode):
	executeFADD_scalar(hexcode, 1)

# executes floating point scalar addition for single precision
def memaccessFADD_scalar_DP(hexcode):
	executeFADD_scalar(hexcode, 2)

# executes floating point vector addition for two 32 bit FPs stored in each 64 bit registers
def memaccessFADD_vector_2S(hexcode):
	executeFADD_vector(hexcode,0,0)

# executes floating point vector addition for four 32 bit FPs stored in each 128 bit registers
def memaccessFADD_vector_4S(hexcode):
	executeFADD_vector(hexcode,0,1)

# executes floating point vector addition for two 64 bit FPs stored in each 128 bit registers
def memaccessFADD_vector_2D(hexcode):
	executeFADD_vector(hexcode,1,1)

# executes floating point scalar subtraction for single precision
def memaccessFSUB_scalar_SP(hexcode):
	executeFSUB_scalar(hexcode,1)

# executes floating point scalar subtraction for double precision
def memaccessFSUB_scalar_DP(hexcode):
	executeFSUB_scalar(hexcode,2)

# executes floating point vector subtraction for two 32 bit FPs stored in each 64 bit registers
def memaccessFSUB_vector_2S(hexcode):
	executeFSUB_vector(hexcode,0,0)

# executes floating point vector subtraction for four 32 bit FPs stored in each 128 bit registers
def memaccessFSUB_vector_4S(hexcode):
	executeFSUB_vector(hexcode,0,1)

# executes floating point vector subtraction for two 64 bit FPs stored in each 128 bit registers
def memaccessFSUB_vector_2D(hexcode):
	executeFSUB_vector(hexcode,1,1)

# utility function for floating point scalar addition
def executeFADD_scalar(hexcode, precision):
	const.FLAG_MEMACCESS_EXECUTED = True	
	const.FLAG_MEMACCESS_COMPLETED = True
	if(armdebug.pipelineStages[4] != '--------'):
		return
	
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	
	mem.writeBackBuffer[0] = mem.ALUResultBuffer
	mem.regValueAvailableInFloatWB[destRegister] = True
	mem.regValueAvailableInFloatWB_buffer_indices[destRegister] = 0
	mem.isSPWriteBackBuffer = mem.isSPBuffer

# utility function for floating point scalar subtraction
def executeFSUB_scalar(hexcode, precision):
	const.FLAG_MEMACCESS_EXECUTED = True	
	const.FLAG_MEMACCESS_COMPLETED = True
	if(armdebug.pipelineStages[4] != '--------'):
		return
	
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])

	mem.writeBackBuffer[0] = mem.ALUResultBuffer
	mem.regValueAvailableInFloatWB[destRegister] = True
	mem.regValueAvailableInFloatWB_buffer_indices[destRegister] = 0
	mem.isSPWriteBackBuffer = mem.isSPBuffer

# utility function for floating point vector addition
def executeFADD_vector(hexcode, Q, size):
	const.FLAG_MEMACCESS_EXECUTED = True	
	const.FLAG_MEMACCESS_COMPLETED = True
	if(armdebug.pipelineStages[4] != '--------'):
		return
	
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])

	mem.writeBackBuffer[0] = mem.ALUResultBuffer
	mem.regValueAvailableInFloatWB[destRegister] = True
	mem.regValueAvailableInFloatWB_buffer_indices[destRegister] = 0
	mem.isSPWriteBackBuffer = mem.isSPBuffer

# utility function for floating point vector subtraction
def executeFSUB_vector(hexcode, Q, size):
	const.FLAG_MEMACCESS_EXECUTED = True	
	const.FLAG_MEMACCESS_COMPLETED = True
	if(armdebug.pipelineStages[4] != '--------'):
		return
	
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])

	mem.writeBackBuffer[0] = mem.ALUResultBuffer
	mem.regValueAvailableInFloatWB[destRegister] = True
	mem.regValueAvailableInFloatWB_buffer_indices[destRegister] = 0
	mem.isSPWriteBackBuffer = mem.isSPBuffer


