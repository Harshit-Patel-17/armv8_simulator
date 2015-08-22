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
import memaccess_rotate
import memaccess_bitwise_shift
import memaccess_adc
import memaccess_moveWide
import memaccess_FP_addSub
import memaccess_FP_maxMin

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
            14 : ROTATE_IMMEDIATE,
            15 : ROTATE_REGISTER,
            16 : BITWISE_SHIFT_REGISTER,
            17 : ADD_WITH_CARRY,
            18 : MOVE_WIDE,
            19 : FLOATING_POINT_ADD_SUB,
            20 : FLOATING_POINT_MOVE_IMMEDIATE,
            21 : FLOATING_POINT_MAX_MIN,
            22 : FLOATING_POINT_MOVE_REGISTER,
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
      "00111010010---------10"      : memaccess_conditional.memaccessConditionalCompareNegative_i32,
      "10111010010---------10"      : memaccess_conditional.memaccessConditionalCompareNegative_i64,
      "00111010010---------00"      : memaccess_conditional.memaccessConditionalCompareNegative_r32,
      "10111010010---------00"      : memaccess_conditional.memaccessConditionalCompareNegative_r64,
    }[key](binary)

def MORE_ALU(binary):
    key = binary[0:22]
    return {
      "0101101011000000000101"  : memaccess_ALU.memaccessCLS_32,
      "1101101011000000000101"  : memaccess_ALU.memaccessCLS_64,
      "0101101011000000000100"  : memaccess_ALU.memaccessCLZ_32,
      "1101101011000000000100"  : memaccess_ALU.memaccessCLZ_64,
    }[key](binary)

def ROTATE_IMMEDIATE(binary):
    key = binary[0:11]
    return {
      "00010011100"  : memaccess_rotate.memaccessRotate_i32,
      "10010011110"  : memaccess_rotate.memaccessRotate_i64,
    }[key](binary)

def ROTATE_REGISTER(binary):
    key = binary[0:11] + "-"*5 + binary[16:22]
    return {
      "00011010110-----001011"  : memaccess_rotate.memaccessRotate_r32,
      "10011010110-----001011"  : memaccess_rotate.memaccessRotate_r64,
    }[key](binary)

def BITWISE_SHIFT_REGISTER(binary):
    key = binary[0:8] + "-"*2 + binary[10:11]
    return {
      "00001010--1" : memaccess_bitwise_shift.memaccessBitwiseShift_32,
      "10001010--1" : memaccess_bitwise_shift.memaccessBitwiseShift_64,
      "01101010--1" : memaccess_bitwise_shift.memaccessBitwiseShiftSetFlags_32,
      "11101010--1" : memaccess_bitwise_shift.memaccessBitwiseShiftSetFlags_64,
    }[key](binary)

def ADD_WITH_CARRY(binary):
    key = binary[0:11] + "-"*5 + binary[16:22]
    return {
      "00011010000-----000000"  : memaccess_adc.memaccessADC_32,
      "10011010000-----000000"  : memaccess_adc.memaccessADC_64,
    }[key](binary)

def MOVE_WIDE(binary):
    key = binary[0:9]
    return {
      "011100101" : memaccess_moveWide.memaccessMoveK_32,
      "111100101" : memaccess_moveWide.memaccessMoveK_64,
      "000100101" : memaccess_moveWide.memaccessMoveN_32,
      "100100101" : memaccess_moveWide.memaccessMoveN_64,
      "010100101" : memaccess_moveWide.memaccessMoveZ_32,
      "110100101" : memaccess_moveWide.memaccessMoveZ_64,
    }[key](binary)
    
def FLOATING_POINT_MOVE_IMMEDIATE(binary):
    key = binary[0:11] + "-"*8 + binary[19:27]
    return {
      "00011110001--------10000000" : memaccess_move.memaccessFMove_iSP,
      "00011110011--------10000000" : memaccess_move.memaccessFMove_iDP,
    }[key](binary)

def FLOATING_POINT_ADD_SUB(binary):
  key = binary[0:11] + "-"*5 + binary[16:22]
  return {
    "00011110001-----001010" :  memaccess_FP_addSub.memaccessFADD_scalar_SP,
    "00011110011-----001010" :  memaccess_FP_addSub.memaccessFADD_scalar_DP,
    "00001110001-----110101" :  memaccess_FP_addSub.memaccessFADD_vector_2S,
    "01001110001-----110101" :  memaccess_FP_addSub.memaccessFADD_vector_4S,
    "01001110011-----110101" :  memaccess_FP_addSub.memaccessFADD_vector_2D,
    "00011110001-----001110" :  memaccess_FP_addSub.memaccessFSUB_scalar_SP,
    "00011110011-----001110" :  memaccess_FP_addSub.memaccessFSUB_scalar_DP,
    "00001110101-----110101" :  memaccess_FP_addSub.memaccessFSUB_vector_2S,
    "01001110101-----110101" :  memaccess_FP_addSub.memaccessFSUB_vector_4S,
    "01001110111-----110101" :  memaccess_FP_addSub.memaccessFSUB_vector_2D,
  }[key](binary)

def FLOATING_POINT_MAX_MIN(binary):
  key = binary[0:11] + "-"*5 + binary[16:22]
  return {
    "00011110001-----010010" :  memaccess_FP_maxMin.memaccessFMAX_scalar_SP,
    "00011110011-----010010" :  memaccess_FP_maxMin.memaccessFMAX_scalar_DP,
    "00001110001-----111101" :  memaccess_FP_maxMin.memaccessFMAX_vector_2S,
    "01001110001-----111101" :  memaccess_FP_maxMin.memaccessFMAX_vector_4S,
    "01001110011-----111101" :  memaccess_FP_maxMin.memaccessFMAX_vector_2D,
    "00011110001-----010110" :  memaccess_FP_maxMin.memaccessFMIN_scalar_SP,
    "00011110011-----010110" :  memaccess_FP_maxMin.memaccessFMIN_scalar_DP,
    "00001110101-----111101" :  memaccess_FP_maxMin.memaccessFMIN_vector_2S,
    "01001110101-----111101" :  memaccess_FP_maxMin.memaccessFMIN_vector_4S,
    "01001110111-----111101" :  memaccess_FP_maxMin.memaccessFMIN_vector_2D,
  }[key](binary)

def FLOATING_POINT_MOVE_REGISTER(binary):
  key = binary[0:22]
  return {
    "0001111000100000010000" :  memaccess_move.memaccessFMove_regSP,
    "0001111001100000010000" :  memaccess_move.memaccessFMove_regDP,
    "0001111000100111000000" :  memaccess_move.memaccessFMove_32toSP,
    "0001111000100110000000" :  memaccess_move.memaccessFMove_SPto32,
    "1001111001100111000000" :  memaccess_move.memaccessFMove_64toDP,
    "1001111010101111000000" :  memaccess_move.memaccessFMove_64to128,
    "1001111001100110000000" :  memaccess_move.memaccessFMove_DPto64,
    "1001111010101110000000" :  memaccess_move.memaccessFMove_128to64,
  }[key](binary)