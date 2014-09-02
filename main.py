import serial, xbee

ser = serial.Serial('/dev/ttyUSB0', 9600)
ser.close()
ser.open()
xbee = xbee.ZigBee(ser)

while True:
	frame = xbee.wait_read_frame()
	print frame