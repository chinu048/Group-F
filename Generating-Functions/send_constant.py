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

def calculate_volt(keithley, volt = 10, volt_range = 20,res_range = 1000, compliance = 0.5):
    # keithley.write(':OUTPUT ON')
    r = keithley.query_ascii_values("meas?")
    # print(r)
    return r

def constant(keithley,amplitude,time_duration):
    my_tuple = []
    keithley = set_volt(keithley)
    keithley.write(':SOURCE:VOLTAGE ' + str(10))

    timestamp = []
    start = time()
    while (time()-start < time_duration):
        my_tuple.append(calculate_volt(keithley))
        timestamp.append(time()-start)
    return (my_tuple,timestamp)

def main():
    rm = visa.ResourceManager()
    if "GPIB0::20::INSTR" in rm.list_resources():
        keithley = rm.open_resource("GPIB0::20::INSTR")

    constant(keithley,10,10)
if __name__ == '__main__':
    main()




# def set_curr(keithley, curr = 10, curr_range = 20,res_range = 1000, compliance = 0.5):
#     # keithley = general_setup()
#     # keithley = rm.open_resource("GPIB0::20::INSTR")
#     keithley.write('*RST')
#     keithley.write(":SENSE:FUNCTION 'RES'")
#     keithley.write(':SENSE:RES:MODE MANUAL')
#     keithley.write(':SENSE:RES:RANGE ' + res_range)
#     keithley.write(':SOURCE:FUNCTION VOLTAGE')
#     keithley.write(':SOURCE:CURRENT:RANGE ' + curr_range)
#     # keithley.write(':SOURCE:VOLTAGE ' + curr)
#     keithley.write(':SYSTEM:RSENSE ON')
#     keithley.write(':SENSE:CURR:PROT ' + compliance)
#     # keithley.write(':FORMAT:ELEMENTS CURR')
#     # keithley.write(':OUTPUT ON')
#     # r = keithley.query_ascii_values("meas?")
#     return keithley
# #

# def calculate_curr(keithley, curr = 10, curr_range = 20, res_range = 1000, compliance = 0.5):
#     keithley = general_setup()
#     keithley = rm.open_resource("GPIB0::20::INSTR")
#     keithley.write('*RST')
#     keithley.write(":SENSE:FUNCTION 'RES'")
#     keithley.write(':SENSE:RES:MODE MANUAL')
#     keithley.write(':SENSE:RES:RANGE ' + res_range)
#     keithley.write(':SOURCE:FUNCTION VOLTAGE')
#     keithley.write(':SOURCE:CURRENT:RANGE ' + curr_range)
#     keithley.write(':SOURCE:CURRENT ' + curr)
#     keithley.write(':SYSTEM:RSENSE ON')
#     keithley.write(':SENSE:CURR:PROT ' + compliance)
#     keithley.write(':FORMAT:ELEMENTS CURR')
#     keithley.write(':OUTPUT ON')
#     r = keithley.query_ascii_values("meas?")
#     return keithley
#
#     # ans = keithley.query_ascii_values(':READ?')
