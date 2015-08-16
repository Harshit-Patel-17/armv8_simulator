# author swarnadeep

import utilFunc

#executes vector addition for integers in A1 configuration
def execVADD_intA1(hexcode):
	executeVADD_int(hexcode)

#executes vector addition for integers in T1 configuration
def execVADD_intT1(hexcode):
	executeVADD_int(hexcode)

#executes vector addition for floating point numbers in A1 configuration
def execVADD_FPA1(hexcode):
	executeVADD_FloatingPoint(hexcode)

#executes vector addition for floating point numbers in T1 configuration
def execVADD_FPT1(hexcode):
	executeVADD_FloatingPoint(hexcode)

#executes vector fused multiplication for vectors in A1 configuration
def execVFMA_A1(hexcode):
	executeVFMA(hexcode)

#executes vector fused multiplication for vectors in A1 configuration
def execVFMA_T1(hexcode):
	executeVFMA(hexcode)

#executes vector addition for integers
def executeVADD_int(hexcode):
	Q = hexcode[25]
	size = hexcode[10:12]
	esize = 8<<(utilFunc.uInt(size))
	elements = 64/esize
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[9] + hexcode[16:20])
	operandRegister1 = utilFunc.getRegKeyByStringKey(hexcode[24] + hexcode[12:16])
	operandRegister2 = utilFunc.getRegKeyByStringKey(hexcode[26] + hexcode[28:32])

	regValue1 = utilFunc.getRegValueByStringkeyFDSIMD(hexcode[24] + hexcode[12:16])
	regValue2 = utilFunc.getRegValueByStringkeyFDSIMD(hexcode[26] + hexcode[28:32])

	if(Q == '0'):
		regs = 1
	else:
		regs = 2
		operandRegister3 = operandRegister1 + 1
		operandRegister4 = operandRegister2 + 1
		regValue3 = utilFunc.getRegValueByRegkeyFDSIMD(operandRegister3)
		regValue4 = utilFunc.getRegValueByRegkeyFDSIMD(operandRegister4)
		resultBinaryHigher = ""

	resultBinaryLower = ""

	for e in range(elements):
		element1 = regValue1[(e*esize):(e*esize + esize)]
		element2 = regValue2[(e*esize):(e*esize + esize)]
		addition,isSp = utilFunc.addSub(destRegister, element1, element2, '0', esize, '0', 0) #SP carries no significance here, just wanted to use the already written addSub util function
		resultBinaryLower = resultBinaryLower + addition

	utilFunc.setRegValueSIMDFP(destRegister, resultBinaryLower)

	if(regs == 2):
		for e in range(elements):
			element1 = regValue3[(e*esize):(e*esize + esize)]
			element2 = regValue4[(e*esize):(e*esize + esize)]
			addition,isSp = utilFunc.addSub(destRegister, element1, element2, '0', esize, '0', 0) #SP carries no significance here, just wanted to use the already written addSub util function
			resultBinaryHigher = resultBinaryHigher + addition

		utilFunc.setRegValueSIMDFP((destRegister+1), resultBinaryHigher)

#executes vector addition for floating point numbers
def executeVADD_FloatingPoint(hexcode):
	Q = hexcode[25]
	esize = 32
	elements = 2
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[9] + hexcode[16:20])
	operandRegister1 = utilFunc.getRegKeyByStringKey(hexcode[24] + hexcode[12:16])
	operandRegister2 = utilFunc.getRegKeyByStringKey(hexcode[26] + hexcode[28:32])

	regValue1 = utilFunc.getRegValueByStringkeyFDSIMD(hexcode[24] + hexcode[12:16])
	regValue2 = utilFunc.getRegValueByStringkeyFDSIMD(hexcode[26] + hexcode[28:32])

	if(Q == '0'):
		regs = 1
	else:
		regs = 2
		operandRegister3 = operandRegister1 + 1
		operandRegister4 = operandRegister2 + 1
		regValue3 = utilFunc.getRegValueByRegkeyFDSIMD(operandRegister3)
		regValue4 = utilFunc.getRegValueByRegkeyFDSIMD(operandRegister4)
		resultBinaryHigher = ""

	resultBinaryLower = ""

	for e in range(elements):
		element1 = regValue1[(e*esize):(e*esize + esize)]
		element2 = regValue2[(e*esize):(e*esize + esize)]
		addition = utilFunc.addFP(element1, element2, esize)
		resultBinaryLower = resultBinaryLower + addition

	utilFunc.setRegValueSIMDFP(destRegister, resultBinaryLower)

	if(regs == 2):
		for e in range(elements):
			element1 = regValue3[(e*esize):(e*esize + esize)]
			element2 = regValue4[(e*esize):(e*esize + esize)]
			addition = utilFunc.addFP(element1, element2, esize)
			resultBinaryHigher = resultBinaryHigher + addition

		utilFunc.setRegValueSIMDFP((destRegister+1), resultBinaryHigher)

#executes vector fused multiplication
def executeVFMA(hexcode):
	Q = hexcode[25]
	op1_neg = (hexcode[10] == '1')
	esize = 32
	elements = 2
	destRegister1 = utilFunc.getRegKeyByStringKey(hexcode[9] + hexcode[16:20])
	operandRegister1 = utilFunc.getRegKeyByStringKey(hexcode[24] + hexcode[12:16])
	operandRegister2 = utilFunc.getRegKeyByStringKey(hexcode[26] + hexcode[28:32])

	destValue1 = utilFunc.getRegValueByStringkeyFDSIMD(hexcode[9] + hexcode[16:20])
	regValue1 = utilFunc.getRegValueByStringkeyFDSIMD(hexcode[24] + hexcode[12:16])
	regValue2 = utilFunc.getRegValueByStringkeyFDSIMD(hexcode[26] + hexcode[28:32])

	if(Q == '0'):
		regs = 1
	else:
		regs = 2
		destRegister2 = destRegister1 + 1
		operandRegister3 = operandRegister1 + 1
		operandRegister4 = operandRegister2 + 1
		destValue2 = utilFunc.getRegValueByRegkeyFDSIMD(destRegister2)
		regValue3 = utilFunc.getRegValueByRegkeyFDSIMD(operandRegister3)
		regValue4 = utilFunc.getRegValueByRegkeyFDSIMD(operandRegister4)
		resultBinaryHigher = ""

	resultBinaryLower = ""

	for e in range(elements):
		element1 = regValue1[(e*esize):(e*esize + esize)]
		if(op1_neg):
			element1 = utilFunc.negFP(element1, esize)
		element2 = regValue2[(e*esize):(e*esize + esize)]
		destElement = destValue1[(e*esize):(e*esize + esize)]
		result = utilFunc.mulAddFP(destElement, element1, element2, esize)
		resultBinaryLower = resultBinaryLower + result

	utilFunc.setRegValueSIMDFP(destRegister1, resultBinaryLower)

	if(regs == 2):
		for e in range(elements):
			element1 = regValue3[(e*esize):(e*esize + esize)]
			if(op1_neg):
				element1 = utilFunc.negFP(element1, esize)
			element2 = regValue4[(e*esize):(e*esize + esize)]
			destElement = destValue2[(e*esize):(e*esize + esize)]
			result = utilFunc.mulAddFP(destElement, element1, element2, esize)
			resultBinaryHigher = resultBinaryHigher + result

		utilFunc.setRegValueSIMDFP(destRegister1, resultBinaryHigher)
