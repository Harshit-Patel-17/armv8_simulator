'''
@author: harinder
'''
import writeback_addSub
import writeback_logical
import writeback_move
import writeback_shift
import writeback_misc
import writeback_mulDiv
import writeback_conditional
import writeback_ALU
import writeback_rotate
import writeback_bitwise_shift
import writeback_adc
import writeback_moveWide
import writeback_FP_addSub
import writeback_FP_maxMin

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
       "00010001" : writeback_addSub.writebackAdd_i32,
       "00110001" : writeback_addSub.writebackAdds_i32,
       "01010001" : writeback_addSub.writebackSub_i32,
       "01110001" : writeback_addSub.writebackSubs_i32,
       "10010001" : writeback_addSub.writebackAdd_i64,
       "10110001" : writeback_addSub.writebackAdds_i64,
       "11010001" : writeback_addSub.writebackSub_i64,
       "11110001" : writeback_addSub.writebackSubs_i64,
    }[key](binary)
      
def ADD_SUB_SHIFT_REG(binary):
    key = binary[0:8] + "--" + binary[10]
    return {
       "00001011--0" : writeback_addSub.writebackAdd_sr32,
       "00101011--0" : writeback_addSub.writebackAdds_sr32,
       "01001011--0" : writeback_addSub.writebackSub_sr32,
       "01101011--0" : writeback_addSub.writebackSubs_sr32,
       "10001011--0" : writeback_addSub.writebackAdd_sr64,
       "10101011--0" : writeback_addSub.writebackAdds_sr64,
       "11001011--0" : writeback_addSub.writebackSub_sr64,
       "11101011--0" : writeback_addSub.writebackSubs_sr64,
    }[key](binary)
    
def ADD_SUB_EXT_REG(binary):
    key = binary[0:11]
    return {
       "00001011001" : writeback_addSub.writebackAdd_er32,
       "00101011001" : writeback_addSub.writebackAdds_er32,
       "01001011001" : writeback_addSub.writebackSub_er32,
       "01101011001" : writeback_addSub.writebackSubs_er32,
       "10001011001" : writeback_addSub.writebackAdd_er64,
       "10101011001" : writeback_addSub.writebackAdds_er64,
       "11001011001" : writeback_addSub.writebackSub_er64,
       "11101011001" : writeback_addSub.writebackSubs_er64,
    }[key](binary) 
    
    
def LOGICAL_IMMEDIATE(binary):
    key = binary[0:9]
    return {
       "000100100" : writeback_logical.writebackAnd_i32,
       "100100100" : writeback_logical.writebackAnd_i64,
       "011100100" : writeback_logical.writebackAnds_i32,
       "111100100" : writeback_logical.writebackAnds_i64,
    }[key](binary)
    
def LOGICAL_SHIFT_REG(binary):
    key = binary[0:8] + "--" + binary[10]
    return {
       "00001010--0" : writeback_logical.writebackAnd_sr32,
       "10001010--0" : writeback_logical.writebackAnd_sr64,
       "01101010--0" : writeback_logical.writebackAnds_sr32,
       "11101010--0" : writeback_logical.writebackAnds_sr64,
    }[key](binary)


def MOVE_IMMEDIATE(binary):
    key = binary[0:9]
    return {
       "000100101" : writeback_move.writebackMov_iwi32,
       "100100101" : writeback_move.writebackMov_iwi64,
       "010100101" : writeback_move.writebackMov_wi32,
       "110100101" : writeback_move.writebackMov_wi64,
       "001100100" : writeback_move.writebackMov_bmi32,
       "101100100" : writeback_move.writebackMov_bmi64,
    }[key](binary)
    
def MOVE_REGISTER(binary):
    key = binary[0:11] + "-"*5 + binary[16:27]
    return {
       "00101010000-----00000011111" : writeback_move.writebackMov_r32,
       "10101010000-----00000011111" : writeback_move.writebackMov_r64,
    }[key](binary)


def SHIFT_REGISTER(binary):
    key = binary[0:11] + "-"*5 + binary[16:22]
    return {
       "00011010110-----001010" : writeback_shift.writebackAsr_r32,
       "10011010110-----001010" : writeback_shift.writebackAsr_r64,
       "00011010110-----001000" : writeback_shift.writebackLsl_r32,
       "10011010110-----001000" : writeback_shift.writebackLsl_r64,
       "00011010110-----001001" : writeback_shift.writebackLsr_r32,
       "10011010110-----001001" : writeback_shift.writebackLsr_r64,
    }[key](binary)
    
def SHIFT_IMMEDIATE(binary):
    key = binary[0:10]
    return {
       "0001001100" : writeback_shift.writebackAsr_i32,
       "1001001101" : writeback_shift.writebackAsr_i64,
       "0101001100" : writeback_shift.writebackLslLsr_i32,
       "1101001101" : writeback_shift.writebackLslLsr_i64,
    }[key](binary)

def PC_RELATIVE(binary):
    key = binary[0] + "--" + binary[3:8]
    return {       
       "0--10000" : writeback_misc.writebackADR,
       "1--10000" : writeback_misc.writebackADRP,
    }[key](binary)
    
def NOP(binary):
    key = binary[0:20] + "-"*7 + binary[27:32]
    return {
       "11010101000000110010" + "-"*7 + "11111" : writeback_misc.writebackNOP,
    }[key](binary)

def MUL_DIV_REG(binary):
    key = binary[0:11] + "-"*5 + binary[16:22]
    return {
      "10011011101-----011111" : writeback_mulDiv.writebackMul,
      "00011010110-----000010" : writeback_mulDiv.writebackUnsignedDiv_32,
      "10011010110-----000010" : writeback_mulDiv.writebackUnsignedDiv_64,
      "00011010110-----000011" : writeback_mulDiv.writebackSignedDiv_32,
      "10011010110-----000011" : writeback_mulDiv.writebackSignedDiv_64,
    }[key](binary)

def CONDITIONAL_INSTRUCTIONS(binary):
    if(binary[11:16] == "11111" and binary[22:27] == "11111"):
        key = binary[0:16] + "-"*4 + binary[20:27]
    else:
        key = binary[0:11] + "-"*9 + binary[20:22]
    return {
      "0001101010011111----0111111" : writeback_conditional.writebackConditionalSet_32,
      "1001101010011111----0111111" : writeback_conditional.writebackConditionalSet_64,
      "01011010100---------00"      : writeback_conditional.writebackConditionalSelectInverse_32,
      "11011010100---------00"      : writeback_conditional.writebackConditionalSelectInverse_64,
      "01011010100---------01"      : writeback_conditional.writebackConditionalSelectNegation_32,
      "11011010100---------01"      : writeback_conditional.writebackConditionalSelectNegation_64,
      "00011010100---------01"      : writeback_conditional.writebackConditionalSelectIncrement_32,
      "10011010100---------01"      : writeback_conditional.writebackConditionalSelectIncrement_64,
      "00111010010---------10"      : writeback_conditional.writebackConditionalCompareNegative_i32,
      "10111010010---------10"      : writeback_conditional.writebackConditionalCompareNegative_i64,
      "00111010010---------00"      : writeback_conditional.writebackConditionalCompareNegative_r32,
      "10111010010---------00"      : writeback_conditional.writebackConditionalCompareNegative_r64,
    }[key](binary)

def MORE_ALU(binary):
    key = binary[0:22]
    return {
      "0101101011000000000101"  : writeback_ALU.writebackCLS_32,
      "1101101011000000000101"  : writeback_ALU.writebackCLS_64,
      "0101101011000000000100"  : writeback_ALU.writebackCLZ_32,
      "1101101011000000000100"  : writeback_ALU.writebackCLZ_64,
    }[key](binary)

def ROTATE_IMMEDIATE(binary):
    key = binary[0:11]
    return {
      "00010011100"  : writeback_rotate.writebackRotate_i32,
      "10010011110"  : writeback_rotate.writebackRotate_i64,
    }[key](binary)

def ROTATE_REGISTER(binary):
    key = binary[0:11] + "-"*5 + binary[16:22]
    return {
      "00011010110-----001011"  : writeback_rotate.writebackRotate_r32,
      "10011010110-----001011"  : writeback_rotate.writebackRotate_r64,
    }[key](binary)

def BITWISE_SHIFT_REGISTER(binary):
    key = binary[0:8] + "-"*2 + binary[10:11]
    return {
      "00001010--1" : writeback_bitwise_shift.writebackBitwiseShift_32,
      "10001010--1" : writeback_bitwise_shift.writebackBitwiseShift_64,
      "01101010--1" : writeback_bitwise_shift.writebackBitwiseShiftSetFlags_32,
      "11101010--1" : writeback_bitwise_shift.writebackBitwiseShiftSetFlags_64,
    }[key](binary)

def ADD_WITH_CARRY(binary):
    key = binary[0:11] + "-"*5 + binary[16:22]
    return {
      "00011010000-----000000"  : writeback_adc.writebackADC_32,
      "10011010000-----000000"  : writeback_adc.writebackADC_64,
    }[key](binary)

def MOVE_WIDE(binary):
    key = binary[0:9]
    return {
      "011100101" : writeback_moveWide.writebackMoveK_32,
      "111100101" : writeback_moveWide.writebackMoveK_64,
      "000100101" : writeback_moveWide.writebackMoveN_32,
      "100100101" : writeback_moveWide.writebackMoveN_64,
      "010100101" : writeback_moveWide.writebackMoveZ_32,
      "110100101" : writeback_moveWide.writebackMoveZ_64,
    }[key](binary)
    
def FLOATING_POINT_MOVE_IMMEDIATE(binary):
    key = binary[0:11] + "-"*8 + binary[19:27]
    return {
      "00011110001--------10000000" : writeback_move.writebackFMove_iSP,
      "00011110011--------10000000" : writeback_move.writebackFMove_iDP,
    }[key](binary)

def FLOATING_POINT_ADD_SUB(binary):
  key = binary[0:11] + "-"*5 + binary[16:22]
  return {
    "00011110001-----001010" :  writeback_FP_addSub.writebackFADD_scalar_SP,
    "00011110011-----001010" :  writeback_FP_addSub.writebackFADD_scalar_DP,
    "00001110001-----110101" :  writeback_FP_addSub.writebackFADD_vector_2S,
    "01001110001-----110101" :  writeback_FP_addSub.writebackFADD_vector_4S,
    "01001110011-----110101" :  writeback_FP_addSub.writebackFADD_vector_2D,
    "00011110001-----001110" :  writeback_FP_addSub.writebackFSUB_scalar_SP,
    "00011110011-----001110" :  writeback_FP_addSub.writebackFSUB_scalar_DP,
    "00001110101-----110101" :  writeback_FP_addSub.writebackFSUB_vector_2S,
    "01001110101-----110101" :  writeback_FP_addSub.writebackFSUB_vector_4S,
    "01001110111-----110101" :  writeback_FP_addSub.writebackFSUB_vector_2D,
  }[key](binary)

def FLOATING_POINT_MAX_MIN(binary):
  key = binary[0:11] + "-"*5 + binary[16:22]
  return {
    "00011110001-----010010" :  writeback_FP_maxMin.writebackFMAX_scalar_SP,
    "00011110011-----010010" :  writeback_FP_maxMin.writebackFMAX_scalar_DP,
    "00001110001-----111101" :  writeback_FP_maxMin.writebackFMAX_vector_2S,
    "01001110001-----111101" :  writeback_FP_maxMin.writebackFMAX_vector_4S,
    "01001110011-----111101" :  writeback_FP_maxMin.writebackFMAX_vector_2D,
    "00011110001-----010110" :  writeback_FP_maxMin.writebackFMIN_scalar_SP,
    "00011110011-----010110" :  writeback_FP_maxMin.writebackFMIN_scalar_DP,
    "00001110101-----111101" :  writeback_FP_maxMin.writebackFMIN_vector_2S,
    "01001110101-----111101" :  writeback_FP_maxMin.writebackFMIN_vector_4S,
    "01001110111-----111101" :  writeback_FP_maxMin.writebackFMIN_vector_2D,
  }[key](binary)

def FLOATING_POINT_MOVE_REGISTER(binary):
  key = binary[0:22]
  return {
    "0001111000100000010000" :  writeback_move.writebackFMove_regSP,
    "0001111001100000010000" :  writeback_move.writebackFMove_regDP,
    "0001111000100111000000" :  writeback_move.writebackFMove_32toSP,
    "0001111000100110000000" :  writeback_move.writebackFMove_SPto32,
    "1001111001100111000000" :  writeback_move.writebackFMove_64toDP,
    "1001111010101111000000" :  writeback_move.writebackFMove_64to128,
    "1001111001100110000000" :  writeback_move.writebackFMove_DPto64,
    "1001111010101110000000" :  writeback_move.writebackFMove_128to64,
  }[key](binary)