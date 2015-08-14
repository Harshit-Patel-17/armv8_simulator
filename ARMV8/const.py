'''
Created on Aug 8, 2014

@author: harinder
'''

INST_SIZE = 32
REG_SIZE = 64

FLAG_INST_EXECUTED = False
FLAG_OPFETCH_EXECUTED = False #Shows whether operand fetch stage executed or not
FLAG_WRITEBACK_EXECUTED = False
FLAG_MEMACCESS_EXECUTED = False

FLAG_FETCH_COMPLETED = False #Shows whether instruction is successfully fetched or not
FLAG_OP_FETCHED = False #Shows whether operands are successfully fetched or not
FLAG_EXECUTION_COMPLETED = False #Shows whether instruction has completed its execution stage or not
FLAG_MEMACCESS_COMPLETED = False #Shows whether instruction has completed its memaccess stage or not
FLAG_WRITEBACK_COMPLETED = False #Shows whether instruction has completed its writeback stage or not


FLAG_DATA_FORWARDING = False

FETCH_COUNTER = 0
OPFETCH_COUNTER = 0
EXECUTION_COUNTER = 0
MEMACCESS_COUNTER = 0
WRITEBACK_COUNTER = 0

MEM_OP_LOAD = "Load"
MEM_OP_STORE = "Store"
MEM_OP_PREFETCH = "Prefetch"

TRAP = 'Trap'

CONDITIONS_MAP = {
	"0000" : "EQ",
	"0001" : "NE",
	"0010" : "CS",
	"0011" : "CC",
	"0100" : "MI",
	"0101" : "PL",
	"0110" : "VS",
	"0111" : "VE",
	"1000" : "HI",
	"1001" : "LS",
	"1010" : "GE",
	"1011" : "LT",
	"1100" : "GT",
	"1101" : "LE",
	"1110" : "AL"
}

CONDITIONS_MAP_LSB_INVERTED = {
	"0001" : "EQ",
	"0000" : "NE",
	"0011" : "CS",
	"0010" : "CC",
	"0101" : "MI",
	"0100" : "PL",
	"0111" : "VS",
	"0110" : "VE",
	"1001" : "HI",
	"1000" : "LS",
	"1011" : "GE",
	"1010" : "LT",
	"1101" : "GT",
	"1100" : "LE",
	"1111" : "AL"
}

CRC_Polynomial = "00000100110000010001110110110111"
