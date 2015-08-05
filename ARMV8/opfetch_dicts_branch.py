'''
@author: harinder
'''
import opfetch_branch

def INSTRUCTION_TYPE(binary,i):
    try:
        return {
            0 : UNCONDITIONAL_BRANCH_IMMEDIATE,
            1 : UNCONDITIONAL_BRANCH_REGISTER,
            2 : CONDITIONAL_BRANCH_IMMEDIATE,
            3 : COMPARE_AND_BRANCH_IMMEDIATE,
        }[i](binary)
    except KeyError:
        i=i
    
def UNCONDITIONAL_BRANCH_IMMEDIATE(binary):
    key = binary[0:6]
    return {
       "000101" : opfetch_branch.opfetchB,
       "100101" : opfetch_branch.opfetchBL,
    }[key](binary)
    
def UNCONDITIONAL_BRANCH_REGISTER(binary):
    key = binary[0:22]+"-"*5+binary[27:32]
    return {
       "1101011000011111000000-----00000" : opfetch_branch.opfetchBR,
       "1101011000111111000000-----00000" : opfetch_branch.opfetchBLR,
       "1101011001011111000000-----00000" : opfetch_branch.opfetchRET,
    }[key](binary)
    
def CONDITIONAL_BRANCH_IMMEDIATE(binary):
    key = binary[0:8]+"-"*19+binary[27]
    return {
       "01010100"+"-"*19+"0" : opfetch_branch.opfetchBCond,
    }[key](binary)
    
def COMPARE_AND_BRANCH_IMMEDIATE(binary):
    key = binary[0:8]
    return {
       "00110100" : opfetch_branch.opfetchCBZ_32,
       "00110101" : opfetch_branch.opfetchCBNZ_32,
       "10110100" : opfetch_branch.opfetchCBZ_64,
       "10110101" : opfetch_branch.opfetchCBNZ_64,
    }[key](binary)
