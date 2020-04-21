import json
import time
import os

while True:
	dataset = json.load(open("data.json"))
	a = input("Enter to find the meaning")
	print(dataset[a])

	