#author swarnadeep

import utilFunc
import mem
import const

def memaccessBitwiseShift_32(hexcode):
	executeBitwiseShiftRegister(hexcode, 32, 0)

def memaccessBitwiseShift_64(hexcode):
	executeBitwiseShiftRegister(hexcode, 64, 0)

def memaccessBitwiseShiftSetFlags_32(hexcode):
	executeBitwiseShiftRegister(hexcode, 32, 1)

def memaccessBitwiseShiftSetFlags_64(hexcode):
	executeBitwiseShiftRegister(hexcode, 64, 1)

def executeBitwiseShiftRegister(hexcode, datasize, setFlags):
	mem.writeBackBuffer[0] = mem.ALUResultBuffer
	mem.isSPWriteBackBuffer = mem.isSPBuffer
	const.FLAG_MEMACCESS_EXECUTED = True