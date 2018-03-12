import serial
import time
def en(i):
    return i

arduino = serial.Serial('/dev/ttyACM0', 9600)
# print(arduino.readLine())
print("Annoying cunt")
a,b,c,d=200,100,120,50
print("Annoying cunt")
time.sleep(2)

arduino.write(en(a))
print("Annoying cunt")
time.sleep(2)
print("Annoying cunt")
print("tik")

arduino.write(en(b))
time.sleep(2)
print("tok")

arduino.write(en(c))
time.sleep(2)
print("tik")

arduino.write(en(d))
print("tok")

print("done")
# Arduino_Serial = serial.Serial('/dev/ttyACM0',9600)  #Create Serial port object called arduinoSerialData
# # print Arduino_Serial.readline()               #read the serial data and print it as line
# print ("Enter 1 to ON LED and 0 to OFF LED")
#
# while 1:                                      #infinite loop
#     input_data = input().encode()                  #waits until user enters data
#     print ("you entered", input_data)           #prints the data for confirmation
#
#     if (input_data ):
#         print("here")                #if the entered data is 1
#         Arduino_Serial.write(input_data)             #send 1 to arduino
#         print ("LED ON")
#
#
#     if (input_data == '0'):                   #if the entered data is 0
#         Arduino_Serial.write('0')             #send 0 to arduino
#         print ("LED OFF")
