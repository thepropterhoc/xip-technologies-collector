import serial, xbee, requests, threading, time
from Queue import Queue as q 

ser = serial.Serial('/dev/ttyUSB0', 9600)
ser.close()
ser.open()
xb = xbee.ZigBee(ser)

baseURL = "http://projectxip.com/api/lot/"

frames = q()

class reader(threading.Thread):
	def run(self):
		while True:
			frame = frames.get()
			if frame[0] == "INCR":
				print requests.post(baseURL + "increment/"+ frame[1])
				print "Increment of lot: " + frame[1]
			elif frame[0] == "DECR":
				print requests.post(baseURL + "decrement/" + frame[1])
				print "Decrement of lot: "  + frame[1]
		
read = reader()
read.start()

while True:
	frame = ser.readline().strip().split(' ')
	frames.put(frame)