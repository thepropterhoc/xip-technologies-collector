import serial, xbee

ser = serial.Serial('/dev/ttyUSB0', 9600)
ser.close()
ser.open()
xb = xbee.ZigBee(ser)

while True:
	frame = xb.wait_read_frame()
	print str(frame)