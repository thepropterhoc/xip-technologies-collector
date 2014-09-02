import serial, xbee, requests

ser = serial.Serial('/dev/ttyUSB0', 9600)
ser.close()
ser.open()
xb = xbee.ZigBee(ser)

baseURL = "http://www.projectxip.com/api/lot/"

while True:
	frame = ser.readline().strip().split(' ')
	if frame[0] == "INCR":
		print requests.post(baseURL + "increment/"+ frame[1], data={}, header="application/json")
		#print "Increment of lot: " + frame[1]
	elif frame[1] == "DECR":
		print requests.post(baseURL + "decrement/" + frame[1], data={}, header="application/json")
		#print "Decrement of lot: "  + frame[1]
	