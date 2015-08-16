# author swarnadeep
import utilFunc
import mem
import const
import armdebug

# executes floating point scalar addition for single precision
def writebackFADD_scalar_SP(hexcode):
	executeFADD_scalar(hexcode, 1)

# executes floating point scalar addition for single precision
def writebackFADD_scalar_DP(hexcode):
	executeFADD_scalar(hexcode, 2)

# executes floating point vector addition for two 32 bit FPs stored in each 64 bit registers
def writebackFADD_vector_2S(hexcode):
	executeFADD_vector(hexcode,0,0)

# executes floating point vector addition for four 32 bit FPs stored in each 128 bit registers
def writebackFADD_vector_4S(hexcode):
	executeFADD_vector(hexcode,0,1)

# executes floating point vector addition for two 64 bit FPs stored in each 128 bit registers
def writebackFADD_vector_2D(hexcode):
	executeFADD_vector(hexcode,1,1)

# executes floating point scalar subtraction for single precision
def writebackFSUB_scalar_SP(hexcode):
	executeFSUB_scalar(hexcode,1)

# executes floating point scalar subtraction for double precision
def writebackFSUB_scalar_DP(hexcode):
	executeFSUB_scalar(hexcode,2)

# executes floating point vector subtraction for two 32 bit FPs stored in each 64 bit registers
def writebackFSUB_vector_2S(hexcode):
	executeFSUB_vector(hexcode,0,0)

# executes floating point vector subtraction for four 32 bit FPs stored in each 128 bit registers
def writebackFSUB_vector_4S(hexcode):
	executeFSUB_vector(hexcode,0,1)

# executes floating point vector subtraction for two 64 bit FPs stored in each 128 bit registers
def writebackFSUB_vector_2D(hexcode):
	executeFSUB_vector(hexcode,1,1)

# utility function for floating point scalar addition
def executeFADD_scalar(hexcode, precision):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])

	utilFunc.setRegValueSIMDFP(destRegister, mem.writeBackBuffer[0])
	armdebug.floatRFActivityCounter += 1
	const.FLAG_WRITEBACK_COMPLETED = True
	const.FLAG_WRITEBACK_EXECUTED = True
	mem.regFloatObsolete[destRegister] -= 1

# utility function for floating point scalar subtraction
def executeFSUB_scalar(hexcode, precision):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	
	utilFunc.setRegValueSIMDFP(destRegister, mem.writeBackBuffer[0])
	armdebug.floatRFActivityCounter += 1
	const.FLAG_WRITEBACK_COMPLETED = True
	const.FLAG_WRITEBACK_EXECUTED = True
	mem.regFloatObsolete[destRegister] -= 1

# utility function for floating point vector addition
def executeFADD_vector(hexcode, Q, size):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	
	utilFunc.setRegValueSIMDFP(destRegister, mem.writeBackBuffer[0])
	armdebug.floatRFActivityCounter += 1
	const.FLAG_WRITEBACK_COMPLETED = True
	const.FLAG_WRITEBACK_EXECUTED = True
	mem.regFloatObsolete[destRegister] -= 1

# utility function for floating point vector subtraction
def executeFSUB_vector(hexcode, Q, size):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	
	utilFunc.setRegValueSIMDFP(destRegister, mem.writeBackBuffer[0])
	armdebug.floatRFActivityCounter += 1
	const.FLAG_WRITEBACK_COMPLETED = True
	const.FLAG_WRITEBACK_EXECUTED = True
	mem.regFloatObsolete[destRegister] -= 1


