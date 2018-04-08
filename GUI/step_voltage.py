import math
import time
import matplotlib.pyplot as plt
import sys,os
import visa
# sys.path.append(os.path.dirname(os.getcwd()) + "/Set-UP" )
# import set_connection

def set_volt(keithley, volt_range ,res_range , compliance ):
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

def step(keithley,begin,stop,steps,compl,volt_range,res_range):
    slope = float(stop - begin)/float(steps)
    my_tuple = []
    keithley = set_volt(keithley,volt_range,res_range,compl)
    keithley.write(':OUTPUT ON')


    timestamp = []
    start = time.time()
    current = time.time()
    counter = 0
    while (counter <= steps):
        value = float(begin) + float(slope * counter)
        if value != 0:    
            keithley.write(':SOURCE:VOLTAGE ' + str(value))
            my_tuple.append(calculate_volt(keithley))
            # print(calculate_volt(keithley)[2])
            timestamp.append(current-start)
            current = time.time()
        counter = counter + 1
    # keithley.write(':OUPTUT OFF')
    keithley.write('*RST')
    # print(my_tuple,timestamp)
    return (my_tuple,timestamp)

def main(begin,stop,steps,compl = 0.5,volt_range = 20,res_range = 1000):
    rm = visa.ResourceManager()
    if "GPIB0::20::INSTR" in rm.list_resources():
        keithley = rm.open_resource("GPIB0::20::INSTR")

    return step(keithley,begin,stop,steps,compl,volt_range,res_range)

'''if __name__ == '__main__':
    rm = visa.ResourceManager()
    if "GPIB0::20::INSTR" in rm.list_resources():
        keithley = rm.open_resource("GPIB0::20::INSTR")
    (a,b) = step(keithley,0,10,7)
    c=[]
    d=[]
    for (tup,time) in zip(a,b):
        if(tup[2]>=1000):
            c.append(tup[2])
            d.append(time)
            print(tup[2],time)
    plt.plot(d,c)
    plt.show()
    # print(a)
    # keithley.write('*RST')'''
