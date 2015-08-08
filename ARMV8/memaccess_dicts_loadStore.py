'''
@author: harinder
'''
import memaccess_loadStore

def INSTRUCTION_TYPE(binary,i):
    try:
        return {
            0 : LOAD_REGISTER_LITERAL,
            1 : LOAD_STORE_REGISTER_PAIR_POSTINDEXED,
            2 : LOAD_STORE_REGISTER_PAIR_PREINDEXED,
            3 : LOAD_STORE_REGISTER_PAIR_SIGNED_OFFSET,
            4 : LOAD_STORE_REGISTER_POSTINDEXED_IMMEDIATE,
            5 : LOAD_STORE_REGISTER_PREINDEXED_IMMEDIATE,
            6 : LOAD_STORE_REGISTER_UNSIGNED_OFFSET,
            7 : LOAD_STORE_REGISTER_OFFSET,
        }[i](binary)
    except KeyError:
        i=i


def LOAD_REGISTER_LITERAL(binary):
    key = binary[0:8]
    return {       
       "00011000" : memaccess_loadStore.memaccessLDR_l32,
       "01011000" : memaccess_loadStore.memaccessLDR_l64,
       "10011000" : memaccess_loadStore.memaccessLDRSW_l,
    }[key](binary)
    
def LOAD_STORE_REGISTER_PAIR_POSTINDEXED(binary):
    key = binary[0:10]
    return {       
       "0010100010" : memaccess_loadStore.memaccessSTP_rp_posti_32,
       "0010100011" : memaccess_loadStore.memaccessLDP_rp_posti_32,
       "1010100010" : memaccess_loadStore.memaccessSTP_rp_posti_64,
       "1010100011" : memaccess_loadStore.memaccessLDP_rp_posti_64,
    }[key](binary)
    
def LOAD_STORE_REGISTER_PAIR_PREINDEXED(binary):
    key = binary[0:10]
    return {       
       "0010100110" : memaccess_loadStore.memaccessSTP_rp_prei_32,
       "0010100111" : memaccess_loadStore.memaccessLDP_rp_prei_32,
       "1010100110" : memaccess_loadStore.memaccessSTP_rp_prei_64,
       "1010100111" : memaccess_loadStore.memaccessLDP_rp_prei_64,
    }[key](binary)
    
def LOAD_STORE_REGISTER_PAIR_SIGNED_OFFSET(binary):
    key = binary[0:10]
    return {       
       "0010100100" : memaccess_loadStore.memaccessSTP_rp_offset_32,
       "0010100101" : memaccess_loadStore.memaccessLDP_rp_offset_32,
       "1010100100" : memaccess_loadStore.memaccessSTP_rp_offset_64,
       "1010100101" : memaccess_loadStore.memaccessLDP_rp_offset_64,
    }[key](binary)
    
def LOAD_STORE_REGISTER_POSTINDEXED_IMMEDIATE(binary):
    key = binary[0:11]+"-"*9+binary[20:22]
    return {       
       "10111000000"+"-"*9+"01" : memaccess_loadStore.memaccessSTR_reg_posti_32,
       "10111000010"+"-"*9+"01" : memaccess_loadStore.memaccessLDR_reg_posti_32,
       "10111000100"+"-"*9+"01" : memaccess_loadStore.memaccessLDRSW_reg_posti,
       "11111000000"+"-"*9+"01" : memaccess_loadStore.memaccessSTR_reg_posti_64,
       "11111000010"+"-"*9+"01" : memaccess_loadStore.memaccessLDR_reg_posti_64,
       "00111000010"+"-"*9+"01" : memaccess_loadStore.memaccessLDRB_reg_posti,
       "01111000010"+"-"*9+"01" : memaccess_loadStore.memaccessLDRH_reg_posti,
       "00111000110"+"-"*9+"01" : memaccess_loadStore.memaccessLDRSB_reg_posti_32,
       "00111000100"+"-"*9+"01" : memaccess_loadStore.memaccessLDRSB_reg_posti_64,
    }[key](binary)
    
def LOAD_STORE_REGISTER_PREINDEXED_IMMEDIATE(binary):
    key = binary[0:11]+"-"*9+binary[20:22]
    return {       
       "10111000000"+"-"*9+"11" : memaccess_loadStore.memaccessSTR_reg_prei_32,
       "10111000010"+"-"*9+"11" : memaccess_loadStore.memaccessLDR_reg_prei_32,
       "10111000100"+"-"*9+"11" : memaccess_loadStore.memaccessLDRSW_reg_prei,
       "11111000000"+"-"*9+"11" : memaccess_loadStore.memaccessSTR_reg_prei_64,
       "11111000010"+"-"*9+"11" : memaccess_loadStore.memaccessLDR_reg_prei_64,
       "00111000010"+"-"*9+"11" : memaccess_loadStore.memaccessLDRB_reg_prei,
       "01111000010"+"-"*9+"11" : memaccess_loadStore.memaccessLDRH_reg_prei,
       "00111000110"+"-"*9+"11" : memaccess_loadStore.memaccessLDRSB_reg_prei_32,
       "00111000100"+"-"*9+"11" : memaccess_loadStore.memaccessLDRSB_reg_prei_64,
    }[key](binary)
    
def LOAD_STORE_REGISTER_UNSIGNED_OFFSET(binary):
    key = binary[0:10]
    return {       
       "1011100100" : memaccess_loadStore.memaccessSTR_reg_unsignedOffset_32,
       "1011100101" : memaccess_loadStore.memaccessLDR_reg_unsignedOffset_32,
       "1011100110" : memaccess_loadStore.memaccessLDRSW_reg_unsignedOffset,
       "1111100100" : memaccess_loadStore.memaccessSTR_reg_unsignedOffset_64,
       "1111100101" : memaccess_loadStore.memaccessLDR_reg_unsignedOffset_64,
       "0011100101" : memaccess_loadStore.memaccessLDRB_reg_unsignedOffset,
       "0111100101" : memaccess_loadStore.memaccessLDRH_reg_unsignedOffset,
       "0011100111" : memaccess_loadStore.memaccessLDRSB_reg_unsignedOffset_32,
       "0011100110" : memaccess_loadStore.memaccessLDRSB_reg_unsignedOffset_64,
    }[key](binary)
    
    
def LOAD_STORE_REGISTER_OFFSET(binary):
    key = binary[0:11]+"-"*9+binary[20:22]
    return {       
       "10111000001"+"-"*9+"10" : memaccess_loadStore.memaccessSTR_reg_offset_32,
       "10111000011"+"-"*9+"10" : memaccess_loadStore.memaccessLDR_reg_offset_32,
       "10111000101"+"-"*9+"10" : memaccess_loadStore.memaccessLDRSW_reg_offset,
       "11111000001"+"-"*9+"10" : memaccess_loadStore.memaccessSTR_reg_offset_64,
       "11111000011"+"-"*9+"10" : memaccess_loadStore.memaccessLDR_reg_offset_64,
       "00111000011"+"-"*9+"10" : memaccess_loadStore.memaccessLDRB_reg_offset,
       "01111000011"+"-"*9+"10" : memaccess_loadStore.memaccessLDRH_reg_offset,
       "00111000111"+"-"*9+"10" : memaccess_loadStore.memaccessLDRSB_reg_offset_32,
       "00111000101"+"-"*9+"10" : memaccess_loadStore.memaccessLDRSB_reg_offset_64,
    }[key](binary)
       