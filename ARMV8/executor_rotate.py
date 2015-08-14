#author swarnadeep

import utilFunc
import mem
import const
import config
import armdebug

# immediate rotate 32 bit
def execRotate_i32(hexcode):
	execRotateImmediate(hexcode, 32)

#immediate rotate 64 bit
def execRotate_i64(hexcode):
	execRotateImmediate(hexcode, 64)

#register rotate 32 bit
def execRotate_r32(hexcode):
	execRotateRegister(hexcode, 32)

#register rotate 64 bit
def execRotate_r64(hexcode):
	execRotateRegister(hexcode, 64)

#utility function for rotation by an immediate value
def execRotateImmediate(hexcode, datasize):
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

	resultBinary = utilFunc.rotateRightByBits(mem.operand1Buffer,mem.operand2Buffer,datasize)
	mem.ALUResultBuffer = resultBinary.zfill(const.REG_SIZE)
	mem.regValueAvailableInALU[destRegister] = True
	#const.FLAG_INST_EXECUTED = True

#utility function for rotaton by a number stored in a register
def execRotateRegister(hexcode, datasize):
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
	
	bitsToBeRotated = int(mem.operand2Buffer,2) % datasize

	resultBinary = utilFunc.rotateRightByBits(mem.operand1Buffer,bitsToBeRotated,datasize)
	mem.ALUResultBuffer = resultBinary.zfill(const.REG_SIZE)
	mem.regValueAvailableInALU[destRegister] = True
	#const.FLAG_INST_EXECUTED = True