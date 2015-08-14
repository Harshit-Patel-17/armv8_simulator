#author swarnadeep

import utilFunc
import mem
import const
import armdebug

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
	armdebug.intRFActivityCounter += 1
	const.FLAG_WRITEBACK_COMPLETED = True
	const.FLAG_WRITEBACK_EXECUTED = True
	mem.regObsolete[destRegister] -= 1
	#utilFunc.finalize(destRegister, resultBinary, "ADC", isSP)

