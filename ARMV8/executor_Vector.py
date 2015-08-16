# author swarnadeep

def execVCNT_A1_64(hexcode):
	executeVCNT(hexcode, 64)

def execVCNT_A1_128(hexcode):
	executeVCNT(hexcode, 128)

def execVCNT_T1_64(hexcode):
	executeVCNT(hexcode, 64)

def execVCNT_T1_128(hexcode):
	executeVCNT(hexcode, 128)

def executeVCNT(hexcode, datasize):
	assert (hexcode[12:14] == "00")
	esize = 8
	elements = 8
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[9] + hexcode[16:20])
	operandRegister1 = utilFunc.getRegKeyByStringKey(hexcode[26] + hexcode[28:32])

	regValue1 = utilFunc.getRegValueByStringkeyFDSIMD(hexcode[26] + hexcode[28:32])
	if(datasize == 64):
		regs = 1
	else: 
		regs = 2
		operandRegister2 = operandRegister1 + 1
		regValue2 = getRegValueByRegkeyFDSIMD(operandRegister2)
		resultBinaryHigher = ""

	resultBinaryLower = ""

	for e in range(elements):
		setBits = utilFunc.countSetBits(regValue1[(e*esize):(e*esize + esize)])
		setBitsBinary = "{0:b}".format(setBits)
		setBitsBinary = setBitsBinary.zfill(esize)
		resultBinaryLower = resultBinaryLower + setBitsBinary

	utilFunc.setRegValueSIMDFP(destRegister, resultBinaryLower)

	if(regs == 2):
		for e in range(elements):
			setBits = utilFunc.countSetBits(regValue2[(e*esize):(e*esize + esize)])
			setBitsBinary = "{0:b}".format(setBits)
			setBitsBinary = setBitsBinary.zfill(esize)
			resultBinaryHigher = resultBinaryHigher + setBitsBinary

		utilFunc.setRegValueSIMDFP((destRegister+1), resultBinaryHigher)