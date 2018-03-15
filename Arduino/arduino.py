import serial
import time

i=serial.Serial('/dev/ttyACM0', 9600)

def ard(ontime,offtime,totaltime):
	s=time.time()
	e=time.time()
	while ((e-s)<totaltime):
        	i.write(str(1).encode())
        	time.sleep(ontime)
        	i.write(str(0).encode())
        	time.sleep(offtime)
        	e=time.time()

i.write(str(0).encode())

