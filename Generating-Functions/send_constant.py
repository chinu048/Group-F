import math
import time
import matplotlib.pyplot as plt

def constant(keithley,amplitude,time_duration):

    X,Y=[],[]

    start = time.time()
    current=time.time()

    keithley.write("SOUR:VOLT:LEV "+ str(amplitude))

    while (current-start < time_duration):
        t = current - start
        value = amplitude
        X.append(value)
        Y.append(t)
        current = time.time()
        keithley.write("SOUR:VOLT:LEV 0")
        X.append(0)
        Y.append(current)

    plt.plot(Y,X)
