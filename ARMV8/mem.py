'''
Created on Aug 8, 2014

@author: harinder
'''

regNum=31
#31st register is used for SP
regFile = list('0'*64 for i in range(32))
#flags-order: n,z,c,v
flagFile = list('0' for i in range(4))

memory_model={}

watchReg = list(False for i in range(regNum))


def setWatchForReg(index):
    del regFile[index]
    regFile[index]=True
    
def resetWatchForReg(index):
    del regFile[index]
    regFile[index]=False    

def setGlobalDataMemory(startAddress, list):
    pass

#both are hex strings 
#assume data is 4 bytes here
def storeWordToMemory(address, data):
    global memory_model
    memory_model[address]=data
    
def printMemoryState():
    print memory_model