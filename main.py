import serial, xbee, requests

ser = serial.Serial('/dev/ttyUSB0', 9600)
ser.close()
ser.open()
xb = xbee.ZigBee(ser)

baseURL = "http://projectxip.com/api/lot/"

with open('log.txt', 'a') as f:
	while True:
		frame = ser.readline().strip().split(' ')
		if frame[0] == "INCR":
			try:
				print requests.post(baseURL + "increment/"+ frame[1])
			except:
				f.write("Failed to push increment")
			f.write("Increment of lot: " + frame[1])
		elif frame[0] == "DECR":
			print requests.post(baseURL + "decrement/" + frame[1])
			try:
				print "Decrement of lot: "  + frame[1]
			except:
				f.write("Failed to push decrement")
			f.write("Decrement of lot: " + frame[1])
