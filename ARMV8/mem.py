'''
Created on Aug 8, 2014

@author: harinder
'''
import parsehelper, const

regNum=32
#31st register is used for SP
regFile = list('0'*64 for i in range(regNum))

#Indicates whether register value is obsolete for use by next instructions
regObsolete = list(0 for i in range(regNum))
regObsolete_last_modified_indices = []

#Indicates whether register value is available in ALUResultBuffer for use by next instructions
regValueAvailableInALU = list(False for i in range(regNum))
regValueAvailableInALU_last_modified_indices = []

#indicates whether register value is available in WritebackBuffer fir use by next instructions
regValueAvailableInWB = list(False for i in range(regNum))
regValueAvailableinWB_last_modified_indices = []
regValueAvailableInWB_buffer_indices = list(-1 for i in range(regNum))

#Operand buffers
operand1Buffer = ''
operand2Buffer = ''

#Buffer to store result generated by ALU
ALUResultBuffer = ''
isSPBuffer = ''

#Buffer to store result for Write-Back
writeBackBuffer = ['', '', '']
isSPWriteBackBuffer = ''

#Interstage data buffers
IF_ID_dataBuffer = []
ID_EX_dataBuffer = []
EX_MA_dataBuffer = []
MA_WB_dataBuffer = []

#flags-order: n,z,c,v
flagFile = list('0' for i in range(4))

memory_model={}

helper_memory_model={}

watchReg = list(False for i in range(regNum))

def findForwardedValues(operandRegister1, operandRegister2 = None, operandRegister3 = None):
    regValue1 = None
    regValue2 = None
    regValue3 = None
    if(regValueAvailableInALU[operandRegister1]):
        regValue1 = ALUResultBuffer
    elif(regValueAvailableInWB[operandRegister1]):
        regValue1 = writeBackBuffer[regValueAvailableInWB_buffer_indices[operandRegister1]]
        
    if(operandRegister2 != None):
        if(regValueAvailableInALU[operandRegister2]):
            regValue2 = ALUResultBuffer
        elif(regValueAvailableInWB[operandRegister2]):
            regValue2 = writeBackBuffer[regValueAvailableInWB_buffer_indices[operandRegister2]]
            
    if(operandRegister3 != None):
        if(regValueAvailableInALU[operandRegister3]):
            regValue3 = ALUResultBuffer
        elif(regValueAvailableInWB[operandRegister3]):
            regValue3 = writeBackBuffer[regValueAvailableInWB_buffer_indices[operandRegister3]]
    
    return [regValue1, regValue2, regValue3]

def freeObsoleteRegisters():
    for index in regObsolete_last_modified_indices:
        regObsolete[index] = False
    regObsolete_last_modified_indices = []


def setWatchForReg(index):
    global watchReg
    del watchReg[index]
    watchReg.insert(index, True)
    
def resetWatchForReg(index):
    global watchReg
    del watchReg[index]
    watchReg.insert(index, False)
    
def printWatchStateAll():
    global watchReg
    
#regKey should be the correct index of the register 0 to 31
#watch on stack pointer too?
def isWatchSet(regKey):
    global watchReg
    return watchReg[regKey]


#will have to use int for address!!!
#data is 4 bytes here in a 8 hexit string like 09090909

def storeWordToMemory(address, data):
    #print 'being called here'
    global memory_model
    memory_model[address]=data
    storeWordToHelperMemory(address, data)
    
def storeWordToHelperMemory(address,data):
    global helper_memory_model
    #data is 8 hexit : 01020304
    #spilt first
    list=[data[0:2],data[2:4],data[4:6],data[6:8]]
    if parsehelper.isLittle():
        list.reverse()
    #print list
    #now each data is 2 hexit
    helper_memory_model[address]=list[0]
    helper_memory_model[address+1]=list[1]
    helper_memory_model[address+2]=list[2]
    helper_memory_model[address+3]=list[3]
    
def fetchByteFromHelperMemory(address):
    global helper_memory_model
    try:
        return helper_memory_model[address]
    except KeyError:
        return const.TRAP
    
#give an int equivalent of address
#will fetch only a word
def fetchWordFromMemory(address):
    global memory_model
    try:
        return memory_model[address]
    except KeyError:
        return const.TRAP
    
def printMemoryState():
    global memory_model
    print memory_model
    printHelperMemoryState()
    
def printHelperMemoryState():
    global helper_memory_model
    print helper_memory_model
    
def init():
    global regFile, flagFile, memory_model, regNum, watchReg
    regNum=31

    regFile = list('0'*64 for i in range(regNum))
    #flags-order: n,z,c,v
    flagFile = list('0' for i in range(4))

    memory_model={}

    watchReg = list(False for i in range(regNum))