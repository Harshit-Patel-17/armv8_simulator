#author swarnadeep

import utilFunc
import mem
import const
import armdebug

# immediate rotate 32 bit
def opfetchRotate_i32(hexcode):
	execRotateImmediate(hexcode, 32)

#immediate rotate 64 bit
def opfetchRotate_i64(hexcode):
	execRotateImmediate(hexcode, 64)

#register rotate 32 bit
def opfetchRotate_r32(hexcode):
	execRotateRegister(hexcode, 32)

#register rotate 64 bit
def opfetchRotate_r64(hexcode):
	execRotateRegister(hexcode, 64)

#utility function for rotation by an immediate value
def execRotateImmediate(hexcode, datasize):
	const.FLAG_OPFETCH_EXECUTED = True
	if(armdebug.pipelineStages[2] != '--------'):
		return
	
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	operandRegister1 = utilFunc.getRegKeyByStringKey(hexcode[22:27])
	operandRegister2 = utilFunc.getRegKeyByStringKey(hexcode[11:16])
	
	assert operandRegister1 == operandRegister2
	
	if(mem.regObsolete[operandRegister1] == 0):
		const.FLAG_OP_FETCHED = True
		reg1Value = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')
		armdebug.intRFActivityCounter += 1
	elif(const.FLAG_DATA_FORWARDING):
		forwardedValues = mem.findForwardedValues(operandRegister1)
		if(forwardedValues[0] != None):
			const.FLAG_OP_FETCHED = True
			reg1Value = forwardedValues[0]
		else:
			return
	else:
		return
	
	mem.regObsolete[destRegister] += 1
	mem.regObsolete_last_modified_indices.append(destRegister)

	#reg1Value = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')

	if(datasize == 32):
		registerType = "w"
		reg1Value = reg1Value[32:64]
	else:
		registerType = "x"

	immediate = hexcode[16:22]
	immediate = int(immediate,2)
	
	mem.operand1Buffer = reg1Value
	mem.operand2Buffer = immediate

#utility function for rotaton by a number stored in a register
def execRotateRegister(hexcode, datasize):
	const.FLAG_OPFETCH_EXECUTED = True
	if(armdebug.pipelineStages[2] != '--------'):
		return
	
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	operandRegister1 = utilFunc.getRegKeyByStringKey(hexcode[22:27])
	operandRegister2 = utilFunc.getRegKeyByStringKey(hexcode[11:16])
	
	if(mem.regObsolete[operandRegister1] == 0 and mem.regObsolete[operandRegister2] == 0):
		const.FLAG_OP_FETCHED = True
		reg1Value = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')
		reg2Value = utilFunc.getRegValueByStringkey(hexcode[11:16],'0')
		armdebug.intRFActivityCounter += 2
	elif(const.FLAG_DATA_FORWARDING):
		forwardedValues = mem.findForwardedValues(operandRegister1, operandRegister2)
		if(forwardedValues[0] == None and mem.regObsolete[operandRegister1] != 0):
			return
		if(forwardedValues[1] == None and mem.regObsolete[operandRegister2] != 0):
			return
		const.FLAG_OP_FETCHED = True
		reg1Value = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')
		reg2Value = utilFunc.getRegValueByStringkey(hexcode[11:16],'0')
		if(forwardedValues[0] != None):
			reg1Value = forwardedValues[0]
		if(forwardedValues[1] != None):
			reg2Value = forwardedValues[1]
		if(None in forwardedValues):
			armdebug.intRFActivityCounter += 1
	else:
		return
	
	mem.regObsolete[destRegister] += 1
	mem.regObsolete_last_modified_indices.append(destRegister)

	#reg1Value = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')
	#reg2Value = utilFunc.getRegValueByStringkey(hexcode[11:16],'0')

	if(datasize == 32):
		registerType = "w"
		reg1Value = reg1Value[32:64]
		reg2Value = reg2Value[32:64]
	else:
		registerType = "x"

	mem.operand1Buffer = reg1Value
	mem.operand2Buffer = reg2Value