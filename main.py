import serial, xbee

ser = serial.Serial('/dev/ttyUSB0', 9600)
ser.close()
ser.open()
xb = xbee.ZigBee(ser)

while True:
	frame = ser.readline().strip().split(' ')
	if frame[0] == "INCR":
		print "Increment of lot: " + frame[1]
	elif frame[1] == "DECR":
		print "Decrement of lot: " + frame[1]
	