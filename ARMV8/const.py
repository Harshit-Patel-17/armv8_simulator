'''
Created on Aug 8, 2014

@author: harinder
'''

INST_SIZE = 32
REG_SIZE = 64

FLAG_INST_EXECUTED = False
FLAG_OPFETCH_EXECUTED = False #Shows whether operand fetch stage executed or not
FLAG_OP_FETCHED = False #Shows whether operands are successfully fetched or not
FLAG_WRITEBACK_EXECUTED = False
FLAG_MEMACCESS_EXECUTED = False

MEM_OP_LOAD = "Load"
MEM_OP_STORE = "Store"
MEM_OP_PREFETCH = "Prefetch"

TRAP = 'Trap'