#author swarnadeep

import utilFunc
import mem
import const

#executes add with carry for 32 bits
def writebackADC_32(hexcode):
	execADC(hexcode, 32)

#executes add with carry for 64 bits
def writebackADC_64(hexcode):
	execADC(hexcode, 64)

#utility function for adding with carry
def execADC(hexcode, datasize):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])

	utilFunc.setRegValue(destRegister, mem.writeBackBuffer[0], mem.isSPWriteBackBuffer)
	const.FLAG_WRITEBACK_EXECUTED = True
	mem.regObsolete[destRegister] = False
	#utilFunc.finalize(destRegister, resultBinary, "ADC", isSP)

