#author swarnadeep

import utilFunc
import mem
import const
import armdebug

#executes CLS instruction(32 bit) 
def writebackCLS_32(hexcode):
	executeCLS(hexcode, 32)

#executes CLS instruction(64 bit)
def writebackCLS_64(hexcode):
	executeCLS(hexcode, 64)

#executes CLZ instruction(32 bit)
def writebackCLZ_32(hexcode):
	executeCLZ(hexcode,32)

#executes CLZ instruction(64 bit)
def writebackCLZ_64(hexcode):
	executeCLZ(hexcode,64)

#utility function for counting the number of leading sign bits
def executeCLS(hexcode, datasize):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])

	utilFunc.setRegValue(destRegister, mem.writeBackBuffer[0], '0')
	armdebug.intRFActivityCounter += 1
	const.FLAG_WRITEBACK_COMPLETED = True
	const.FLAG_WRITEBACK_EXECUTED = True
	mem.regObsolete[destRegister] -= 1

#utility function for counting the number of leading zero bits
def executeCLZ(hexcode, datasize):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])

	utilFunc.setRegValue(destRegister, mem.writeBackBuffer[0], '0')
	armdebug.intRFActivityCounter += 1
	const.FLAG_WRITEBACK_COMPLETED = True
	const.FLAG_WRITEBACK_EXECUTED = True
	mem.regObsolete[destRegister] -= 1
