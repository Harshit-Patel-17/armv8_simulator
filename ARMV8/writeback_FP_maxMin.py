# author swarnadeep

import utilFunc
import const
import mem
import armdebug
import config

def writebackFMAX_scalar_SP(hexcode):
	executeFMAX_scalar(hexcode,1)

def writebackFMAX_scalar_DP(hexcode):
	executeFMAX_scalar(hexcode,2)

def writebackFMAX_vector_2S(hexcode):
	executeFMAX_vector(hexcode,0,0)

def writebackFMAX_vector_4S(hexcode):
	executeFMAX_vector(hexcode,1,0)

def writebackFMAX_vector_2D(hexcode):
	executeFMAX_vector(hexcode,1,1)

def writebackFMIN_scalar_SP(hexcode):
	executeFMIN_scalar(hexcode,1)

def writebackFMIN_scalar_DP(hexcode):
	executeFMIN_scalar(hexcode,2)

def writebackFMIN_vector_2S(hexcode):
	executeFMIN_vector(hexcode,0,0)

def writebackFMIN_vector_4S(hexcode):
	executeFMIN_vector(hexcode,1,0)

def writebackFMIN_vector_2D(hexcode):
	executeFMIN_vector(hexcode,1,1)

def executeFMAX_scalar(hexcode, precision):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])

	utilFunc.setRegValueSIMDFP(destRegister, mem.writeBackBuffer[0])
	armdebug.floatRFActivityCounter += 1
	const.FLAG_WRITEBACK_COMPLETED = True
	const.FLAG_WRITEBACK_EXECUTED = True
	mem.regFloatObsolete[destRegister] -= 1

def executeFMIN_scalar(hexcode, precision):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	
	utilFunc.setRegValueSIMDFP(destRegister, mem.writeBackBuffer[0])
	armdebug.floatRFActivityCounter += 1
	const.FLAG_WRITEBACK_COMPLETED = True
	const.FLAG_WRITEBACK_EXECUTED = True
	mem.regFloatObsolete[destRegister] -= 1
	