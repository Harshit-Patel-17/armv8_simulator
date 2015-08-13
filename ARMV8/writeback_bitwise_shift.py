#author swarnadeep

import utilFunc
import mem
import const

def writebackBitwiseShift_32(hexcode):
	executeBitwiseShiftRegister(hexcode, 32, 0)

def writebackBitwiseShift_64(hexcode):
	executeBitwiseShiftRegister(hexcode, 64, 0)

def writebackBitwiseShiftSetFlags_32(hexcode):
	executeBitwiseShiftRegister(hexcode, 32, 1)

def writebackBitwiseShiftSetFlags_64(hexcode):
	executeBitwiseShiftRegister(hexcode, 64, 1)

def executeBitwiseShiftRegister(hexcode, datasize, setFlags):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	
	utilFunc.setRegValue(destRegister, mem.writeBackBuffer[0], '0')
	const.FLAG_WRITEBACK_COMPLETED = True
	const.FLAG_WRITEBACK_EXECUTED = True
	mem.regObsolete[destRegister] = False