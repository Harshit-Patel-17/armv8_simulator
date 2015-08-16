# author swarnadeep

import utilFunc
import const
import mem
import armdebug

# executes Move Wide with Keep for 32 bits
def writebackMoveK_32(hexcode):
	executeMoveWideWithKeep(hexcode,32)

# executes Move Wide with Keep for 64 bits
def writebackMoveK_64(hexcode):
	executeMoveWideWithKeep(hexcode,64)

# executes Move Wide with Not for 32 bits
def writebackMoveN_32(hexcode):
	executeMoveWideWithNot(hexcode, 32)

# executes Move Wide with Not for 64 bits
def writebackMoveN_64(hexcode):
	executeMoveWideWithNot(hexcode, 64)

# executes Move Wide with Zero for 32 bits
def writebackMoveZ_32(hexcode):
	executeMoveWideWithZero(hexcode, 32)

# executes Move Wide with Zero for 64 bits
def writebackMoveZ_64(hexcode):
	executeMoveWideWithZero(hexcode, 64)

# utility function for Move Wide with Keep
def executeMoveWideWithKeep(hexcode, datasize):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	
	utilFunc.setRegValue(destRegister, mem.writeBackBuffer[0], '0')
	armdebug.intRFActivityCounter += 1
	const.FLAG_WRITEBACK_COMPLETED = True
	const.FLAG_WRITEBACK_EXECUTED = True
	mem.regObsolete[destRegister] -= 1

# utility function for Move Wide with Not
def executeMoveWideWithNot(hexcode, datasize):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	
	utilFunc.setRegValue(destRegister, mem.writeBackBuffer[0], '0')
	armdebug.intRFActivityCounter += 1
	const.FLAG_WRITEBACK_COMPLETED = True
	const.FLAG_WRITEBACK_EXECUTED = True
	mem.regObsolete[destRegister] -= 1

# utility function for Move Wide with Zero
def executeMoveWideWithZero(hexcode, datasize):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	
	utilFunc.setRegValue(destRegister, mem.writeBackBuffer[0], '0')
	armdebug.intRFActivityCounter += 1
	const.FLAG_WRITEBACK_COMPLETED = True
	const.FLAG_WRITEBACK_EXECUTED = True
	mem.regObsolete[destRegister] -= 1