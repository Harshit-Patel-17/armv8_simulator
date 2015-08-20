# author swarnadeep

import utilFunc
import const
import mem
import armdebug
import config

def execFMAX_scalar_SP(hexcode):
	executeFMAX_scalar(hexcode,1)

def execFMAX_scalar_DP(hexcode):
	executeFMAX_scalar(hexcode,2)

def execFMAX_vector_2S(hexcode):
	executeFMAX_vector(hexcode,0,0)

def execFMAX_vector_4S(hexcode):
	executeFMAX_vector(hexcode,1,0)

def execFMAX_vector_2D(hexcode):
	executeFMAX_vector(hexcode,1,1)

def execFMIN_scalar_SP(hexcode):
	executeFMIN_scalar(hexcode,1)

def execFMIN_scalar_DP(hexcode):
	executeFMIN_scalar(hexcode,2)

def execFMIN_vector_2S(hexcode):
	executeFMIN_vector(hexcode,0,0)

def execFMIN_vector_4S(hexcode):
	executeFMIN_vector(hexcode,1,0)

def execFMIN_vector_2D(hexcode):
	executeFMIN_vector(hexcode,1,1)

def executeFMAX_scalar(hexcode, precision):
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

	resultBinary = utilFunc.maxFP(mem.operand1Buffer,mem.operand2Buffer, datasize)
	mem.ALUResultBuffer = resultBinary.zfill(128)
	mem.regValueAvailableInFloatALU[destRegister] = True
	const.FLAG_INST_EXECUTED = True

def executeFMIN_scalar(hexcode, precision):
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

	resultBinary = utilFunc.minFP(mem.operand1Buffer,mem.operand2Buffer, datasize)
	mem.ALUResultBuffer = resultBinary.zfill(128)
	mem.regValueAvailableInFloatALU[destRegister] = True
	const.FLAG_INST_EXECUTED = True

def executeFMAX_vector(hexcode, Q, size):
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
		resultBinary = resultBinary + utilFunc.maxFP(element1, element2, esize)

	mem.ALUResultBuffer = resultBinary.zfill(128)
	mem.regValueAvailableInFloatALU[destRegister] = True

def executeFMIN_vector(hexcode, Q, size):
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
		resultBinary = resultBinary + utilFunc.minFP(element1, element2, esize)

	mem.ALUResultBuffer = resultBinary.zfill(128)
	mem.regValueAvailableInFloatALU[destRegister] = True