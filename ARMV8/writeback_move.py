'''
Created on Aug 8, 2014

@author: harinder
'''
import const
import utilFunc
import mem


def writebackMov_iwi32(binary):
    mov_imm(binary, "MOV w", '1', 32)
    
def writebackMov_iwi64(binary):
    mov_imm(binary, "MOV x", '1', 64)
    
def writebackMov_wi32(binary):
    mov_imm(binary, "MOV w", '0', 32)
    
def writebackMov_wi64(binary):
    mov_imm(binary, "MOV x", '0', 64)
    
def mov_imm(binary, instr, inverted, N):   
    const.FLAG_WRITEBACK_EXECUTED = True

def mov_reg(binary, N):
    const.FLAG_WRITEBACK_EXECUTED = True

def writebackMov_r32(binary):
    mov_reg(binary, 32)
    
def writebackMov_r64(binary):
    mov_reg(binary, 64)
                           
                           
def mov_bmi(binary, N):
    const.FLAG_WRITEBACK_EXECUTED = True
    
def writebackMov_bmi32(binary):
    mov_bmi(binary, 32)
    
def writebackMov_bmi64(binary):
    mov_bmi(binary, 64)
