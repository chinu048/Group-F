# phase in radians
def sin(amplitude ,freq ,time_duration , phase):
    pi = math.pi
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
