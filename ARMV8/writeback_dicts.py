'''
@author: harinder
'''
import writeback_addSub
import writeback_logical
import writeback_move
import writeback_shift
import writeback_misc
import writeback_mulDiv

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
    }[key](binary)
    
def LOGICAL_SHIFT_REG(binary):
    key = binary[0:8] + "--" + binary[10]
    return {
       "00001010--0" : writeback_logical.writebackAnd_sr32,
       "10001010--0" : writeback_logical.writebackAnd_sr64,
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
