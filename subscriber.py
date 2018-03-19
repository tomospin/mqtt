# Slothy group - simple mqtt
# Sirapat N. - Thanaboon M. - Sunhakoch
from socket import * 
import sys
import time

MAX_BUF = 2048
SERV_PORT = 50000

addr = ('127.0.0.1', SERV_PORT)
s = socket(AF_INET, SOCK_STREAM)
s.connect(addr)

print "Connected to the broker successfully\n"
old_message = None
topic_name= raw_input("Enter a TOPIC_NAME to subscribe\n")

# ignore topic/publish/cancel functions in Subscriber
if (topic_name.startswith("topic") or topic_name.startswith("publish") or topic_name.startswith("cancel")):
	print "ERROR! This is subscriber, USAGE: TOPIC_NAME"
	topic_name= raw_input("Enter a topic name to subscribe\n")
else:
	# Every topic name in the broker is replaced by - instead of space
	if " " in topic_name:
		topic_name = topic_name.replace(" ", "-")
	# send desired topic name to subscribe
	s.send(topic_name)
	print "Subscribing topic: " + topic_name
	while True:
		# get data from the subscribed topic
		receivedMessage = s.recv(2048)
		print receivedMessage
		# exit when the subscribed topic is canceled
		if (receivedMessage == "This topic is canceled or not published yet"):
			break
		time.sleep(1)
s.close()
