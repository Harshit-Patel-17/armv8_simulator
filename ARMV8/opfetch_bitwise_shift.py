#author swarnadeep

import utilFunc
import mem
import const

def opfetchBitwiseShift_32(hexcode):
	executeBitwiseShiftRegister(hexcode, 32, 0)

def opfetchBitwiseShift_64(hexcode):
	executeBitwiseShiftRegister(hexcode, 64, 0)

def opfetchBitwiseShiftSetFlags_32(hexcode):
	executeBitwiseShiftRegister(hexcode, 32, 1)

def opfetchBitwiseShiftSetFlags_64(hexcode):
	executeBitwiseShiftRegister(hexcode, 64, 1)

def executeBitwiseShiftRegister(hexcode, datasize, setFlags):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	operandRegister1 = utilFunc.getRegKeyByStringKey(hexcode[22:27])
	operandRegister2 = utilFunc.getRegKeyByStringKey(hexcode[11:16])
	
	const.FLAG_OPFETCH_EXECUTED = True
	if(mem.regObsolete[operandRegister1] == False and mem.regObsolete[operandRegister2] == False):
		const.FLAG_OP_FETCHED = True
		reg1Value = utilFunc.getRegValueByStringkey(hexcode[22:27],'0')
		reg2Value = utilFunc.getRegValueByStringkey(hexcode[11:16],'0')
	elif(const.FLAG_DATA_FORWARDING):
		forwardedValues = mem.findForwardedValues(operandRegister1, operandRegister2)
		if(forwardedValues[0] != None and forwardedValues[1] != None):
			const.FLAG_OP_FETCHED = True
			reg1Value = forwardedValues[0]
			reg2Value = forwardedValues[1]
		else:
			return
	else:
		return
	
	mem.regObsolete[destRegister] = True
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