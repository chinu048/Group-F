import math
from time import time
import matplotlib.pyplot as plt
import sys,os
import visa
# sys.path.append(os.path.dirname(os.getcwd()) + "/Set-UP" )
# import set_connection

def set_volt(keithley, volt_range = 20,res_range = 1000, compliance = 0.5):
    keithley.write('*RST')
    keithley.write(":SENSE:FUNCTION 'RES'")
    keithley.write(':SENSE:RES:MODE MANUAL')
    keithley.write(':SENSE:RES:RANGE ' + str(res_range))
    keithley.write(':SOURCE:FUNCTION VOLTAGE')
    keithley.write(':SOURCE:VOLTAGE:RANGE ' + str(volt_range))
    # keithley.write(':SOURCE:VOLTAGE ' + volt)
    keithley.write(':SYSTEM:RSENSE ON')
    keithley.write(':SENSE:CURR:PROT ' + str(compliance))
    # keithley.write(':FORMAT:ELEMENTS CURR')
    # keithley.write(':OUTPUT ON')
    # r = keithley.query_ascii_values("meas?")
    return keithley

def calculate_volt(keithley):
    # keithley.write(':OUTPUT ON')
    r = keithley.query_ascii_values("meas?")
    # print(r)
    return r

def constant(keithley,amplitude,totalTime,compliance,voltageRange,resistanceRange):
    my_tuple = []
    keithley = set_volt(keithley,voltageRange,resistanceRange,compliance)
    keithley.write(':SOURCE:VOLTAGE ' + str(amplitude))

    timestamp = []
    start = time()
    while (time()-start < totalTime):
        my_tuple.append(calculate_volt(keithley))
        timestamp.append(time()-start)
    return (my_tuple,timestamp)

def main(amplitude,totalTime,compliance = 0.5,voltageRange = 20,resistanceRange = 1000):
    rm = visa.ResourceManager()
    if "GPIB0::20::INSTR" in rm.list_resources():
        keithley = rm.open_resource("GPIB0::20::INSTR")

    return constant(keithley,amplitude,totalTime,compliance,voltageRange,resistanceRange)
