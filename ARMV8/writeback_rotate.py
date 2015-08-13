#author swarnadeep

import utilFunc
import mem
import const

# immediate rotate 32 bit
def writebackRotate_i32(hexcode):
	execRotateImmediate(hexcode, 32)

#immediate rotate 64 bit
def writebackRotate_i64(hexcode):
	execRotateImmediate(hexcode, 64)

#register rotate 32 bit
def writebackRotate_r32(hexcode):
	execRotateRegister(hexcode, 32)

#register rotate 64 bit
def writebackRotate_r64(hexcode):
	execRotateRegister(hexcode, 64)

#utility function for rotation by an immediate value
def execRotateImmediate(hexcode, datasize):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])

	utilFunc.setRegValue(destRegister, mem.writeBackBuffer[0], '0')
	const.FLAG_WRITEBACK_COMPLETED = True
	const.FLAG_WRITEBACK_EXECUTED = True
	mem.regObsolete[destRegister] = False

#utility function for rotaton by a number stored in a register
def execRotateRegister(hexcode, datasize):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])

	utilFunc.setRegValue(destRegister, mem.writeBackBuffer[0], '0')
	const.FLAG_WRITEBACK_COMPLETED = True
	const.FLAG_WRITEBACK_EXECUTED = True
	mem.regObsolete[destRegister] = False