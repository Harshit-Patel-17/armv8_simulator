import sys
import xml.etree.ElementTree as ET

configTreeRoot = ET.parse('config.xml').getroot()

latency = {}
leakageEnergy = {}
dynamicEnergy = {}

try:
    Decode = configTreeRoot.find('System').find('Core').find('Decode')
    IntRF = configTreeRoot.find('System').find('Core').find('RegisterFile').find('Integer')
    FloatRF = configTreeRoot.find('System').find('Core').find('RegisterFile').find('Float')
    Decode = configTreeRoot.find('System').find('Core').find('Decode')
    IntALU = configTreeRoot.find('System').find('Core').find('IntShifterALU')
    IntMul = configTreeRoot.find('System').find('Core').find('IntMul')
    IntDiv = configTreeRoot.find('System').find('Core').find('IntDiv')
    FloatALU = configTreeRoot.find('System').find('Core').find('FloatALU')
    FloatMul = configTreeRoot.find('System').find('Core').find('FloatMul')
    FloatDiv = configTreeRoot.find('System').find('Core').find('FloatDiv')
    ICache = configTreeRoot.find('Library').find('ICache_32K_8')
    L1Cache = configTreeRoot.find('Library').find('L1Cache_32K_8')
    
    latency['IntALU'] = int(IntALU.find('Latency').text)
    latency['IntMul'] = int(IntMul.find('Latency').text)
    latency['IntDiv'] = int(IntDiv.find('Latency').text)
    latency['FloatALU'] = int(FloatALU.find('Latency').text)
    latency['FLoatMul'] = int(FloatMul.find('Latency').text)
    latency['FloatDiv'] = int(FloatDiv.find('Latency').text)
    latency['ICache'] = int(ICache.find('Latency').text)
    latency['L1Cache'] = int(L1Cache.find('Latency').text)
    
    
    leakageEnergy['Decode'] = float(Decode.find('LeakageEnergy').text)
    leakageEnergy['IntRF'] = float(IntRF.find('LeakageEnergy').text)
    leakageEnergy['FloatRF'] = float(FloatRF.find('LeakageEnergy').text)
    leakageEnergy['IntALU'] = float(IntALU.find('LeakageEnergyALU').text)
    leakageEnergy['IntMul'] = float(IntMul.find('LeakageEnergy').text)
    leakageEnergy['IntDiv'] = float(IntDiv.find('LeakageEnergy').text)
    leakageEnergy['FloatALU'] = float(FloatALU.find('LeakageEnergy').text)
    leakageEnergy['FLoatMul'] = float(FloatMul.find('LeakageEnergy').text)
    leakageEnergy['FloatDiv'] = float(FloatDiv.find('LeakageEnergy').text)
    leakageEnergy['ICache'] = float(ICache.find('LeakageEnergy').text)
    leakageEnergy['L1Cache'] = float(L1Cache.find('LeakageEnergy').text)
    
    dynamicEnergy['Decode'] = float(Decode.find('DynamicEnergy').text)
    dynamicEnergy['IntRF'] = float(IntRF.find('DynamicEnergy').text)
    dynamicEnergy['FloatRF'] = float(FloatRF.find('DynamicEnergy').text)
    dynamicEnergy['IntALU'] = float(IntALU.find('DynamicEnergyALU').text)
    dynamicEnergy['IntMul'] = float(IntMul.find('DynamicEnergy').text)
    dynamicEnergy['IntDiv'] = float(IntDiv.find('DynamicEnergy').text)
    dynamicEnergy['FloatALU'] = float(FloatALU.find('DynamicEnergy').text)
    dynamicEnergy['FLoatMul'] = float(FloatMul.find('DynamicEnergy').text)
    dynamicEnergy['FloatDiv'] = float(FloatDiv.find('DynamicEnergy').text)
    dynamicEnergy['ICacheRead'] = float(ICache.find('ReadDynamicEnergy').text)
    dynamicEnergy['ICacheWrite'] = float(ICache.find('WriteDynamicEnergy').text)
    dynamicEnergy['L1CacheRead'] = float(L1Cache.find('ReadDynamicEnergy').text)
    dynamicEnergy['L1CacheWrite'] = float(L1Cache.find('WriteDynamicEnergy').text)
except AttributeError:
    print "Config.py: One or more attributes for functional units are not available in config.xml file"
    sys.exit(1)

