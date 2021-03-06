'''
@author: harinder
'''
import const
import mem
import armdebug
import math
import sys

def hexToBin(s, numOfBits=const.INST_SIZE):
    scale = 16  # # equals to hexadecimal 
    binary = bin(int(s, scale))[2:].zfill(numOfBits)
    return binary

def lsl(s, i):
    return s[i:len(s)] + '0' * i
    
def lsr(s, i):
    return '0' * i + s[0:len(s) - i]
    
def asr(s, i):
    return s[0] * i + s[0:len(s) - i]
    
def ror(s, i):
    for x in range(i):
        s = s[-1] + s[0:len(s) - 1]
    return s

# gives 64 bit, truncate when using
# key should be 0 to 31 in binary string
def getRegValueByStringkey(key, isSp):
    key = int(key, 2)
    assert key >= 0 and key <= 31
    if key != 31 or isSp == '1':
        return mem.regFile[key]
    else:
        return '0' * 64

# gives 128 bit, truncate when using
# key should be 0 to 31 in binary string
# used for FP & SIMD instructions
def getRegValueByStringkeyFPSIMD(key):
    key = int(key, 2)
    assert key >= 0 and key <= 31
    return mem.regFileFPSIMD[key]

def getRegValueByRegkeyFDSIMD(key):
    assert key >= 0 and key <= 31
    return mem.regFileFPSIMD[key]

def getRegKeyByStringKey(key):
    key = int(key, 2)
    return key

# assuming both s1 and s2 have same length    
def logical_and(s1, s2):
    to_return = ''
    if len(s1) != len(s2):
        print 'Implementation error. Lengths not equal'
        exit(1)
    else:        
        for x in range(len(s1)):
            if s1[x] != s2[x]:
                to_return += '0'
            elif s1[x] == '0':
                to_return += '0'
            else:
                to_return += '1'
    return to_return

# assuming both s1 and s2 have same length    
def logical_or(s1, s2):
    to_return = ''
    if len(s1) != len(s2):
        print 'Implementation error. Lengths not equal'
        exit(1)
    else:
        for x in range(len(s1)):
            if s1[x] != s2[x]:
                to_return += '1'
            elif s1[x] == '1':
                to_return += '1'
            else:
                to_return += '0'
    return to_return


def resetInstrFlag():
    const.FLAG_INST_EXECUTED = "0"
    
# sets the register value, prints the inst, sets the instr flag
def finalize(rdKey, val, instr, isSp):
    setRegValue(rdKey, val, isSp)
    finalize_simple(instr)
    
def finalize_simple(instr):
    print instr
    const.FLAG_INST_EXECUTED = "1"

# val is 64 bit string to be stored in reg with rdkey
def setRegValue(rdKey, val, isSp):
    assert rdKey >= 0 and rdKey <= 31
    #assuming rdkey is being changed, we call a method here which check for the watch method
    ifWatch(rdKey) #ask about 31 from partner
        
    if(rdKey != 31 or isSp == '1'):    
        # ignoring the result - zero register        
        del mem.regFile[rdKey]
        mem.regFile.insert(rdKey, val)

# val is 128 bit string to be stored in reg with rdkey
def setRegValueSIMDFP(rdKey, val):
    assert rdKey >= 0 and rdKey <= 31
    del mem.regFileFPSIMD[rdKey]
    mem.regFileFPSIMD.insert(rdKey, val)
        
def ifWatch(rdKey):
    if mem.isWatchSet(rdKey):
        mem.resetWatchForReg(rdKey)
        #set somtehing global here which pauses everything on the planet!
        #after this inst everything should pause!!
        armdebug.setWatchPause()
        #dont forget to reset the watch pause!!
        
# utility function that takes num int convert it into binary of size N
def intToBinary(num, N):
    x = "{0:b}".format(num)
    if(x[0] == '-'):
        x = (x[1:len(x)]).zfill(N)
        x = twosComplement(x,N)
    return x.zfill(N)
    
        
# utility function used by all add-sub instructions
def addSub(rdKey, op1, op2, sub_op, N, setFlags, addWithCarry):
    c_in = '0'
    if(sub_op == '1'):
        op2 = negate(op2)
    if(sub_op == '1' or addWithCarry):
        c_in = '1'
    unsigned_sum = uInt(op1) + uInt(op2) + uInt(c_in)
    signed_sum = sInt(op1, N) + sInt(op2, N) + uInt(c_in)
    result = ("{0:b}".format(unsigned_sum))
    if(len(result) > N):
        result = result[1:N + 1]
    if(len(result) < N):
        result = result.zfill(N)

    if(setFlags == '1'):
        setFlagsFromResult(result, unsigned_sum, signed_sum, N)
    
    if(rdKey == 31 and setFlags == '0'):
        isSp = '1'
    else:
        isSp = '0'
    return result.zfill(N), isSp

def uInt(x):
    return int(x, 2)

def sInt(x, N):
    result = int(x, 2)
    if(x[0] == '1'):
        result = result - 2 ** N
    return result

# return not(x)
def negate(x):
    to_ret = ''
    for c in x:
        if(c == '1'):
            to_ret = to_ret + '0'
        else:
            to_ret = to_ret + '1'
    return to_ret

def twosComplement(x, N):
    result, isSp = addSub(0,'0' * N, x, '1', N, '0', 0)
    return result

def binaryToHexStr(x):
    #print 'x '+str(x)
    x = str(hex(int(x, 2)))
    if(x[-1] == 'L'):
        x = x[0:len(x) - 1]
    return x
    
# get flags
def get_N_flag():
    return mem.flagFile[0];
    
def set_N_flag():
    mem.flagFile[0] = '1';

def reset_N_flag():
    mem.flagFile[0] = '0';

def get_Z_flag():
    return mem.flagFile[1];
    
def set_Z_flag():
    mem.flagFile[1] = '1';
    
def reset_Z_flag():
    mem.flagFile[1] = '0';

def get_C_flag():
    return mem.flagFile[2];
    
def set_C_flag():
    mem.flagFile[2] = '1';
    
def reset_C_flag():
    mem.flagFile[2] = '0';

def get_V_flag():
    return mem.flagFile[3];
    
def set_V_flag():
    mem.flagFile[3] = '1';

def reset_V_flag():
    mem.flagFile[3] = '0';

def printAllFlags():
    print "flags(z,v,n,c): " + get_Z_flag() + "," + get_V_flag() + "," + get_N_flag() + "," + get_C_flag()
    
def printAllRegs():
    i = 0
    for x in mem.regFile:
        print 'R'+str(i).zfill(2) + ": " + x
        i = i + 1
    print '<--\'R31\' denotes SP-->'

# usage give a binary of length <=N
# sign extends it and returns the resulting binary
def signExtend(binary, N):
    assert len(binary) <= N
    return binary[0] * (N - len(binary)) + binary

def zeroExtend(binary, N):
    assert len(binary) <= N
    return '0' * (N - len(binary)) + binary

def extend(x, N, unsigned):
    if(unsigned == 1):
        return zeroExtend(x, N)
    else:
        return signExtend(x, N)

def branchWithOffset(offset):  # signed offset
    armdebug.setPC((armdebug.getPC() + offset - 4))  # the magic! #-4 for the current instruction
    
#def branchToAddress(hexint):  # give the exact address in int where to branch
#    armdebug.setPC(hexint - 4)  # the magic again! #-4 for the current instruction

def branchToAddress(hexint):  # give the exact address in int where to branch
    armdebug.setPC(hexint)  # the magic again! #-4 for the current instruction
    
def PCwithOffset(offset):
    return armdebug.getPC()+offset#don't change this, it is no 4 only!!! 
    #why this? because the offset is always given from the current instruction
    
def PCwithPageOffset(N,offset):
    PCint=armdebug.getPC()
    PCbin=intToBinary(PCint, 64)
    PCbinModified=PCbin[0:52]+'0'*N
    PCnow=int(PCbinModified,2)
    return PCnow+offset
    
def conditionHolds(bits_four):
    # print 'condHolds'
    first_three = bits_four[0:3]
    # print first_three
    result = False
    cond = ''
    if first_three == '000':
        result = get_Z_flag() == '1'
        cond = 'EQ/NE'
        # print '1'
    elif first_three == '001':
        result = get_C_flag() == '1'
        cond = 'CS/CC'
        # print '2'
    elif first_three == '010':
        result = get_N_flag() == '1'
        cond = 'MI/PL'
        # print '3'
    elif first_three == '011':
        result = get_V_flag() == '1'
        cond = 'VS/VC'
        # print '4'
    elif first_three == '100':
        result = get_C_flag() == '1' and get_Z_flag() == '0'
        cond = 'HI/LS'
        # print '5'
    elif first_three == '101':
        result = (get_N_flag() == get_V_flag())
        cond = 'GE/LT'
        # print '6'
    elif first_three == '111':
        result = True
        cond = 'AL'
        # print'7'
        
    if bits_four[-1] == '1' and bits_four != '1111':
        result = not result
        # print '8'
    # print cond
    return (result, cond)

def getOffset(immkey):
    immkey=signExtend(immkey+'00', 64) #times 4 and 64 bits
    sign=immkey[0]
    offset=''
    inst=''
    if sign=='1':
        immkey=twosComplement(immkey, 64)
        inst+='-'
        offset=-int(immkey, 2)
    else:
        offset=int(immkey, 2)
    inst+=str(int(immkey, 2))
    return (inst, offset)

def getOffsetWithoutTimes(immkey):
    immkey=signExtend(immkey, 64) #no times 4 and 64 bits
    sign=immkey[0]
    offset=''
    inst=''
    if sign=='1':
        immkey=twosComplement(immkey, 64)
        inst+='-'
        offset=-int(immkey, 2)
    else:
        offset=int(immkey, 2)
    inst+=str(int(immkey, 2))
    return (inst, offset)

def decodeBitMasks(immN, imms, immr, M):
    len = highestSetBit(immN+negate(imms))
    levels = zeroExtend('1'*len, 6)
    s = uInt(logical_and(imms, levels))
    r = uInt(logical_and(immr, levels))
    diff = s-r
    esize = 1<<len
    d = uInt(intToBinary(diff, len))
    welem = zeroExtend('1'*(s+1), esize)
    telem = zeroExtend('1'*(d+1), esize)
    wmask = replicate(ror(welem, r), M)
    tmask = replicate(telem, M)
    return wmask,tmask

def replicate(x, N):
    while(len(x)<N):
        x = x+x
    return x
    
    
def highestSetBit(x):
    i = 0
    for c in x:
        if(c == '1'):
            return len(x)-i-1
        i = i+1
    return -1

def extendReg(rmVal, shift, option, instr, N):
    assert shift >= 0 and shift <= 4
    if(option == "000"):
        # ExtendType_UXTB
        instr += 'UXTB'
        unsigned = 1
        len = 8
    elif (option == "001"):
        # ExtendType_UXTH
        instr += 'UXTH'
        unsigned = 1
        len = 16
    elif (option == "010"):
        # ExtendType_UXTW
        instr += 'UXTW'
        unsigned = 1
        len = 32
    elif (option == "011"):
        # ExtendType_UXTX
        instr += 'UXTX'
        unsigned = 1
        len = 64
    elif (option == "100"):
        # ExtendType_SXTB
        instr += 'SXTB'
        unsigned = 0
        len = 8
    elif (option == "101"):
        # ExtendType_SXTH
        instr += 'SXTH'
        unsigned = 0
        len = 16
    elif (option == "110"):
        # ExtendType_SXTW
        instr += 'SXTW'
        unsigned = 0
        len = 32
    elif (option == "111"):
        # ExtendType_SXTX
        instr += 'SXTX'
        unsigned = 0
        len = 64
    len = min(len, N - shift)
    return extend(rmVal[N - 1 - (len - 1):N] + '0' * shift, N, unsigned), instr

def fetch32bitDataFromMem(address):
    hexData = mem.fetchWordFromMemory(address)
    if(hexData == const.TRAP):
        return const.TRAP
    return hexToBin(hexData)

def fetch64bitDataFromMem(address):
    rightData = fetch32bitDataFromMem(address)    
    leftData = fetch32bitDataFromMem(address+4)
    if(rightData == const.TRAP or leftData == const.TRAP):
        return const.TRAP
    return leftData + rightData

def fetchFromMemory(address, dataSize):
    if(dataSize == 64):
        data = fetch64bitDataFromMem(address)
    else:
        data = fetch32bitDataFromMem(address)
        
    if(dataSize == 8):
        data = data[24:32]
    elif(dataSize == 16):
        data = data[16:32]
    return data

def store32bitDataToMem(address, data):
    data = binaryToHexStr(data)
    data = (data[2:len(data)]).zfill(8)
    mem.storeWordToMemory(address, data)
    
def store64bitDataToMem(address, data):
    rightData = data[32:64]
    leftData = data[0:31]
    store32bitDataToMem(address, rightData)
    store32bitDataToMem(address+4, leftData)
    
def storeToMemory(data, address, dataSize):
    if(dataSize == 32):
            data = data[32:64]
            store32bitDataToMem(address, data)
    if(dataSize == 64):
            store64bitDataToMem(address, data)

def calculateXor(input1,input2):
    answer = ''
    for i in range(len(input1)):
        if(input1[i] == input2[i]):
            answer = answer + '0'
        else:
            answer = answer +'1'
    return answer

def countLeadingZeroBits(input, datasize):
    index = datasize - 1
    for i in range(datasize):
        if(input[i] == '1'):
            return datasize - 1 - index
        index = index -1

    return datasize

def countLeadingSignBits(input, datasize):
    return countLeadingZeroBits(calculateXor(input[1:datasize],input[0:(datasize-1)]), datasize-1)

def countSetBits(input):
    i = 0
    count = 0
    for c in input:
        if(c == '1'):
            count = count + 1
        i = i+1
    return count 

def setFlags(flags):
    if(flags[0]=='1'):
        set_N_flag()
    else:
        reset_N_flag()
    
    if(flags[1]=='1'):
        set_Z_flag()
    else:
        reset_Z_flag()

    if(flags[2]=='1'):
        set_C_flag()
    else:
        reset_C_flag()

    if(flags[3]=='1'):
        set_V_flag()
    else:
        reset_V_flag()

def rotateRightByBits(binary, numberOfBits, datasize):
    return binary[(datasize-numberOfBits):datasize] + binary[0:(datasize-numberOfBits)]

# Setting flags
def setFlagsFromResult(result, unsigned_sum, signed_sum, N):
    if(result[0] == '0'):
        reset_N_flag()
    else:
        set_N_flag()
    if(int(result) == 0):
        set_Z_flag()
    else:
        reset_Z_flag()
    if(uInt(result) == unsigned_sum):
        reset_C_flag()
    else:
        set_C_flag()
    if(sInt(result, N) == signed_sum):
        reset_V_flag()
    else:
        set_V_flag()

def isZero(result):
    if(int(result) == 0):
        return '1'
    else:
        return '0'

def isOnes(result, datasize):
    if("1"*datasize == result):
        return '1'
    else:
        return '0'

#-------------Floating Point Util functions-----------------


def FPDefaultNaN(datasize):
    if(datasize == 16):
        exp = 5
    elif(datasize == 32):
        exp = 8
    else:
        exp = 11

    frac = datasize-1-exp

    return "0" + "1"*exp + "1" + "0"*(frac-1)

def FPInfinity(datasize, sign):
    if(datasize == 16):
        exp = 5
    elif(datasize == 32):
        exp = 8
    else:
        exp = 11

    frac = datasize-1-exp

    return sign + "1"*exp + "0"*frac

def FPZero(datasize, sign):
    if(datasize == 16):
        exp = 5
    elif(datasize == 32):
        exp = 8
    else:
        exp = 11

    frac = datasize-1-exp

    return sign + "0"*exp + "0"*frac 

def FPMaxNormal(datasize, sign):
    if(datasize == 16):
        exp = 5
    elif(datasize == 32):
        exp = 8
    else:
        exp = 11

    frac = datasize-1-exp

    return sign + "1"*(exp-1) + "0" + "1"*frac  

def FPProcessNaN(type, op, datasize):
    if(datasize == 32):
        topFrac = 9
    else:
        topFrac = 12

    result = op
    if(type == "FPType_SNaN"):
        result[topFrac] = '1'
    if(getDNBit()=='1'):
        result = FPDefaultNaN()
    return result

def FPProcessNaNs(type1, type2, op1, op2, datasize):
    if(type1 == "FPType_SNaN"):
        done = True
        result = FPProcessNaN(type1, op1, datasize)
    elif(type2 == "FPType_SNaN"):
        done = True
        result = FPProcessNaN(type2, op2, datasize)
    elif(type1 == "FPType_QNaN"):
        done = True 
        result = FPProcessNaN(type1, op1, datasize)
    elif(type2 == "FPType_QNaN"):
        done = True
        result = FPProcessNaN(type2, op2, datasize)
    else:
        done = False 
        result = "0"*datasize; # 'Don't care' result
    return (done, result)

def FPProcessNaNs3(type1, type2, type3, op1,op2, op3, datasize):
    if(type1 == "FPType_SNaN"):
        done = True
        result = FPProcessNaN(type1, op1, datasize)
    elif(type2 == "FPType_SNaN"):
        done = True
        result = FPProcessNaN(type2, op2, datasize)
    elif(type3 == "FPType_SNaN"):
        done = True
        result = FPProcessNaN(type3, op3, datasize)
    elif(type1 == "FPType_QNaN"):
        done = True 
        result = FPProcessNaN(type1, op1, datasize)
    elif(type2 == "FPType_QNaN"):
        done = True
        result = FPProcessNaN(type2, op2, datasize)
    elif(type3 == "FPType_QNaN"):
        done = True
        result = FPProcessNaN(type3, op3, datasize)
    else:
        done = False 
        result = "0"*datasize; # 'Don't care' result
    return (done, result)

def getRoundingBits():
    return mem.fpcrFile[8:10]

def getDNBit():
    return mem.fpcrFile[6]

def getAHPBit():
    return mem.fpcrFile[5]

def getFZBit():
    return mem.fpcrFile[7]

def VFPExpandImm(imm8, datasize):
    if(datasize == 32):
        exp = 8
    else:
        exp = 11
    frac = datasize - exp - 1
    sign = imm8[0]
    exp = negate(imm8[1]) + imm8[1]*(exp-3) + imm8[2:4]
    frac = imm8[4:8] + '0'*(frac-4)
    return sign + exp + frac

def FPDecodeRounding(bits):
    if(bits == "00"):
        return "TIEEVEN"
    elif(bits == "01"):
        return "POSINF"
    elif(bits == "10"):
        return "NEGINF"
    else:
        return "ZERO"

# decodes the floating point number
def unpackFP(fpval, datasize):
    if(datasize == 16):
        sign = fpval[0]
        exp16 = fpval[1:6]
        frac16 = fpval[6:16]

        if(isZero(exp16)=='1'):
            if(isZero(frac16)=='1'):
                typeOfVal = "FPType_Zero"
                value = 0.0
            else:
                typeOfVal = "FPType_Nonzero"
                value = 2.0**(-14) * uInt(frac16) * 2.0**(-10)
        elif(isOnes(exp16, datasize)=='1' and getAHPBit() == '0'):
            if(isZero(frac16)=='1'):
                typeOfVal = "FPType_Infinity"
                value = sys.maxint#2.0**(1000000)
            else:
                if(frac16[0] == '1'):
                    typeOfVal = "FPType_QNaN" 
                else:
                    typeOfVal = "FPType_SNaN"
                value = 0.0
        else:
            typeOfVal = "FPType_Nonzero"
            value = 2.0**(uInt(exp16)-15) * (1.0 + uInt(frac16) * 2.0**(-10))

    elif(datasize == 32):
        sign = fpval[0]
        exp32 = fpval[1:9]
        frac32 = fpval[9:32]
        
        if(isZero(exp32)=='1'):
            if(isZero(frac32)=='1' or getFZBit() == '1'):
                typeOfVal = "FPType_Zero"
                value = 0.0
            else:
                typeOfVal = "FPType_Nonzero"
                value = 2.0**(-126) * uInt(frac32) * 2.0**(-23)
        elif(isOnes(exp32, datasize) == '1'):
            if(isZero(frac32) == '1'):
                typeOfVal = "FPType_Infinity"
                value = sys.maxint#2.0**(1000000)
            else:
                if(frac32[0] == '1'):
                    typeOfVal = "FPType_QNaN" 
                else:
                    typeOfVal = "FPType_SNaN"
                value = 0.0
        else:
            typeOfVal = "FPType_Nonzero"
            value = 2.0**(uInt(exp32)-127) * (1.0 + uInt(frac32) * 2.0**(-23))

    else:
        sign = fpval[0]
        exp64 = fpval[1:12]
        frac64 = fpval[12:64]

        if(isZero(exp64)=='1'):
            if(isZero(frac64)=='1' or getFZBit() =='1'):
                typeOfVal = "FPType_Zero"
                value = 0.0
            else:
                typeOfVal = "FPType_Nonzero"
                value = 2.0**(-1022) * uInt(frac64) * 2.0**(-52)
        elif(isOnes(exp64, datasize)=='1'):
            if(isZero(frac64)):
                typeOfVal = "FPType_Infinity"
                value = sys.maxint#2.0**(1000000)
            else:
                if(frac64[0] == '1'):
                    typeOfVal = "FPType_QNaN" 
                else:
                    typeOfVal = "FPType_SNaN"
                value = 0.0
        else:
            typeOfVal = "FPType_Nonzero"
            value = 2.0**(uInt(exp64)-1023) * (1.0 + uInt(frac64) * 2.0**(-52))


    if(sign == '1'):
        value = -value

    return (typeOfVal, sign, value)

#applies proper rounding technique and returns the binary represenattion of op
def FPRound(op, rounding, datasize):
    if(datasize == 16):
        minimum_exp = -14
        E = 5
        F = 10
    elif(datasize == 32):
        minimum_exp = -126
        E = 8
        F = 23
    else:
        minimum_exp = -1022
        E = 11
        F = 52

    if(op < 0.0):
        sign = '1'
        mantissa = -op
    else:
        sign = '0'
        mantissa = op
    exponent = 0

    while(mantissa < 1.0):
        mantissa = mantissa * 2.0
        exponent = exponent - 1

    while(mantissa >= 2.0):
        mantissa = mantissa / 2.0
        exponent = exponent + 1

    if(getFZBit() == '1' and datasize != 16 and exponent < minimum_exp):
        return FPZero(datasize, sign)

    biased_exp = max((exponent - minimum_exp + 1), 0)
    if(biased_exp == 0):
        mantissa = mantissa / 2.0**(minimum_exp - exponent)

    int_mant = int(math.floor(mantissa * 2.0**F))
    error = mantissa * 2.0**F - int_mant

    if(rounding == "TIEEVEN"):
        round_up = (error > 0.5 or (error == 0.5 and int_mant%2 == 1))
        overflow_to_inf = True
    elif(rounding == "POSINF"):
        round_up = (error != 0.0 and sign == '0')
        overflow_to_inf = (sign == '0')
    elif(rounding == "NEGINF"):
        round_up = (error != 0.0 and sign == '1')
        overflow_to_inf = (sign == '1')
    else:
        round_up = False
        overflow_to_inf = False

    if(round_up):
        int_mant = int_mant + 1
        if(int_mant == 2**F):
            biased_exp = 1
        if(int_mant == 2*(F+1)):
            biased_exp = biased_exp + 1
            int_mant = int_mant / 2

    if(datasize != 16 or getAHPBit() == '0'):
        if(biased_exp >= (2**E - 1)):
            if(overflow_to_inf):
                result = FPInfinity(datasize, sign)
            else:
                result = FPMaxNormal(datasize, sign)
            error = 1.0
        else:
            biased_exp_binary = "{0:b}".format(biased_exp)
            biased_exp_binary = biased_exp_binary[-(datasize - F -1):]
            binary_mant = "{0:b}".format(int_mant)
            binary_mant = binary_mant[-F:]
            result = sign + biased_exp_binary + binary_mant
    else:
        if(biased_exp >= 2^E):
            result = sign + "1"*(datasize - 1)
            error = 0.0
        else:
            biased_exp_binary = "{0:b}".format(biased_exp)
            biased_exp_binary = biased_exp_binary[-(datasize - F -1):]
            binary_mant = "{0:b}".format(int_mant)
            binary_mant = binary_mant[-F:]
            result = sign + biased_exp_binary + binary_mant

    return result


def addFP(op1, op2, datasize):
    rounding = FPDecodeRounding(getRoundingBits())

    (type1, sign1, value1) = unpackFP(op1, datasize)
    (type2, sign2, value2) = unpackFP(op2, datasize)

    (done, result) = FPProcessNaNs(type1, type2, op1, op2, datasize)

    if(not done):
        inf1 = (type1 == "FPType_Infinity")
        inf2 = (type2 == "FPType_Infinity")
        zero1 = (type1 == "FPType_Zero")
        zero2 = (type2 == "FPType_Zero")

        if(inf1 and inf2 and (sign1 == negate(sign2))):
            result = FPDefaultNaN()
        elif((inf1 and sign1 == '0') or (inf2 and sign2 == '0')):
            result = FPInfinity(datasize, "0")
        elif((inf1 and sign1 == '1') or (inf2 and sign2 == '1')):
            result = FPInfinity(datasize, "1")
        elif(zero1 and zero2 and sign1 == sign2):
            result = FPZero(datasize, sign1)
        else:
            result_value = value1 + value2
            if(result_value == 0.0):
                if(rounding == "NEGINF"):
                    result_sign = "1"
                else:
                    result_sign = "0"
                result = FPZero(datasize, result_sign)
            else:
                result = FPRound(result_value, rounding, datasize)

    return result


def subFP(op1, op2, datasize):
    rounding = FPDecodeRounding(getRoundingBits())
    
    (type1, sign1, value1) = unpackFP(op1, datasize)
    (type2, sign2, value2) = unpackFP(op2, datasize)

    (done, result) = FPProcessNaNs(type1, type2, op1, op2,datasize)

    if(not done):
        inf1 = (type1 == "FPType_Infinity")
        inf2 = (type2 == "FPType_Infinity")
        zero1 = (type1 == "FPType_Zero")
        zero2 = (type2 == "FPType_Zero")

        if(inf1 and inf2 and (sign1 == negate(sign2))):
            result = FPDefaultNaN()
        elif((inf1 and sign1 == '0') or (inf2 and sign2 == '1')):
            result = FPInfinity(datasize, "0")
        elif((inf1 and sign1 == '1') or (inf2 and sign2 == '0')):
            result = FPInfinity(datasize, "1")
        elif(zero1 and zero2 and sign1 == negate(sign2)):
            result = FPZero(datasize, sign1)
        else:
            result_value = value1 - value2
            if(result_value == 0.0):
                if(rounding == "NEGINF"):
                    result_sign = "1"
                else:
                    result_sign = "0"
                result = FPZero(datasize, result_sign)
            else:
                result = FPRound(result_value, rounding, datasize)

    return result

def negFP(op, datasize):
    if(op[0] == '0'):
        sign = '1'
    else:
        sign = '0'

    return sign + op[1:datasize]

def maxFP(op1, op2, datasize):
    rounding = FPDecodeRounding(getRoundingBits())

    (type1, sign1, value1) = unpackFP(op1, datasize)
    (type2, sign2, value2) = unpackFP(op2, datasize)

    (done, result) = FPProcessNaNs(type1, type2, op1, op2,datasize)

    if(not done):
        if(value1 > value2):
            (typeOfVal,sign,value) = (type1,sign1,value1)
        else:
            (typeOfVal,sign,value) = (type2,sign2,value2)

        if(typeOfVal == "FPType_Infinity"):
            result = FPInfinity(datasize, sign)
        elif(typeOfVal == "FPType_Zero"):
            sign = logical_and(sign1,sign2)
            result = FPZero(datasize, sign)
        else:
            result = FPRound(value, rounding, datasize)

    return result

def minFP(op1, op2, datasize):
    rounding = FPDecodeRounding(getRoundingBits())

    (type1, sign1, value1) = unpackFP(op1, datasize)
    (type2, sign2, value2) = unpackFP(op2, datasize)

    (done, result) = FPProcessNaNs(type1, type2, op1, op2,datasize)

    if(not done):
        if(value1 < value2):
            (typeOfVal,sign,value) = (type1,sign1,value1)
        else:
            (typeOfVal,sign,value) = (type2,sign2,value2)

        if(typeOfVal == "FPType_Infinity"):
            result = FPInfinity(datasize, sign)
        elif(typeOfVal == "FPType_Zero"):
            sign = logical_or(sign1,sign2)
            result = FPZero(datasize, sign)
        else:
            result = FPRound(value, rounding, datasize)

    return result