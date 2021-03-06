'''
@author: harinder
'''
import opfetch_addSub
import opfetch_logical
import opfetch_move
import opfetch_shift
import opfetch_misc
import opfetch_mulDiv
import opfetch_conditional
import opfetch_ALU
import opfetch_rotate
import opfetch_bitwise_shift
import opfetch_adc
import opfetch_moveWide
import opfetch_FP_addSub
import opfetch_FP_maxMin

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
       "00010001" : opfetch_addSub.opfetchAdd_i32,
       "00110001" : opfetch_addSub.opfetchAdds_i32,
       "01010001" : opfetch_addSub.opfetchSub_i32,
       "01110001" : opfetch_addSub.opfetchSubs_i32,
       "10010001" : opfetch_addSub.opfetchAdd_i64,
       "10110001" : opfetch_addSub.opfetchAdds_i64,
       "11010001" : opfetch_addSub.opfetchSub_i64,
       "11110001" : opfetch_addSub.opfetchSubs_i64,
    }[key](binary)
      
def ADD_SUB_SHIFT_REG(binary):
    key = binary[0:8] + "--" + binary[10]
    return {
       "00001011--0" : opfetch_addSub.opfetchAdd_sr32,
       "00101011--0" : opfetch_addSub.opfetchAdds_sr32,
       "01001011--0" : opfetch_addSub.opfetchSub_sr32,
       "01101011--0" : opfetch_addSub.opfetchSubs_sr32,
       "10001011--0" : opfetch_addSub.opfetchAdd_sr64,
       "10101011--0" : opfetch_addSub.opfetchAdds_sr64,
       "11001011--0" : opfetch_addSub.opfetchSub_sr64,
       "11101011--0" : opfetch_addSub.opfetchSubs_sr64,
    }[key](binary)
    
def ADD_SUB_EXT_REG(binary):
    key = binary[0:11]
    return {
       "00001011001" : opfetch_addSub.opfetchAdd_er32,
       "00101011001" : opfetch_addSub.opfetchAdds_er32,
       "01001011001" : opfetch_addSub.opfetchSub_er32,
       "01101011001" : opfetch_addSub.opfetchSubs_er32,
       "10001011001" : opfetch_addSub.opfetchAdd_er64,
       "10101011001" : opfetch_addSub.opfetchAdds_er64,
       "11001011001" : opfetch_addSub.opfetchSub_er64,
       "11101011001" : opfetch_addSub.opfetchSubs_er64,
    }[key](binary) 
    
    
def LOGICAL_IMMEDIATE(binary):
    key = binary[0:9]
    return {
       "000100100" : opfetch_logical.opfetchAnd_i32,
       "100100100" : opfetch_logical.opfetchAnd_i64,
       "011100100" : opfetch_logical.opfetchAnds_i32,
       "111100100" : opfetch_logical.opfetchAnds_i64,
    }[key](binary)
    
def LOGICAL_SHIFT_REG(binary):
    key = binary[0:8] + "--" + binary[10]
    return {
       "00001010--0" : opfetch_logical.opfetchAnd_sr32,
       "10001010--0" : opfetch_logical.opfetchAnd_sr64,
       "01101010--0" : opfetch_logical.opfetchAnds_sr32,
       "11101010--0" : opfetch_logical.opfetchAnds_sr64,
    }[key](binary)


def MOVE_IMMEDIATE(binary):
    key = binary[0:9]
    return {
       "000100101" : opfetch_move.opfetchMov_iwi32,
       "100100101" : opfetch_move.opfetchMov_iwi64,
       "010100101" : opfetch_move.opfetchMov_wi32,
       "110100101" : opfetch_move.opfetchMov_wi64,
       "001100100" : opfetch_move.opfetchMov_bmi32,
       "101100100" : opfetch_move.opfetchMov_bmi64,
    }[key](binary)
    
def MOVE_REGISTER(binary):
    key = binary[0:11] + "-"*5 + binary[16:27]
    return {
       "00101010000-----00000011111" : opfetch_move.opfetchMov_r32,
       "10101010000-----00000011111" : opfetch_move.opfetchMov_r64,
    }[key](binary)


def SHIFT_REGISTER(binary):
    key = binary[0:11] + "-"*5 + binary[16:22]
    return {
       "00011010110-----001010" : opfetch_shift.opfetchAsr_r32,
       "10011010110-----001010" : opfetch_shift.opfetchAsr_r64,
       "00011010110-----001000" : opfetch_shift.opfetchLsl_r32,
       "10011010110-----001000" : opfetch_shift.opfetchLsl_r64,
       "00011010110-----001001" : opfetch_shift.opfetchLsr_r32,
       "10011010110-----001001" : opfetch_shift.opfetchLsr_r64,
    }[key](binary)
    
def SHIFT_IMMEDIATE(binary):
    key = binary[0:10]
    return {
       "0001001100" : opfetch_shift.opfetchAsr_i32,
       "1001001101" : opfetch_shift.opfetchAsr_i64,
       "0101001100" : opfetch_shift.opfetchLslLsr_i32,
       "1101001101" : opfetch_shift.opfetchLslLsr_i64,
    }[key](binary)

def PC_RELATIVE(binary):
    key = binary[0] + "--" + binary[3:8]
    return {       
       "0--10000" : opfetch_misc.opfetchADR,
       "1--10000" : opfetch_misc.opfetchADRP,
    }[key](binary)
    
def NOP(binary):
    key = binary[0:20] + "-"*7 + binary[27:32]
    return {
       "11010101000000110010" + "-"*7 + "11111" : opfetch_misc.opfetchNOP,
    }[key](binary)

def MUL_DIV_REG(binary):
    key = binary[0:11] + "-"*5 + binary[16:22]
    return {
      "10011011101-----011111" : opfetch_mulDiv.opfetchMul,
      "00011010110-----000010" : opfetch_mulDiv.opfetchUnsignedDiv_32,
      "10011010110-----000010" : opfetch_mulDiv.opfetchUnsignedDiv_64,
      "00011010110-----000011" : opfetch_mulDiv.opfetchSignedDiv_32,
      "10011010110-----000011" : opfetch_mulDiv.opfetchSignedDiv_64,
    }[key](binary)

def CONDITIONAL_INSTRUCTIONS(binary):
    if(binary[11:16] == "11111" and binary[22:27] == "11111"):
        key = binary[0:16] + "-"*4 + binary[20:27]
    else:
        key = binary[0:11] + "-"*9 + binary[20:22]
    return {
      "0001101010011111----0111111" : opfetch_conditional.opfetchConditionalSet_32,
      "1001101010011111----0111111" : opfetch_conditional.opfetchConditionalSet_64,
      "01011010100---------00"      : opfetch_conditional.opfetchConditionalSelectInverse_32,
      "11011010100---------00"      : opfetch_conditional.opfetchConditionalSelectInverse_64,
      "01011010100---------01"      : opfetch_conditional.opfetchConditionalSelectNegation_32,
      "11011010100---------01"      : opfetch_conditional.opfetchConditionalSelectNegation_64,
      "00011010100---------01"      : opfetch_conditional.opfetchConditionalSelectIncrement_32,
      "10011010100---------01"      : opfetch_conditional.opfetchConditionalSelectIncrement_64,
      "00111010010---------10"      : opfetch_conditional.opfetchConditionalCompareNegative_i32,
      "10111010010---------10"      : opfetch_conditional.opfetchConditionalCompareNegative_i64,
      "00111010010---------00"      : opfetch_conditional.opfetchConditionalCompareNegative_r32,
      "10111010010---------00"      : opfetch_conditional.opfetchConditionalCompareNegative_r64,
    }[key](binary)

def MORE_ALU(binary):
    key = binary[0:22]
    return {
      "0101101011000000000101"  : opfetch_ALU.opfetchCLS_32,
      "1101101011000000000101"  : opfetch_ALU.opfetchCLS_64,
      "0101101011000000000100"  : opfetch_ALU.opfetchCLZ_32,
      "1101101011000000000100"  : opfetch_ALU.opfetchCLZ_64,
    }[key](binary)

def ROTATE_IMMEDIATE(binary):
    key = binary[0:11]
    return {
      "00010011100"  : opfetch_rotate.opfetchRotate_i32,
      "10010011110"  : opfetch_rotate.opfetchRotate_i64,
    }[key](binary)

def ROTATE_REGISTER(binary):
    key = binary[0:11] + "-"*5 + binary[16:22]
    return {
      "00011010110-----001011"  : opfetch_rotate.opfetchRotate_r32,
      "10011010110-----001011"  : opfetch_rotate.opfetchRotate_r64,
    }[key](binary)

def BITWISE_SHIFT_REGISTER(binary):
    key = binary[0:8] + "-"*2 + binary[10:11]
    return {
      "00001010--1" : opfetch_bitwise_shift.opfetchBitwiseShift_32,
      "10001010--1" : opfetch_bitwise_shift.opfetchBitwiseShift_64,
      "01101010--1" : opfetch_bitwise_shift.opfetchBitwiseShiftSetFlags_32,
      "11101010--1" : opfetch_bitwise_shift.opfetchBitwiseShiftSetFlags_64,
    }[key](binary)

def ADD_WITH_CARRY(binary):
    key = binary[0:11] + "-"*5 + binary[16:22]
    return {
      "00011010000-----000000"  : opfetch_adc.opfetchADC_32,
      "10011010000-----000000"  : opfetch_adc.opfetchADC_64,
    }[key](binary)
    
def MOVE_WIDE(binary):
    key = binary[0:9]
    return {
      "011100101" : opfetch_moveWide.opfetchMoveK_32,
      "111100101" : opfetch_moveWide.opfetchMoveK_64,
      "000100101" : opfetch_moveWide.opfetchMoveN_32,
      "100100101" : opfetch_moveWide.opfetchMoveN_64,
      "010100101" : opfetch_moveWide.opfetchMoveZ_32,
      "110100101" : opfetch_moveWide.opfetchMoveZ_64,
    }[key](binary)
    
def FLOATING_POINT_MOVE_IMMEDIATE(binary):
    key = binary[0:11] + "-"*8 + binary[19:27]
    return {
      "00011110001--------10000000" : opfetch_move.opfetchFMove_iSP,
      "00011110011--------10000000" : opfetch_move.opfetchFMove_iDP,
    }[key](binary)

def FLOATING_POINT_ADD_SUB(binary):
  key = binary[0:11] + "-"*5 + binary[16:22]
  return {
    "00011110001-----001010" :  opfetch_FP_addSub.opfetchFADD_scalar_SP,
    "00011110011-----001010" :  opfetch_FP_addSub.opfetchFADD_scalar_DP,
    "00001110001-----110101" :  opfetch_FP_addSub.opfetchFADD_vector_2S,
    "01001110001-----110101" :  opfetch_FP_addSub.opfetchFADD_vector_4S,
    "01001110011-----110101" :  opfetch_FP_addSub.opfetchFADD_vector_2D,
    "00011110001-----001110" :  opfetch_FP_addSub.opfetchFSUB_scalar_SP,
    "00011110011-----001110" :  opfetch_FP_addSub.opfetchFSUB_scalar_DP,
    "00001110101-----110101" :  opfetch_FP_addSub.opfetchFSUB_vector_2S,
    "01001110101-----110101" :  opfetch_FP_addSub.opfetchFSUB_vector_4S,
    "01001110111-----110101" :  opfetch_FP_addSub.opfetchFSUB_vector_2D,
  }[key](binary)

def FLOATING_POINT_MAX_MIN(binary):
  key = binary[0:11] + "-"*5 + binary[16:22]
  return {
    "00011110001-----010010" :  opfetch_FP_maxMin.opfetchFMAX_scalar_SP,
    "00011110011-----010010" :  opfetch_FP_maxMin.opfetchFMAX_scalar_DP,
    "00001110001-----111101" :  opfetch_FP_maxMin.opfetchFMAX_vector_2S,
    "01001110001-----111101" :  opfetch_FP_maxMin.opfetchFMAX_vector_4S,
    "01001110011-----111101" :  opfetch_FP_maxMin.opfetchFMAX_vector_2D,
    "00011110001-----010110" :  opfetch_FP_maxMin.opfetchFMIN_scalar_SP,
    "00011110011-----010110" :  opfetch_FP_maxMin.opfetchFMIN_scalar_DP,
    "00001110101-----111101" :  opfetch_FP_maxMin.opfetchFMIN_vector_2S,
    "01001110101-----111101" :  opfetch_FP_maxMin.opfetchFMIN_vector_4S,
    "01001110111-----111101" :  opfetch_FP_maxMin.opfetchFMIN_vector_2D,
  }[key](binary)

def FLOATING_POINT_MOVE_REGISTER(binary):
  key = binary[0:22]
  return {
    "0001111000100000010000" :  opfetch_move.opfetchFMove_regSP,
    "0001111001100000010000" :  opfetch_move.opfetchFMove_regDP,
    "0001111000100111000000" :  opfetch_move.opfetchFMove_32toSP,
    "0001111000100110000000" :  opfetch_move.opfetchFMove_SPto32,
    "1001111001100111000000" :  opfetch_move.opfetchFMove_64toDP,
    "1001111010101111000000" :  opfetch_move.opfetchFMove_64to128,
    "1001111001100110000000" :  opfetch_move.opfetchFMove_DPto64,
    "1001111010101110000000" :  opfetch_move.opfetchFMove_128to64,
  }[key](binary)