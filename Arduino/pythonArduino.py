import serial
import time

i=serial.Serial('/dev/ttyACM0', 9600)

Off=(0)
OnTime=int(input("OnTime\n"))
OffTime=int(input("OffTime\n"))
TotalTime=int(input("TotalTime\n"))
intensity=int(input("Voltage\n"))
s=time.time()
e=time.time()
while ((e-s)<TotalTime):
        print(intensity,e-s)
        i.write(str(intensity).encode())
        time.sleep(OnTime)
        i.write(str(0).encode())
        time.sleep(OffTime)
        e=time.time()

i.write(str(0).encode())
