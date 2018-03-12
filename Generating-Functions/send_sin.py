import visa
import math
import time
import matplotlib.pyplot as plt

# phase in radians
pi = math.pi
def sin(keithley ,amplitude ,freq ,time_duration , phase):
    w = 2* pi *freq  #frequency
    X,Y=[],[]

    start = time.time()
    current=time.time()

    while (current-start < time_duration):
        t = current - start
        value =amplitude * math.sin(w * t + phase)
        X.append(value)
        Y.append(t)
        keithley.write("SOUR:VOLT:LEV "+ str(value))
        current=time.time()

#     print(len(X),len(Y))
    plt.plot(Y,X)
