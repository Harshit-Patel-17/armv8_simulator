'''
@author: harinder
'''
import executor_addSub
import executor_logical
import executor_move
import executor_shift
import executor_misc
import executor_mulDiv
import executor_conditional
import executor_ALU
import executor_rotate
import executor_bitwise_shift
import executor_adc
import executor_moveWide
import executor_FP_addSub
import executor_Vector

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
            20 : FLOATING_POINT_MOVE, #only for testing purpose,to be removed later
            21 : VECTOR_INSTRUCTIONS,
        }[i](binary)
    except KeyError:
        i = i

def ADD_SUB_IMMEDIATE(binary):
    key = binary[0:8] 
    return {
       "00010001" : executor_addSub.execAdd_i32,
       "00110001" : executor_addSub.execAdds_i32,
       "01010001" : executor_addSub.execSub_i32,
       "01110001" : executor_addSub.execSubs_i32,
       "10010001" : executor_addSub.execAdd_i64,
       "10110001" : executor_addSub.execAdds_i64,
       "11010001" : executor_addSub.execSub_i64,
       "11110001" : executor_addSub.execSubs_i64,
    }[key](binary)
      
def ADD_SUB_SHIFT_REG(binary):
    key = binary[0:8] + "--" + binary[10]
    return {
       "00001011--0" : executor_addSub.execAdd_sr32,
       "00101011--0" : executor_addSub.execAdds_sr32,
       "01001011--0" : executor_addSub.execSub_sr32,
       "01101011--0" : executor_addSub.execSubs_sr32,
       "10001011--0" : executor_addSub.execAdd_sr64,
       "10101011--0" : executor_addSub.execAdds_sr64,
       "11001011--0" : executor_addSub.execSub_sr64,
       "11101011--0" : executor_addSub.execSubs_sr64,
    }[key](binary)
    
def ADD_SUB_EXT_REG(binary):
    key = binary[0:11]
    return {
       "00001011001" : executor_addSub.execAdd_er32,
       "00101011001" : executor_addSub.execAdds_er32,
       "01001011001" : executor_addSub.execSub_er32,
       "01101011001" : executor_addSub.execSubs_er32,
       "10001011001" : executor_addSub.execAdd_er64,
       "10101011001" : executor_addSub.execAdds_er64,
       "11001011001" : executor_addSub.execSub_er64,
       "11101011001" : executor_addSub.execSubs_er64,
    }[key](binary) 
    
    
def LOGICAL_IMMEDIATE(binary):
    key = binary[0:9]
    return {
       "000100100" : executor_logical.execAnd_i32,
       "100100100" : executor_logical.execAnd_i64,
       "011100100" : executor_logical.execAnds_i32,
       "111100100" : executor_logical.execAnds_i64,
    }[key](binary)
    
def LOGICAL_SHIFT_REG(binary):
    key = binary[0:8] + "--" + binary[10]
    return {
       "00001010--0" : executor_logical.execAnd_sr32,
       "10001010--0" : executor_logical.execAnd_sr64,
       "01101010--0" : executor_logical.execAnds_sr32,
       "11101010--0" : executor_logical.execAnds_sr64,
    }[key](binary)


def MOVE_IMMEDIATE(binary):
    key = binary[0:9]
    return {
       "000100101" : executor_move.execMov_iwi32,
       "100100101" : executor_move.execMov_iwi64,
       "010100101" : executor_move.execMov_wi32,
       "110100101" : executor_move.execMov_wi64,
       "001100100" : executor_move.execMov_bmi32,
       "101100100" : executor_move.execMov_bmi64,
    }[key](binary)
    
def MOVE_REGISTER(binary):
    key = binary[0:11] + "-"*5 + binary[16:27]
    return {
       "00101010000-----00000011111" : executor_move.execMov_r32,
       "10101010000-----00000011111" : executor_move.execMov_r64,
    }[key](binary)


def SHIFT_REGISTER(binary):
    key = binary[0:11] + "-"*5 + binary[16:22]
    return {
       "00011010110-----001010" : executor_shift.execAsr_r32,
       "10011010110-----001010" : executor_shift.execAsr_r64,
       "00011010110-----001000" : executor_shift.execLsl_r32,
       "10011010110-----001000" : executor_shift.execLsl_r64,
       "00011010110-----001001" : executor_shift.execLsr_r32,
       "10011010110-----001001" : executor_shift.execLsr_r64,
    }[key](binary)
    
def SHIFT_IMMEDIATE(binary):
    key = binary[0:10]
    return {
       "0001001100" : executor_shift.execAsr_i32,
       "1001001101" : executor_shift.execAsr_i64,
       "0101001100" : executor_shift.execLslLsr_i32,
       "1101001101" : executor_shift.execLslLsr_i64,
    }[key](binary)

def PC_RELATIVE(binary):
    key = binary[0] + "--" + binary[3:8]
    return {       
       "0--10000" : executor_misc.execADR,
       "1--10000" : executor_misc.execADRP,
    }[key](binary)
    
def NOP(binary):
    key = binary[0:20] + "-"*7 + binary[27:32]
    return {
       "11010101000000110010" + "-"*7 + "11111" : executor_misc.execNOP,
    }[key](binary)

def MUL_DIV_REG(binary):
    key = binary[0:11] + "-"*5 + binary[16:22]
    return {
      "10011011101-----011111" : executor_mulDiv.execMul,
      "00011010110-----000010" : executor_mulDiv.execUnsignedDiv_32,
      "10011010110-----000010" : executor_mulDiv.execUnsignedDiv_64,
      "00011010110-----000011" : executor_mulDiv.execSignedDiv_32,
      "10011010110-----000011" : executor_mulDiv.execSignedDiv_64,
    }[key](binary)


def CONDITIONAL_INSTRUCTIONS(binary):
  if(binary[11:16] == "11111" and binary[22:27] == "11111"):
    key = binary[0:16] + "-"*4 + binary[20:27]
  else:
    key = binary[0:11] + "-"*9 + binary[20:22]
  return {
    "0001101010011111----0111111" : executor_conditional.execConditionalSet_32,
    "1001101010011111----0111111" : executor_conditional.execConditionalSet_64,
    "01011010100---------00"      : executor_conditional.execConditionalSelectInverse_32,
    "11011010100---------00"      : executor_conditional.execConditionalSelectInverse_64,
    "01011010100---------01"      : executor_conditional.execConditionalSelectNegation_32,
    "11011010100---------01"      : executor_conditional.execConditionalSelectNegation_64,
    "00011010100---------01"      : executor_conditional.execConditionalSelectIncrement_32,
    "10011010100---------01"      : executor_conditional.execConditionalSelectIncrement_64,
    "00111010010---------10"      : executor_conditional.execConditionalCompareNegative_i32,
    "10111010010---------10"      : executor_conditional.execConditionalCompareNegative_i64,
    "00111010010---------00"      : executor_conditional.execConditionalCompareNegative_r32,
    "10111010010---------00"      : executor_conditional.execConditionalCompareNegative_r64,
  }[key](binary)

def MORE_ALU(binary):
    key = binary[0:22]
    return {
      "0101101011000000000101"  : executor_ALU.executeCLS_32,
      "1101101011000000000101"  : executor_ALU.executeCLS_64,
      "0101101011000000000100"  : executor_ALU.executeCLZ_32,
      "1101101011000000000100"  : executor_ALU.executeCLZ_64,
    }[key](binary)

def ROTATE_IMMEDIATE(binary):
    key = binary[0:11]
    return {
      "00010011100"  : executor_rotate.execRotate_i32,
      "10010011110"  : executor_rotate.execRotate_i64,
    }[key](binary)

def ROTATE_REGISTER(binary):
    key = binary[0:11] + "-"*5 + binary[16:22]
    return {
      "00011010110-----001011"  : executor_rotate.execRotate_r32,
      "10011010110-----001011"  : executor_rotate.execRotate_r64,
    }[key](binary)

def BITWISE_SHIFT_REGISTER(binary):
  key = binary[0:8] + "-"*2 + binary[10:11]
  return {
    "00001010--1" : executor_bitwise_shift.execBitwiseShift_32,
    "10001010--1" : executor_bitwise_shift.execBitwiseShift_64,
    "01101010--1" : executor_bitwise_shift.execBitwiseShiftSetFlags_32,
    "11101010--1" : executor_bitwise_shift.execBitwiseShiftSetFlags_64,
  }[key](binary)

def ADD_WITH_CARRY(binary):
  key = binary[0:11] + "-"*5 + binary[16:22]
  return {
    "00011010000-----000000"  : executor_adc.execADC_32,
    "10011010000-----000000"  : executor_adc.execADC_64,
  }[key](binary)

def MOVE_WIDE(binary):
  key = binary[0:9]
  return {
    "011100101" : executor_moveWide.execMoveK_32,
    "111100101" : executor_moveWide.execMoveK_64,
    "000100101" : executor_moveWide.execMoveN_32,
    "100100101" : executor_moveWide.execMoveN_64,
    "010100101" : executor_moveWide.execMoveZ_32,
    "110100101" : executor_moveWide.execMoveZ_64,
  }[key](binary)

def FLOATING_POINT_ADD_SUB(binary):
  key = binary[0:11] + "-"*5 + binary[16:22]
  return {
    "00011110001-----001010" :  executor_FP_addSub.execFADD_scalar_SP,
    "00011110011-----001010" :  executor_FP_addSub.execFADD_scalar_DP,
    "00001110001-----110101" :  executor_FP_addSub.execFADD_vector_2S,
    "01001110001-----110101" :  executor_FP_addSub.execFADD_vector_4S,
    "01001110011-----110101" :  executor_FP_addSub.execFADD_vector_2D,
    "00011110001-----001110" :  executor_FP_addSub.execFSUB_scalar_SP,
    "00011110011-----001110" :  executor_FP_addSub.execFSUB_scalar_DP,
    "00001110101-----110101" :  executor_FP_addSub.execFSUB_vector_2S,
    "01001110101-----110101" :  executor_FP_addSub.execFSUB_vector_4S,
    "01001110111-----110101" :  executor_FP_addSub.execFSUB_vector_2D,
  }[key](binary)

def VECTOR_INSTRUCTIONS(binary):
  key = binary[0:9] + "-" + binary[10:12] + "--" + binary[14:16] + "----" + binary[20:26] + "-" + binary[27]
  return {
    "111100111-11--00----010100-0" :  executor_Vector.execVCNT_A1_64,
    "111100111-11--00----010101-0" :  executor_Vector.execVCNT_A1_128,
    "111111111-11--00----010100-0" :  executor_Vector.execVCNT_T1_64,
    "111111111-11--00----010101-0" :  executor_Vector.execVCNT_T1_128,
  }

def FLOATING_POINT_MOVE(binary):
  key = binary[0:11] + "-"*8 + binary[19:27]
  return {
    "00011110001--------10000000" : executor_move.execFMove_SP,
    "00011110011--------10000000" : executor_move.execFMove_DP,
  }[key](binary)
