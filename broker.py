# Slothy group - simple mqtt
# Sirapat N. - Thanaboon M. - Sunhakoch

from socket import * 
import thread
import sys
import time

SERV_PORT = 50000

# Global dictionary for publisher and subscriber
global dict_topic
dict_topic = {}
# Flag for checking whether the topic is canceled or not
global cancel_flag
cancel_flag = False

# Control loops and also use for break 2 loops
keeplooping = True

# Handle multiple publishers and subscribers
def handle_client(s, keeplooping):
  while keeplooping:
     global dict_topic
     global cancel_flag
     role = "publisher"
     # Get input from clients (publisher or subscriber)
     txtin = s.recv(1024).split(" ")

     if (txtin[0] == 'quit'):
        break
     # Publish a topic
     elif (txtin[0] == "topic"):
        topic = txtin[1]
        dict_topic[topic] = "Existed topic with no data yet"
        print "Topic: " + topic + " has been published\n"
     # Publish the data to existed topic
     elif (txtin[0] == "publish"):
        data = txtin[1]
        dict_topic[topic] = data
        print "Data: " + data + " has been published to Topic: " + topic
     # Cancel the existed topic
     elif (txtin[0] == "cancel"):
        topic = txtin[1]
        # Delete dictionary with topic key to cancel topic
        if (dict_topic.get(topic) != None):
            del dict_topic[topic]
            print "Topic: " + topic + " has been canceled\n"
        else:
            print "ERROR!, There is no topic name: " + topic + "\n"
        cancel_flag = True
     else: # subscriber 
        role = "subscriber"
        sub_topic = txtin[0]
        old_message = None
        while keeplooping:
            # Retrieve data from subscribed topic
            sub_data = dict_topic.get(sub_topic)
            if (sub_data != None):
                # return data to the subscriber
                if (old_message != sub_data):
                    s.send(sub_data)
                old_message = sub_data
            else:
                # Checking whether the topic is canceled or not
                if (cancel_flag == True):
                    response_message = "This topic is canceled or not published yet"
                    if (old_message != response_message):
                        s.send(response_message)
                    old_message = response_message
                    # cancel_flag = False
                    keeplooping = False # disconnect & unsubscribe when cancel subscribed topic
                else:
                    response_message = "This topic isn't published yet..."
                    if (old_message != response_message):
                        s.send(response_message)
                    old_message = response_message
            time.sleep(1)
  s.close()
  return

# localhost
addr = ('127.0.0.1', SERV_PORT)
s = socket(AF_INET, SOCK_STREAM)
s.bind(addr)
s.listen(5)
print 'MQTT Broker server is running ...'

while True:
  # Accept incoming request and keep return values (socket object and address)
  sckt, addr = s.accept()
  print '\nNew client connected from ..', addr
  # Summond client thread for publisher or subscriber 
  thread.start_new_thread(handle_client, (sckt,keeplooping))

s.close()
