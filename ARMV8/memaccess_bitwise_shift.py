#author swarnadeep

import utilFunc
import mem
import const
import armdebug

def memaccessBitwiseShift_32(hexcode):
	executeBitwiseShiftRegister(hexcode, 32, 0)

def memaccessBitwiseShift_64(hexcode):
	executeBitwiseShiftRegister(hexcode, 64, 0)

def memaccessBitwiseShiftSetFlags_32(hexcode):
	executeBitwiseShiftRegister(hexcode, 32, 1)

def memaccessBitwiseShiftSetFlags_64(hexcode):
	executeBitwiseShiftRegister(hexcode, 64, 1)

def executeBitwiseShiftRegister(hexcode, datasize, setFlags):
	const.FLAG_MEMACCESS_EXECUTED = True    
	const.FLAG_MEMACCESS_COMPLETED = True
	if(armdebug.pipelineStages[4] != '--------'):
		return

	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	mem.writeBackBuffer[0] = mem.ALUResultBuffer
	mem.regValueAvailableInWB[destRegister] = True
	mem.regValueAvailableInWB_buffer_indices[destRegister] = 0
	mem.isSPWriteBackBuffer = mem.isSPBuffer
	const.FLAG_MEMACCESS_EXECUTED = True
	const.FLAG_MEMACCESS_COMPLETED = True