#!/usr/bin/env python3

from virtualbus.vBusClient import VBusClient

import random


def main():
	b = VBusClient(host="127.0.0.1", port=8888, logging=False)
	try:
		while True:
			msg = b.receive()
			print("Received: '{}'".format(msg))

	except KeyboardInterrupt as e:
		pass

if __name__ == "__main__":
	main()
