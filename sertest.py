import serial

ser = serial.Serial('/dev/ttyUSB0',115200)

while(True):
	
	line = str(ser.readline())[42:-3]
	print(line) 
