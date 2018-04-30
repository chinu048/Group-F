import serial
import time
#i=serial.Serial('/dev/ttyACM0', 9600)
i=serial.Serial('COM3', 9600)
def ard(ontime,offtime,totaltime):
        time.sleep(1)
        i.write(str(ontime).encode())
        time.sleep(1)
        i.write(str(offtime).encode())
        time.sleep(1)
        i.write(str(totaltime).encode())
