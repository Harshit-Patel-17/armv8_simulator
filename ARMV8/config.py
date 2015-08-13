import sys
import xml.etree.ElementTree as ET

configTreeRoot = ET.parse('config.xml').getroot()

latency = {}

try:
    IntALU = configTreeRoot.find('System').find('Core').find('IntShifterALU')
    IntMul = configTreeRoot.find('System').find('Core').find('IntMul')
    IntDiv = configTreeRoot.find('System').find('Core').find('IntDiv')
    FloatALU = configTreeRoot.find('System').find('Core').find('FloatALU')
    FloatMul = configTreeRoot.find('System').find('Core').find('FloatMul')
    FloatDiv = configTreeRoot.find('System').find('Core').find('FloatDiv')
    ICache = configTreeRoot.find('Library').find('ICache_32K_8')
    L1Cache = configTreeRoot.find('Library').find('L1Cache_32K_8')
except AttributeError:
    print "One or more attributes for functional units are not available in config.xml file"
    sys.exit(1)
    
latency['IntALU'] = int(IntALU.find('Latency').text)
latency['IntMul'] = int(IntMul.find('Latency').text)
latency['IntDiv'] = int(IntDiv.find('Latency').text)
latency['FloatALU'] = int(FloatALU.find('Latency').text)
latency['FLoatMul'] = int(FloatMul.find('Latency').text)
latency['FloatDiv'] = int(FloatDiv.find('Latency').text)
latency['ICache'] = int(ICache.find('Latency').text)
latency['L1Cache'] = int(L1Cache.find('Latency').text)