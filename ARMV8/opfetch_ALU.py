#author swarnadeep

import utilFunc
import const
import mem
import armdebug

#executes CLS instruction(32 bit) 
def opfetchCLS_32(hexcode):
	executeCLS(hexcode, 32)

#executes CLS instruction(64 bit)
def opfetchCLS_64(hexcode):
	executeCLS(hexcode, 64)

#executes CLZ instruction(32 bit)
def opfetchCLZ_32(hexcode):
	executeCLZ(hexcode,32)

#executes CLZ instruction(64 bit)
def opfetchCLZ_64(hexcode):
	executeCLZ(hexcode,64)

#utility function for counting the number of leading sign bits
def executeCLS(hexcode, datasize):
	const.FLAG_OPFETCH_EXECUTED = True
	if(armdebug.pipelineStages[2] != '--------'):
		return
	
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	operandRegister = utilFunc.getRegKeyByStringKey(hexcode[22:27])
	
	if(mem.regObsolete[operandRegister] == 0):
		const.FLAG_OP_FETCHED = True
		regValue = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')
		armdebug.intRFActivityCounter += 1
	elif(const.FLAG_DATA_FORWARDING):
		forwardedValues = mem.findForwardedValues(operandRegister)
		if(forwardedValues[0] != None):
			const.FLAG_OP_FETCHED = True
			regValue = forwardedValues[0]
		else:
			return
	else:
		return

	mem.regObsolete[destRegister] += 1
	mem.regObsolete_last_modified_indices.append(destRegister)

	#regValue = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')
	
	if(datasize == 32):
		registerType = "w"
		regValue = regValue[32:64]
	else:
		registerType = "x"
		
	mem.operand1Buffer = regValue

#utility function for counting the number of leading zero bits
def executeCLZ(hexcode, datasize):
	const.FLAG_OPFETCH_EXECUTED = True
	if(armdebug.pipelineStages[2] != '--------'):
		return
	
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	operandRegister = utilFunc.getRegKeyByStringKey(hexcode[22:27])
	
	if(mem.regObsolete[operandRegister] == 0):
		const.FLAG_OP_FETCHED = True
		regValue = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')
		armdebug.intRFActivityCounter += 1
	elif(const.FLAG_DATA_FORWARDING):
		forwardedValues = mem.findForwardedValues(operandRegister)
		if(forwardedValues[0] != None):
			const.FLAG_OP_FETCHED = True
			regValue = forwardedValues[0]
		else:
			return
	else:
		return

	mem.regObsolete[destRegister] += 1
	mem.regObsolete_last_modified_indices.append(destRegister)

	#regValue = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')
	
	if(datasize == 32):
		registerType = "w"
		regValue = regValue[32:64]
	else:
		registerType = "x"
		
	mem.operand1Buffer = regValue