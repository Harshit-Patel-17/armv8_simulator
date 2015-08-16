# author swarnadeep

import utilFunc
import mem
import const
import armdebug

# executes Move Wide with Keep for 32 bits
def opfetchMoveK_32(hexcode):
	executeMoveWideWithKeep(hexcode,32)

# executes Move Wide with Keep for 64 bits
def opfetchMoveK_64(hexcode):
	executeMoveWideWithKeep(hexcode,64)

# executes Move Wide with Not for 32 bits
def opfetchMoveN_32(hexcode):
	executeMoveWideWithNot(hexcode, 32)

# executes Move Wide with Not for 64 bits
def opfetchMoveN_64(hexcode):
	executeMoveWideWithNot(hexcode, 64)

# executes Move Wide with Zero for 32 bits
def opfetchMoveZ_32(hexcode):
	executeMoveWideWithZero(hexcode, 32)

# executes Move Wide with Zero for 64 bits
def opfetchMoveZ_64(hexcode):
	executeMoveWideWithZero(hexcode, 64)

# utility function for Move Wide with Keep
def executeMoveWideWithKeep(hexcode, datasize):
	const.FLAG_OPFETCH_EXECUTED = True
	if(armdebug.pipelineStages[2] != '--------'):
		return
	
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])

	if(mem.regObsolete[destRegister] == 0):
		const.FLAG_OP_FETCHED = True
		destRegisterValue = utilFunc.getRegValueByStringkey(hexcode[27:32],'0')
		armdebug.intRFActivityCounter += 1
	elif(const.FLAG_DATA_FORWARDING):
		forwardedValues = mem.findForwardedValues(destRegister)
		if(forwardedValues[0] != None):
			const.FLAG_OP_FETCHED = True
			destRegisterValue = forwardedValues[0]
		else:
			return
	else:
		return
	
	mem.regObsolete[destRegister] += 1
	mem.regObsolete_last_modified_indices.append(destRegister)
	
	if(datasize == 32):
		destRegisterValue = destRegisterValue[32:64]
	
	mem.operand1Buffer = destRegisterValue

# utility function for Move Wide with Not
def executeMoveWideWithNot(hexcode, datasize):
	const.FLAG_OPFETCH_EXECUTED = True
	if(armdebug.pipelineStages[2] != '--------'):
		return
	
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	
	const.FLAG_OP_FETCHED = True
	
	mem.regObsolete[destRegister] += 1
	mem.regObsolete_last_modified_indices.append(destRegister)

# utility function for Move Wide with Zero
def executeMoveWideWithZero(hexcode, datasize):
	const.FLAG_OPFETCH_EXECUTED = True
	if(armdebug.pipelineStages[2] != '--------'):
		return
	
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	
	const.FLAG_OP_FETCHED = True
	
	mem.regObsolete[destRegister] += 1
	mem.regObsolete_last_modified_indices.append(destRegister)