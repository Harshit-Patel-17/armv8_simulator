'''
@author: harinder
'''
import memaccess_addSub
import memaccess_logical
import memaccess_move
import memaccess_shift
import memaccess_misc
import memaccess_mulDiv
import memaccess_conditional
import memaccess_ALU
import memaccess_bitwise_shift

def INSTRUCTION_TYPE(binary, i):
    try:
        return {
            0 : ADD_SUB_IMMEDIATE,
            1 : MOVE_IMMEDIATE,
            2 : MOVE_REGISTER,
            3 : ADD_SUB_EXT_REG,
            4 : ADD_SUB_SHIFT_REG,
            5 : LOGICAL_SHIFT_REG,
            6 : SHIFT_REGISTER,
            7 : SHIFT_IMMEDIATE,
            8 : LOGICAL_IMMEDIATE,
            9 : PC_RELATIVE,
            10 : NOP,
            11 : MUL_DIV_REG,
            12 : CONDITIONAL_INSTRUCTIONS,
            13 : MORE_ALU,
            16: BITWISE_SHIFT_REGISTER
        }[i](binary)
    except KeyError:
        i = i

def ADD_SUB_IMMEDIATE(binary):
    key = binary[0:8] 
    return {
       "00010001" : memaccess_addSub.memaccessAdd_i32,
       "00110001" : memaccess_addSub.memaccessAdds_i32,
       "01010001" : memaccess_addSub.memaccessSub_i32,
       "01110001" : memaccess_addSub.memaccessSubs_i32,
       "10010001" : memaccess_addSub.memaccessAdd_i64,
       "10110001" : memaccess_addSub.memaccessAdds_i64,
       "11010001" : memaccess_addSub.memaccessSub_i64,
       "11110001" : memaccess_addSub.memaccessSubs_i64,
    }[key](binary)
      
def ADD_SUB_SHIFT_REG(binary):
    key = binary[0:8] + "--" + binary[10]
    return {
       "00001011--0" : memaccess_addSub.memaccessAdd_sr32,
       "00101011--0" : memaccess_addSub.memaccessAdds_sr32,
       "01001011--0" : memaccess_addSub.memaccessSub_sr32,
       "01101011--0" : memaccess_addSub.memaccessSubs_sr32,
       "10001011--0" : memaccess_addSub.memaccessAdd_sr64,
       "10101011--0" : memaccess_addSub.memaccessAdds_sr64,
       "11001011--0" : memaccess_addSub.memaccessSub_sr64,
       "11101011--0" : memaccess_addSub.memaccessSubs_sr64,
    }[key](binary)
    
def ADD_SUB_EXT_REG(binary):
    key = binary[0:11]
    return {
       "00001011001" : memaccess_addSub.memaccessAdd_er32,
       "00101011001" : memaccess_addSub.memaccessAdds_er32,
       "01001011001" : memaccess_addSub.memaccessSub_er32,
       "01101011001" : memaccess_addSub.memaccessSubs_er32,
       "10001011001" : memaccess_addSub.memaccessAdd_er64,
       "10101011001" : memaccess_addSub.memaccessAdds_er64,
       "11001011001" : memaccess_addSub.memaccessSub_er64,
       "11101011001" : memaccess_addSub.memaccessSubs_er64,
    }[key](binary) 
    
    
def LOGICAL_IMMEDIATE(binary):
    key = binary[0:9]
    return {
       "000100100" : memaccess_logical.memaccessAnd_i32,
       "100100100" : memaccess_logical.memaccessAnd_i64,
       "011100100" : memaccess_logical.memaccessAnds_i32,
       "111100100" : memaccess_logical.memaccessAnds_i64,
    }[key](binary)
    
def LOGICAL_SHIFT_REG(binary):
    key = binary[0:8] + "--" + binary[10]
    return {
       "00001010--0" : memaccess_logical.memaccessAnd_sr32,
       "10001010--0" : memaccess_logical.memaccessAnd_sr64,
       "01101010--0" : memaccess_logical.memaccessAnds_sr32,
       "11101010--0" : memaccess_logical.memaccessAnds_sr64,
    }[key](binary)


def MOVE_IMMEDIATE(binary):
    key = binary[0:9]
    return {
       "000100101" : memaccess_move.memaccessMov_iwi32,
       "100100101" : memaccess_move.memaccessMov_iwi64,
       "010100101" : memaccess_move.memaccessMov_wi32,
       "110100101" : memaccess_move.memaccessMov_wi64,
       "001100100" : memaccess_move.memaccessMov_bmi32,
       "101100100" : memaccess_move.memaccessMov_bmi64,
    }[key](binary)
    
def MOVE_REGISTER(binary):
    key = binary[0:11] + "-"*5 + binary[16:27]
    return {
       "00101010000-----00000011111" : memaccess_move.memaccessMov_r32,
       "10101010000-----00000011111" : memaccess_move.memaccessMov_r64,
    }[key](binary)


def SHIFT_REGISTER(binary):
    key = binary[0:11] + "-"*5 + binary[16:22]
    return {
       "00011010110-----001010" : memaccess_shift.memaccessAsr_r32,
       "10011010110-----001010" : memaccess_shift.memaccessAsr_r64,
       "00011010110-----001000" : memaccess_shift.memaccessLsl_r32,
       "10011010110-----001000" : memaccess_shift.memaccessLsl_r64,
       "00011010110-----001001" : memaccess_shift.memaccessLsr_r32,
       "10011010110-----001001" : memaccess_shift.memaccessLsr_r64,
    }[key](binary)
    
def SHIFT_IMMEDIATE(binary):
    key = binary[0:10]
    return {
       "0001001100" : memaccess_shift.memaccessAsr_i32,
       "1001001101" : memaccess_shift.memaccessAsr_i64,
       "0101001100" : memaccess_shift.memaccessLslLsr_i32,
       "1101001101" : memaccess_shift.memaccessLslLsr_i64,
    }[key](binary)

def PC_RELATIVE(binary):
    key = binary[0] + "--" + binary[3:8]
    return {       
       "0--10000" : memaccess_misc.memaccessADR,
       "1--10000" : memaccess_misc.memaccessADRP,
    }[key](binary)
    
def NOP(binary):
    key = binary[0:20] + "-"*7 + binary[27:32]
    return {
       "11010101000000110010" + "-"*7 + "11111" : memaccess_misc.memaccessNOP,
    }[key](binary)

def MUL_DIV_REG(binary):
    key = binary[0:11] + "-"*5 + binary[16:22]
    return {
      "10011011101-----011111" : memaccess_mulDiv.memaccessMul,
      "00011010110-----000010" : memaccess_mulDiv.memaccessUnsignedDiv_32,
      "10011010110-----000010" : memaccess_mulDiv.memaccessUnsignedDiv_64,
      "00011010110-----000011" : memaccess_mulDiv.memaccessSignedDiv_32,
      "10011010110-----000011" : memaccess_mulDiv.memaccessSignedDiv_64,
    }[key](binary)

def CONDITIONAL_INSTRUCTIONS(binary):
    if(binary[11:16] == "11111" and binary[22:27] == "11111"):
        key = binary[0:16] + "-"*4 + binary[20:27]
    else:
        key = binary[0:11] + "-"*9 + binary[20:22]
    return {
      "0001101010011111----0111111" : memaccess_conditional.memaccessConditionalSet_32,
      "1001101010011111----0111111" : memaccess_conditional.memaccessConditionalSet_64,
      "01011010100---------00"      : memaccess_conditional.memaccessConditionalSelectInverse_32,
      "11011010100---------00"      : memaccess_conditional.memaccessConditionalSelectInverse_64,
      "01011010100---------01"      : memaccess_conditional.memaccessConditionalSelectNegation_32,
      "11011010100---------01"      : memaccess_conditional.memaccessConditionalSelectNegation_64,
      "00011010100---------01"      : memaccess_conditional.memaccessConditionalSelectIncrement_32,
      "10011010100---------01"      : memaccess_conditional.memaccessConditionalSelectIncrement_64,
    }[key](binary)

def MORE_ALU(binary):
    key = binary[0:22]
    return {
      "0101101011000000000101"  : memaccess_ALU.memaccessCLS_32,
      "1101101011000000000101"  : memaccess_ALU.memaccessCLS_64,
      "0101101011000000000100"  : memaccess_ALU.memaccessCLZ_32,
      "1101101011000000000100"  : memaccess_ALU.memaccessCLZ_64,
    }[key](binary)

def BITWISE_SHIFT_REGISTER(binary):
    key = binary[0:8] + "-"*2 + binary[10:11]
    return {
      "00001010--1" : memaccess_bitwise_shift.memaccessBitwiseShift_32,
      "10001010--1" : memaccess_bitwise_shift.memaccessBitwiseShift_64,
      "01101010--1" : memaccess_bitwise_shift.memaccessBitwiseShiftSetFlags_32,
      "11101010--1" : memaccess_bitwise_shift.memaccessBitwiseShiftSetFlags_64,
    }[key](binary)