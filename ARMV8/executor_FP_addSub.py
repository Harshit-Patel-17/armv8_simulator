# author swarnadeep
import utilFunc
import const
import mem
import armdebug
import config

# executes floating point scalar addition for single precision
def execFADD_scalar_SP(hexcode):
	executeFADD_scalar(hexcode, 1)

# executes floating point scalar addition for single precision
def execFADD_scalar_DP(hexcode):
	executeFADD_scalar(hexcode, 2)

# executes floating point vector addition for two 32 bit FPs stored in each 64 bit registers
def execFADD_vector_2S(hexcode):
	executeFADD_vector(hexcode,0,0)

# executes floating point vector addition for four 32 bit FPs stored in each 128 bit registers
def execFADD_vector_4S(hexcode):
	executeFADD_vector(hexcode,1,0)

# executes floating point vector addition for two 64 bit FPs stored in each 128 bit registers
def execFADD_vector_2D(hexcode):
	executeFADD_vector(hexcode,1,1)

# executes floating point scalar subtraction for single precision
def execFSUB_scalar_SP(hexcode):
	executeFSUB_scalar(hexcode,1)

# executes floating point scalar subtraction for double precision
def execFSUB_scalar_DP(hexcode):
	executeFSUB_scalar(hexcode,2)

# executes floating point vector subtraction for two 32 bit FPs stored in each 64 bit registers
def execFSUB_vector_2S(hexcode):
	executeFSUB_vector(hexcode,0,0)

# executes floating point vector subtraction for four 32 bit FPs stored in each 128 bit registers
def execFSUB_vector_4S(hexcode):
	executeFSUB_vector(hexcode,1,0)

# executes floating point vector subtraction for two 64 bit FPs stored in each 128 bit registers
def execFSUB_vector_2D(hexcode):
	executeFSUB_vector(hexcode,1,1)

# utility function for floating point scalar addition
def executeFADD_scalar(hexcode, precision):
	const.FLAG_INST_EXECUTED = True	
	if(const.FLAG_EXECUTION_COMPLETED == False and const.EXECUTION_COUNTER == 0):
		const.EXECUTION_COUNTER = config.latency['FloatALU']
	
	if(const.EXECUTION_COUNTER != 0):
		armdebug.floatALUActivityCounter += 1
		const.EXECUTION_COUNTER -= 1
		
	if(const.EXECUTION_COUNTER == 0):
		const.FLAG_EXECUTION_COMPLETED = True
		if(armdebug.pipelineStages[3] != '--------'):
			return
	else:
		return
	
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	
	if(precision == 1):
		datasize = 32
	else:
		datasize = 64

	resultBinary = utilFunc.addFP(mem.operand1Buffer,mem.operand2Buffer, datasize)
	mem.ALUResultBuffer = resultBinary.zfill(128)
	mem.regValueAvailableInFloatALU[destRegister] = True
	const.FLAG_INST_EXECUTED = True
	
# utility function for floating point scalar subtraction
def executeFSUB_scalar(hexcode, precision):
	const.FLAG_INST_EXECUTED = True	
	if(const.FLAG_EXECUTION_COMPLETED == False and const.EXECUTION_COUNTER == 0):
		const.EXECUTION_COUNTER = config.latency['FloatALU']
	
	if(const.EXECUTION_COUNTER != 0):
		armdebug.floatALUActivityCounter += 1
		const.EXECUTION_COUNTER -= 1
		
	if(const.EXECUTION_COUNTER == 0):
		const.FLAG_EXECUTION_COMPLETED = True
		if(armdebug.pipelineStages[3] != '--------'):
			return
	else:
		return
	
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])

	if(precision == 1):
		datasize =32
	else:
		datasize = 64

	resultBinary = utilFunc.subFP(mem.operand1Buffer,mem.operand2Buffer, datasize)
	mem.ALUResultBuffer = resultBinary.zfill(128)
	mem.regValueAvailableInFloatALU[destRegister] = True
	const.FLAG_INST_EXECUTED = True

# utility function for floating point vector addition
def executeFADD_vector(hexcode, Q, size):
	esize = 32<<size
	if(Q == 1):
		datasize = 128
	else:
		datasize = 64

	elements = datasize/esize
	
	const.FLAG_INST_EXECUTED = True	
	if(const.FLAG_EXECUTION_COMPLETED == False and const.EXECUTION_COUNTER == 0):
		const.EXECUTION_COUNTER = elements*config.latency['FloatALU']
	
	if(const.EXECUTION_COUNTER != 0):
		armdebug.floatALUActivityCounter += 1
		const.EXECUTION_COUNTER -= 1
		
	if(const.EXECUTION_COUNTER == 0):
		const.FLAG_EXECUTION_COMPLETED = True
		if(armdebug.pipelineStages[3] != '--------'):
			return
	else:
		return
	
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])

	resultBinary = ""
	
	if(elements == 2 and datasize == 64):
		mem.operand1Buffer = mem.operand1Buffer[64:128]
		mem.operand2Buffer = mem.operand2Buffer[64:128]

	for e in range(elements):
		element1 = mem.operand1Buffer[(e*esize):(e*esize + esize)]
		element2 = mem.operand2Buffer[(e*esize):(e*esize + esize)]
		resultBinary = resultBinary + utilFunc.addFP(element1, element2, esize)

	mem.ALUResultBuffer = resultBinary.zfill(128)
	mem.regValueAvailableInFloatALU[destRegister] = True

# utility function for floating point vector subtraction
def executeFSUB_vector(hexcode, Q, size):
	esize = 32<<size
	if(Q == 1):
		datasize = 128
	else:
		datasize = 64

	elements = datasize/esize
	
	const.FLAG_INST_EXECUTED = True	
	if(const.FLAG_EXECUTION_COMPLETED == False and const.EXECUTION_COUNTER == 0):
		const.EXECUTION_COUNTER = elements*config.latency['FloatALU']
	
	if(const.EXECUTION_COUNTER != 0):
		armdebug.floatALUActivityCounter += 1
		const.EXECUTION_COUNTER -= 1
		
	if(const.EXECUTION_COUNTER == 0):
		const.FLAG_EXECUTION_COMPLETED = True
		if(armdebug.pipelineStages[3] != '--------'):
			return
	else:
		return
	
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])

	resultBinary = ""
	
	if(elements == 2 and datasize == 64):
		mem.operand1Buffer = mem.operand1Buffer[64:128]
		mem.operand2Buffer = mem.operand2Buffer[64:128]

	for e in range(elements):
		element1 = mem.operand1Buffer[(e*esize):(e*esize + esize)]
		element2 = mem.operand2Buffer[(e*esize):(e*esize + esize)]
		resultBinary = resultBinary + utilFunc.subFP(element1, element2, esize)

	mem.ALUResultBuffer = resultBinary.zfill(128)
	mem.regValueAvailableInFloatALU[destRegister] = True

