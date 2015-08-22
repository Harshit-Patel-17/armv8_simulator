# author swarnadeep
import utilFunc
import const
import mem
import armdebug

# executes floating point scalar addition for single precision
def opfetchFADD_scalar_SP(hexcode):
	executeFADD_scalar(hexcode, 1)

# executes floating point scalar addition for single precision
def opfetchFADD_scalar_DP(hexcode):
	executeFADD_scalar(hexcode, 2)

# executes floating point vector addition for two 32 bit FPs stored in each 64 bit registers
def opfetchFADD_vector_2S(hexcode):
	executeFADD_vector(hexcode,0,0)

# executes floating point vector addition for four 32 bit FPs stored in each 128 bit registers
def opfetchFADD_vector_4S(hexcode):
	executeFADD_vector(hexcode,0,1)

# executes floating point vector addition for two 64 bit FPs stored in each 128 bit registers
def opfetchFADD_vector_2D(hexcode):
	executeFADD_vector(hexcode,1,1)

# executes floating point scalar subtraction for single precision
def opfetchFSUB_scalar_SP(hexcode):
	executeFSUB_scalar(hexcode,1)

# executes floating point scalar subtraction for double precision
def opfetchFSUB_scalar_DP(hexcode):
	executeFSUB_scalar(hexcode,2)

# executes floating point vector subtraction for two 32 bit FPs stored in each 64 bit registers
def opfetchFSUB_vector_2S(hexcode):
	executeFSUB_vector(hexcode,0,0)

# executes floating point vector subtraction for four 32 bit FPs stored in each 128 bit registers
def opfetchFSUB_vector_4S(hexcode):
	executeFSUB_vector(hexcode,0,1)

# executes floating point vector subtraction for two 64 bit FPs stored in each 128 bit registers
def opfetchFSUB_vector_2D(hexcode):
	executeFSUB_vector(hexcode,1,1)

# utility function for floating point scalar addition
def executeFADD_scalar(hexcode, precision):
	const.FLAG_OPFETCH_EXECUTED = True
	if(armdebug.pipelineStages[2] != '--------'):
		return
	
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	operandRegister1 = utilFunc.getRegKeyByStringKey(hexcode[22:27])
	operandRegister2 = utilFunc.getRegKeyByStringKey(hexcode[11:16])
	
	if(mem.regFloatObsolete[operandRegister1] == 0 and mem.regFloatObsolete[operandRegister2] == 0):
		const.FLAG_OP_FETCHED = True
		reg1Value = utilFunc.getRegValueByStringkeyFPSIMD(hexcode[22:27])
		reg2Value = utilFunc.getRegValueByStringkeyFPSIMD(hexcode[11:16])
		armdebug.floatRFActivityCounter += 1
	elif(const.FLAG_DATA_FORWARDING):
		forwardedValues = mem.findForwardedFloatValues(operandRegister1, operandRegister2)
		if(forwardedValues[0] == None and mem.regFloatObsolete[operandRegister1] != 0):
			return
		if(forwardedValues[1] == None and mem.regFloatObsolete[operandRegister2] != 0):
			return
		const.FLAG_OP_FETCHED = True
		reg1Value = utilFunc.getRegValueByStringkeyFPSIMD(hexcode[22:27])
		reg2Value = utilFunc.getRegValueByStringkeyFPSIMD(hexcode[11:16])
		if(forwardedValues[0] != None):
			reg1Value = forwardedValues[0]
		if(forwardedValues[1] != None):
			reg2Value = forwardedValues[1]
		if(None in forwardedValues):
			armdebug.floatRFActivityCounter += 1
	else:
		return

	mem.regFloatObsolete[destRegister] += 1
	mem.regFloatObsolete_last_modified_indices.append(destRegister)
	#reg1Value = utilFunc.getRegValueByStringkeyFPSIMD(hexcode[22:27])
	#reg2Value = utilFunc.getRegValueByStringkeyFPSIMD(hexcode[11:16])

	if(precision == 1):
		reg1Value = reg1Value[96:128]
		reg2Value = reg2Value[96:128]
		datasize =32
	else:
		reg1Value = reg1Value[64:128]
		reg2Value = reg2Value[64:128]
		datasize = 64

	mem.operand1Buffer = reg1Value
	mem.operand2Buffer = reg2Value

# utility function for floating point scalar subtraction
def executeFSUB_scalar(hexcode, precision):
	const.FLAG_OPFETCH_EXECUTED = True
	if(armdebug.pipelineStages[2] != '--------'):
		return
	
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	operandRegister1 = utilFunc.getRegKeyByStringKey(hexcode[22:27])
	operandRegister2 = utilFunc.getRegKeyByStringKey(hexcode[11:16])
	
	if(mem.regFloatObsolete[operandRegister1] == 0 and mem.regFloatObsolete[operandRegister2] == 0):
		const.FLAG_OP_FETCHED = True
		reg1Value = utilFunc.getRegValueByStringkeyFPSIMD(hexcode[22:27])
		reg2Value = utilFunc.getRegValueByStringkeyFPSIMD(hexcode[11:16])
		armdebug.floatRFActivityCounter += 1
	elif(const.FLAG_DATA_FORWARDING):
		forwardedValues = mem.findForwardedFloatValues(operandRegister1, operandRegister2)
		if(forwardedValues[0] == None and mem.regFloatObsolete[operandRegister1] != 0):
			return
		if(forwardedValues[1] == None and mem.regFloatObsolete[operandRegister2] != 0):
			return
		const.FLAG_OP_FETCHED = True
		reg1Value = utilFunc.getRegValueByStringkeyFPSIMD(hexcode[22:27])
		reg2Value = utilFunc.getRegValueByStringkeyFPSIMD(hexcode[11:16])
		if(forwardedValues[0] != None):
			reg1Value = forwardedValues[0]
		if(forwardedValues[1] != None):
			reg2Value = forwardedValues[1]
		if(None in forwardedValues):
			armdebug.floatRFActivityCounter += 1
	else:
		return
	
	mem.regFloatObsolete[destRegister] += 1
	mem.regFloatObsolete_last_modified_indices.append(destRegister)
	#reg1Value = utilFunc.getRegValueByStringkeyFPSIMD(hexcode[22:27])
	#reg2Value = utilFunc.getRegValueByStringkeyFPSIMD(hexcode[11:16])

	if(precision == 1):
		reg1Value = reg1Value[96:128]
		reg2Value = reg2Value[96:128]
		datasize =32
	else:
		reg1Value = reg1Value[64:128]
		reg2Value = reg2Value[64:128]
		datasize = 64

	mem.operand1Buffer = reg1Value
	mem.operand2Buffer = reg2Value

# utility function for floating point vector addition
def executeFADD_vector(hexcode, Q, size):
	const.FLAG_OPFETCH_EXECUTED = True
	if(armdebug.pipelineStages[2] != '--------'):
		return
	
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	operandRegister1 = utilFunc.getRegKeyByStringKey(hexcode[22:27])
	operandRegister2 = utilFunc.getRegKeyByStringKey(hexcode[11:16])
	
	if(mem.regFloatObsolete[operandRegister1] == 0 and mem.regFloatObsolete[operandRegister2] == 0):
		const.FLAG_OP_FETCHED = True
		reg1Value = utilFunc.getRegValueByStringkeyFPSIMD(hexcode[22:27])
		reg2Value = utilFunc.getRegValueByStringkeyFPSIMD(hexcode[11:16])
		armdebug.floatRFActivityCounter += 1
	elif(const.FLAG_DATA_FORWARDING):
		forwardedValues = mem.findForwardedFloatValues(operandRegister1, operandRegister2)
		if(forwardedValues[0] == None and mem.regFloatObsolete[operandRegister1] != 0):
			return
		if(forwardedValues[1] == None and mem.regFloatObsolete[operandRegister2] != 0):
			return
		const.FLAG_OP_FETCHED = True
		reg1Value = utilFunc.getRegValueByStringkeyFPSIMD(hexcode[22:27])
		reg2Value = utilFunc.getRegValueByStringkeyFPSIMD(hexcode[11:16])
		if(forwardedValues[0] != None):
			reg1Value = forwardedValues[0]
		if(forwardedValues[1] != None):
			reg2Value = forwardedValues[1]
		if(None in forwardedValues):
			armdebug.floatRFActivityCounter += 1
	else:
		return
	
	mem.regFloatObsolete[destRegister] += 1
	mem.regFloatObsolete_last_modified_indices.append(destRegister)
	#reg1Value = utilFunc.getRegValueByStringkeyFPSIMD(hexcode[22:27])
	#reg2Value = utilFunc.getRegValueByStringkeyFPSIMD(hexcode[11:16])
	
	mem.operand1Buffer = reg1Value
	mem.operand2Buffer = reg2Value

# utility function for floating point vector subtraction
def executeFSUB_vector(hexcode, Q, size):
	const.FLAG_OPFETCH_EXECUTED = True
	if(armdebug.pipelineStages[2] != '--------'):
		return
	
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	operandRegister1 = utilFunc.getRegKeyByStringKey(hexcode[22:27])
	operandRegister2 = utilFunc.getRegKeyByStringKey(hexcode[11:16])
	
	if(mem.regFloatObsolete[operandRegister1] == 0 and mem.regFloatObsolete[operandRegister2] == 0):
		const.FLAG_OP_FETCHED = True
		reg1Value = utilFunc.getRegValueByStringkeyFPSIMD(hexcode[22:27])
		reg2Value = utilFunc.getRegValueByStringkeyFPSIMD(hexcode[11:16])
		armdebug.floatRFActivityCounter += 1
	elif(const.FLAG_DATA_FORWARDING):
		forwardedValues = mem.findForwardedFloatValues(operandRegister1, operandRegister2)
		if(forwardedValues[0] == None and mem.regFloatObsolete[operandRegister1] != 0):
			return
		if(forwardedValues[1] == None and mem.regFloatObsolete[operandRegister2] != 0):
			return
		const.FLAG_OP_FETCHED = True
		reg1Value = utilFunc.getRegValueByStringkeyFPSIMD(hexcode[22:27])
		reg2Value = utilFunc.getRegValueByStringkeyFPSIMD(hexcode[11:16])
		if(forwardedValues[0] != None):
			reg1Value = forwardedValues[0]
		if(forwardedValues[1] != None):
			reg2Value = forwardedValues[1]
		if(None in forwardedValues):
			armdebug.floatRFActivityCounter += 1
	else:
		return
	
	mem.regFloatObsolete[destRegister] += 1
	mem.regFloatObsolete_last_modified_indices.append(destRegister)
	#reg1Value = utilFunc.getRegValueByStringkeyFPSIMD(hexcode[22:27])
	#reg2Value = utilFunc.getRegValueByStringkeyFPSIMD(hexcode[11:16])
		
	mem.operand1Buffer = reg1Value
	mem.operand2Buffer = reg2Value


