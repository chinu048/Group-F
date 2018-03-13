import serial
import time

i=serial.Serial('/dev/ttyACM0', 9600)
ON = int(1)
OFF = int(0)

OnTime = int(input("Enter the \"OnTime\" \n"))
OffTime = int(input("Enter the \"OffTime\"\n"))
TotalTime = int(input("Enter the time duration of the experiment \n"))

start = time.time()
current = start
while (current - start) < TotalTime):
        i.write(ON)
        time.sleep(OnTime)
        current = time.time()
        if ( current - start > TotalTime):
            break
        i.write(OFF)
        time.sleep(OffTime)

print("done")
