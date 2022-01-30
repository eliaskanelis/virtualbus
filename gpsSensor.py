#!/usr/bin/env python3

from virtualbus.client import Client

import random
import time
import argparse

class GPS():
	def __init__(self, host, port):
		self.client = Client(host, port)

		self.i = 0
		self.nmeaSentenceList = []
		self.nmeaSentenceListLen = len(self.nmeaSentenceList)

	def load(self, nmeaFilePath):

		# Open file
		try:
			nmea_file = open( nmeaFilePath,'r' )
		except Exception:
			print("Can not open nmea file!")
			return 1

		# Create a list with nmea sentences exctracted from the nmea file
		self.i = 0
		self.nmeaSentenceList = []
		while True:
			rv = nmea_file.readline()
			if rv == "":
				break

			#print( "Line: {}".format( rv ) )
			self.nmeaSentenceList.append( rv.rstrip() )

		# Measure the number of nmea sentences inthe list
		self.nmeaSentenceListLen = len(self.nmeaSentenceList)

	def unload(self):
		self.i = 0
		self.nmeaSentenceList = []
		self.nmeaSentenceListLen = len(self.nmeaSentenceList)

	def run(self):
		if self.nmeaSentenceListLen is 0:
			# Not any NMEA available
			return 1

		# Sent NMEA sentences
		nmea = self.nmeaSentenceList[self.i]
		self.client.sent(nmea)
		print( "GPS NMEA[{}]: '{}'".format(self.i, nmea))

		# Iterate over nmea sentences
		self.i += 1
		if self.i >= self.nmeaSentenceListLen:
			self.i = 0

def main():

	try:
		# Parser
		parser = argparse.ArgumentParser( prog="gpsSensor",
						  description = "Fake GPS sensor",
						  fromfile_prefix_chars="@" )

		parser.add_argument("-a", "--address",
				    help = "Selects the server ip address or hostname. Default is 'localhost'",
				    default = "localhost")
		parser.add_argument("-p", "--port",
				    help = "When mode is socket, selects the server port. Default is '8888'",
				    type = int, default = 8888)

		args = parser.parse_args()

		# Sensor
		s = GPS(host=args.address, port=args.port)
		s.load("nmea.txt")
		while True:
			s.run()

			time.sleep( 0.05 )

	except KeyboardInterrupt as e:
		pass


if __name__ == "__main__":
	main()
