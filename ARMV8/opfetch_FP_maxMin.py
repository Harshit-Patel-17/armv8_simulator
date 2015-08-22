# author swarnadeep

import utilFunc
import const
import mem
import armdebug
import config

def opfetchFMAX_scalar_SP(hexcode):
	executeFMAX_scalar(hexcode,1)

def opfetchFMAX_scalar_DP(hexcode):
	executeFMAX_scalar(hexcode,2)

def opfetchFMAX_vector_2S(hexcode):
	executeFMAX_vector(hexcode,0,0)

def opfetchFMAX_vector_4S(hexcode):
	executeFMAX_vector(hexcode,1,0)

def opfetchFMAX_vector_2D(hexcode):
	executeFMAX_vector(hexcode,1,1)

def opfetchFMIN_scalar_SP(hexcode):
	executeFMIN_scalar(hexcode,1)

def opfetchFMIN_scalar_DP(hexcode):
	executeFMIN_scalar(hexcode,2)

def opfetchFMIN_vector_2S(hexcode):
	executeFMIN_vector(hexcode,0,0)

def opfetchFMIN_vector_4S(hexcode):
	executeFMIN_vector(hexcode,1,0)

def opfetchFMIN_vector_2D(hexcode):
	executeFMIN_vector(hexcode,1,1)

def executeFMAX_scalar(hexcode, precision):
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
		armdebug.floatRFActivityCounter += 2
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

def executeFMIN_scalar(hexcode, precision):
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
		armdebug.floatRFActivityCounter += 2
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

def executeFMAX_vector(hexcode, Q, size):
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
		armdebug.floatRFActivityCounter += 2
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

def executeFMIN_vector(hexcode, Q, size):
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
		armdebug.floatRFActivityCounter += 2
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
