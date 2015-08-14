# author swarnadeep

# executes floating point scalar addition for single precision
def execFADD_scalar_SP(hexcode):
	executeFADD_scalar(hexcode, 1)

# executes floating point scalar addition for single precision
def execFADD_scalar_DP(hexcode):
	executeFADD_scalar(hexcode, 2)

# executes floating point vector addition for two 32 bit FPs stored in each 64 bit registers
def execFADD_vector_2S(hexcode):
	executeFADD_vector(hexcode,0,0)

# executes floating point vector addition for four 32 bit FPs stored in each 128 bit registers
def execFADD_vector_4S(hexcode):
	executeFADD_vector(hexcode,0,1)

# executes floating point vector addition for two 64 bit FPs stored in each 128 bit registers
def execFADD_vector_2D(hexcode):
	executeFADD_vector(hexcode,1,1)

# executes floating point scalar subtraction for single precision
def execFSUB_scalar_SP(hexcode):
	executeFSUB_scalar(hexcode,1)

# executes floating point scalar subtraction for double precision
def execFSUB_scalar_DP(hexcode):
	executeFSUB_scalar(hexcode,2)

# executes floating point vector subtraction for two 32 bit FPs stored in each 64 bit registers
def execFSUB_vector_2S(hexcode):
	executeFSUB_vector(hexcode,0,0)

# executes floating point vector subtraction for four 32 bit FPs stored in each 128 bit registers
def execFSUB_vector_4S(hexcode):
	executeFSUB_vector(hexcode,0,1)

# executes floating point vector subtraction for two 64 bit FPs stored in each 128 bit registers
def execFSUB_vector_2D(hexcode):
	executeFSUB_vector(hexcode,1,1)

# utility function for floating point scalar addition
def executeFADD_scalar(hexcode, precision):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	operandRegister1 = utilFunc.getRegKeyByStringKey(hexcode[22:27])
	operandRegister2 = utilFunc.getRegKeyByStringKey(hexcode[11:16])

	reg1Value = utilFunc.getRegValueByStringkeyFDSIMD(hexcode[22:27])
	reg2Value = utilFunc.getRegValueByStringkeyFDSIMD(hexcode[11:16])

	if(precision == 1):
		reg1Value = reg1Value[96:128]
		reg2Value = reg2Value[96:128]
		datasize =32
	else:
		reg1Value = reg1Value[64:128]
		reg2Value = reg2Value[64:128]
		datasize = 64

	resultBinary = utilFunc.addFP(reg1Value,reg2Value, datasize)
	resultBinary.zfill(128)

	utilFunc.setRegValueSIMDFP(destRegister, resultBinary)

# utility function for floating point scalar subtraction
def executeFSUB_scalar(hexcode, precision):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	operandRegister1 = utilFunc.getRegKeyByStringKey(hexcode[22:27])
	operandRegister2 = utilFunc.getRegKeyByStringKey(hexcode[11:16])

	reg1Value = utilFunc.getRegValueByStringkeyFDSIMD(hexcode[22:27])
	reg2Value = utilFunc.getRegValueByStringkeyFDSIMD(hexcode[11:16])

	if(precision == 1):
		reg1Value = reg1Value[96:128]
		reg2Value = reg2Value[96:128]
		datasize =32
	else:
		reg1Value = reg1Value[64:128]
		reg2Value = reg2Value[64:128]
		datasize = 64

	resultBinary = utilFunc.subFP(reg1Value,reg2Value, datasize)
	resultBinary.zfill(128)

	utilFunc.setRegValueSIMDFP(destRegister, resultBinary)

# utility function for floating point vector addition
def executeFADD_vector(hexcode, Q, size):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	operandRegister1 = utilFunc.getRegKeyByStringKey(hexcode[22:27])
	operandRegister2 = utilFunc.getRegKeyByStringKey(hexcode[11:16])

	reg1Value = utilFunc.getRegValueByStringkeyFDSIMD(hexcode[22:27])
	reg2Value = utilFunc.getRegValueByStringkeyFDSIMD(hexcode[11:16])

	resultBinary = ""

	esize = 32<<int(size, 2)
	if(Q == '1'):
		datasize = 128
	else:
		datasize = 64
		reg1Value = reg1Value[64:128]
		reg2Value = reg2Value[64:128]

	elements = datasize/esize

	for e in range(elements):
		element1 = reg1Value[(e*esize):(e*esize + size)]
		element2 = reg2Value[(e*esize):(e*esize + size)]

		resultBinary = resultBinary + utilFunc.addFP(element1, element2, datasize)

	resultBinary.zfill(128)

	utilFunc.setRegValueSIMDFP(destRegister, resultBinary)

# utility function for floating point vector subtraction
def executeFSUB_vector(hexcode, Q, size):
	destRegister = utilFunc.getRegKeyByStringKey(hexcode[27:32])
	operandRegister1 = utilFunc.getRegKeyByStringKey(hexcode[22:27])
	operandRegister2 = utilFunc.getRegKeyByStringKey(hexcode[11:16])

	reg1Value = utilFunc.getRegValueByStringkeyFDSIMD(hexcode[22:27])
	reg2Value = utilFunc.getRegValueByStringkeyFDSIMD(hexcode[11:16])

	resultBinary = ""

	esize = 32<<int(size, 2)
	if(Q == '1'):
		datasize = 128
	else:
		datasize = 64
		reg1Value = reg1Value[64:128]
		reg2Value = reg2Value[64:128]

	elements = datasize/esize

	for e in range(elements):
		element1 = reg1Value[(e*esize):(e*esize + size)]
		element2 = reg2Value[(e*esize):(e*esize + size)]

		resultBinary = resultBinary + utilFunc.subFP(element1, element2, datasize)

	resultBinary.zfill(128)

	utilFunc.setRegValueSIMDFP(destRegister, resultBinary)


