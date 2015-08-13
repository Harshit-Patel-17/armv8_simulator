'''
Created on Aug 8, 2014

@author: harinder
'''

import utilFunc
import mem
import const
import armdebug

def op_i(binary, N, setFlags):
    const.FLAG_OPFETCH_EXECUTED = True
    if(armdebug.pipelineStages[2] != '--------'):
        return
    
    if(setFlags):
        inst = "ANDS "
    else:
        inst = 'AND '
    
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    
    if(mem.regObsolete[rnKey] == False):
        const.FLAG_OP_FETCHED = True
        rnValue = utilFunc.getRegValueByStringkey(binary[22:27],'0')
    elif(const.FLAG_DATA_FORWARDING):
        forwardedValues = mem.findForwardedValues(rnKey)
        if(forwardedValues[0] != None):
            const.FLAG_OP_FETCHED = True
            rnValue = forwardedValues[0]
        else:
            return
    else:
        return
    
    mem.regObsolete[rdKey] = True
    mem.regObsolete_last_modified_indices.append(rdKey)
    
    #rnValue = utilFunc.getRegValueByStringkey(binary[22:27], '0')
    if(N == 32):
        r = 'w'
        rnValue = rnValue[32:64]
    else:
        r = 'x'
    inst += r + str(rdKey) + ', ' + r + str(rnKey)
    
    
    immr = binary[10:16]
    imms = binary[16:22]
    immN = binary[9]
    
    imm, temp = utilFunc.decodeBitMasks(immN, imms, immr, N)
    inst += ', #' + str(int(imm,2))
    
    mem.operand1Buffer = rnValue
    mem.operand2Buffer = imm

def opfetchAnd_i32(binary):
    op_i(binary, 32, 0)
    
    
def opfetchAnd_i64(binary):
    op_i(binary, 64, 0)

def opfetchAnds_i32(binary):
    op_i(binary, 32, 1)

def opfetchAnds_i64(binary):
    op_i(binary, 64, 1)
    
    
def opfetchAnd_sr32(binary):    
    const.FLAG_OPFETCH_EXECUTED = True
    if(armdebug.pipelineStages[2] != '--------'):
        return
    
    inst = 'AND '
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    rmKey = utilFunc.getRegKeyByStringKey(binary[11:16])    
    
    if(mem.regObsolete[rnKey] == False and mem.regObsolete[rmKey] == False):
        const.FLAG_OP_FETCHED = True
        rnValue = utilFunc.getRegValueByStringkey(binary[22:27],'0')
        rmValue = utilFunc.getRegValueByStringkey(binary[11:16],'0')
    elif(const.FLAG_DATA_FORWARDING):
        forwardedValues = mem.findForwardedValues(rnKey, rmKey)
        if(forwardedValues[0] != None and forwardedValues[1] != None):
            const.FLAG_OP_FETCHED = True
            rnValue = forwardedValues[0]
            rmValue = forwardedValues[1]
        else:
            return
    else:
        return
    
    mem.regObsolete[rdKey] = True
    mem.regObsolete_last_modified_indices.append(rdKey)
    
    inst += 'w' + str(rdKey) + ', w' + str(rnKey) + ', w' + str(rmKey) + ', '    
    
    #rnValue = utilFunc.getRegValueByStringkey(binary[22:27], '0')
    immKey = binary[16:22]
    immvalue = int(immKey, 2)  # amount
    #rmValue = utilFunc.getRegValueByStringkey(binary[11:16], '0')
    
    shifttype = binary[8:10]
    
    temp = ''
    
    if shifttype == "00":   
        temp = utilFunc.lsl(rmValue[32:64], immvalue)
        inst += 'LSL'
    elif shifttype == "01":
        temp = utilFunc.lsr(rmValue[32:64], immvalue)
        inst += 'LSR'
    elif shifttype == "10":
        temp = utilFunc.asr(rmValue[32:64], immvalue)
        inst += 'ASR'
    else:
        temp = utilFunc.ror(rmValue[32:64], immvalue)
        inst += 'ROR'
    inst += ' #' + str(immvalue)

    mem.operand1Buffer = temp
    mem.operand2Buffer = rnValue[32:64]
    
def opfetchAnd_sr64(binary):
    const.FLAG_OPFETCH_EXECUTED = True
    if(armdebug.pipelineStages[2] != '--------'):
        return
    
    inst = 'AND '
    
    rdKey = utilFunc.getRegKeyByStringKey(binary[27:32])
    rnKey = utilFunc.getRegKeyByStringKey(binary[22:27])
    rmKey = utilFunc.getRegKeyByStringKey(binary[11:16])
    
    if(mem.regObsolete[rnKey] == False and mem.regObsolete[rmKey] == False):
        const.FLAG_OP_FETCHED = True
        rnValue = utilFunc.getRegValueByStringkey(binary[22:27],'0')
        rmValue = utilFunc.getRegValueByStringkey(binary[11:16],'0')
    elif(const.FLAG_DATA_FORWARDING):
        forwardedValues = mem.findForwardedValues(rnKey, rmKey)
        if(forwardedValues[0] != None and forwardedValues[1] != None):
            const.FLAG_OP_FETCHED = True
            rnValue = forwardedValues[0]
            rmValue = forwardedValues[1]
        else:
            return
    else:
        return
    
    mem.regObsolete[rdKey] = True
    mem.regObsolete_last_modified_indices.append(rdKey)
    
    inst += 'x' + str(rdKey) + ', x' + str(rnKey) + ', x' + str(rmKey) + ', '
    
    #rnValue = utilFunc.getRegValueByStringkey(binary[22:27], '0')
    immKey = binary[16:22]
    immvalue = int(immKey, 2)  # amount
    #rmValue = utilFunc.getRegValueByStringkey(binary[11:16], '0')
    
    shifttype = binary[8:10]
    
    temp = ''
    
    if shifttype == "00":   
        temp = utilFunc.lsl(rmValue[0:64], immvalue)
        inst += 'LSL'
    elif shifttype == "01":
        temp = utilFunc.lsr(rmValue[0:64], immvalue)
        inst += 'LSR'
    elif shifttype == "10":
        temp = utilFunc.asr(rmValue[0:64], immvalue)
        inst += 'ASR'
    else:
        temp = utilFunc.ror(rmValue[0:64], immvalue)
        inst += 'ROR'
    inst += ' #' + str(immvalue)

    mem.operand1Buffer = temp
    mem.operand2Buffer = rnValue[0:64]
    
def opfetchAnds_sr32(binary):
    opfetchAnd_sr32(binary)

def opfetchAnds_sr64(binary):
    opfetchAnd_sr64(binary)