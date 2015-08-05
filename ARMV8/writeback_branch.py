'''
Created on Aug 8, 2014

@author: abhishek
'''

import utilFunc
import const
#from utilFunc import uInt, signExtend, getRegValueByStringkey
import armdebug

def writebackB(binary):
    const.FLAG_WRITEBACK_EXECUTED = True
    
def writebackBCond(binary):
    const.FLAG_WRITEBACK_EXECUTED = True
    
def writebackBL(binary):
    const.FLAG_WRITEBACK_EXECUTED = True
    
def writebackBR(binary):
    const.FLAG_WRITEBACK_EXECUTED = True
    
def writebackBLR(binary):
    const.FLAG_WRITEBACK_EXECUTED = True
    
def writebackRET(binary):
    const.FLAG_WRITEBACK_EXECUTED = True
    
def writebackCBZ_32(binary):
    CBZClass(binary, 32, True)
    
def writebackCBNZ_32(binary):
    CBZClass(binary, 32, False)
    
def writebackCBZ_64(binary):
    CBZClass(binary, 64, True)
    
def writebackCBNZ_64(binary):
    CBZClass(binary, 64, False)

def CBZClass(binary,width,bool):
    const.FLAG_WRITEBACK_EXECUTED = True