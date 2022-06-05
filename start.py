import paho.mqtt.client as mqtt 
import time
import random
import Loggin as log

#create a rising value in return
class Sensor(object):
    def readtemp(self):
        return float(random.random()*10)
    def readhum(self):
        return float(random.random()*10)

broker_address= log._get_broker_address() #get data from login
client = mqtt.Client("Projekt") #create a new instance
client.connect(broker_address) #connect to broker

sensor = Sensor()
print('publishing data') #debug for user
temperature = 0 
humidity = 0
while True:
    temperature += sensor.readtemp()
    humidity += sensor.readhum()
    client.publish("sensor/temperature",temperature)
    client.publish("sensor/humidity",humidity)
    time.sleep(10)


