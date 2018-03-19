python broker.py
python publisher.py
python subscriber.py


#Example of how to use publiser
	topic cpu/temp
	publish 40C
	publish 50c
	cancel cpu/temp
	quit
#Example of how to use subscriber
	cpu/temp


# Sirapat N.
# Simple-mqtt
#First, run broker. After that, run publisher or subscriber. Would be better to publish topic before subscribe.
#In each terminal
	python broker.py
	python publisher.py
	python subscriber.py

# Terminate publisher.py by enter "quit" to avoid socket in used
