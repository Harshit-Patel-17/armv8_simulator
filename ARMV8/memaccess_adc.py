#author swarnadeep

import utilFunc
import mem
import const
import config
import armdebug

#executes add with carry for 32 bits
def memaccessADC_32(hexcode):
	execADC(hexcode, 32)

#executes add with carry for 64 bits
def memaccessADC_64(hexcode):
	execADC(hexcode, 64)

#utility function for adding with carry
def execADC(hexcode, datasize):
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

