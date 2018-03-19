# Slothy group - simple mqtt
# Sirapat N. - Thanaboon M. - Sunhakoch
from socket import * 
import sys

MAX_BUF = 2048
SERV_PORT = 50000

addr = ('127.0.0.1', SERV_PORT)
s = socket(AF_INET, SOCK_STREAM)
s.connect(addr)

print "Connected to the broker successfully"
while True:
	# get function and topic/data from the user
	input = raw_input("\nEnter topic/cancel followed by TOPIC_NAME or publish followed by DATA or quit\n").split(" ")

	if (input[0] == "quit"):
		txtout = "quit"
	else:
		function = input[0]
		# prompt for function
		if (function == "topic" or function == "publish" or function == "cancel"):
			txtout = input[0] + " " + input[1]
			# if the topic name contains space , then change it to -
			if (len(input) > 2):
				for index in range(2,len(input)):
					txtout = txtout + "-" + str(input[index])
				print "Your topic name's space is automatically replaced by -"
			print "Sending : " + txtout + " to the broker"
		else:
			print "ERROR! USAGE: FUNCTION TOPIC_NAME/DATA\n"
			continue
	# command to the broker (topic/publish/cancel)
	s.send(txtout)

	if (txtout == "quit"):
		break

s.close()
