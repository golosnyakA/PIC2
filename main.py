from tracemalloc import stop
import paho.mqtt.client as mqtt 
import telepot
from telepot.loop import MessageLoop
import time
import Loggin as log


broker_address = log._get_broker_address()
chat_id = log._get_chat_id()
token = log._get_token()

client = mqtt.Client() #create a new instance
client.connect(broker_address) #connect to broker


def on_connect(client,userdata,flags,rc):
    print("Connected with result code "+str(rc))
    

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print('From Telegram: ')
    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        command = msg['text']
        print('Command: ', command)
        if command == '/subscribe':
            client.subscribe('sensor/+') #Subscribing to both topics
            bot.sendMessage(chat_id, "You subscribed to the 3D printer")
        if command == '/stop':
            client.unsubscribe('sensor/+')
        if command == 'Fan on':
            hide_keyboard = {'hide_keyboard' : True}
            bot.sendMessage(chat_id, 'Fan is activated', reply_markup=hide_keyboard)
        if command == 'Ignore alarm':
            hide_keyboard = {'hide_keyboard' : True}
            bot.sendMessage(chat_id, 'Alarm is ignored', reply_markup=hide_keyboard)
            

def on_message(client,userdate,msg):
    if msg.topic == "sensor/temperature":
        bot.sendMessage(chat_id,"Temperature 3D- Printer: "+ msg.payload.decode('utf-8'))
    elif msg.topic == "sensor/humidity":
        bot.sendMessage(chat_id,"Humidity 3D- Printer: "+ msg.payload.decode('utf-8'))

    if(float(msg.payload.decode('utf-8')) > 85):
        bot.sendMessage(chat_id,'Fan on')
    elif(float(msg.payload.decode('utf-8')) > 50):
        show_keyboard = {'keyboard': [['Fan on','Ignore alarm']]}   
        bot.sendMessage(chat_id, 'Alarm Notification. What will u do?', reply_markup=show_keyboard) 
    



bot = telepot.Bot(token)
MessageLoop(bot, handle).run_as_thread()  #Bucle

print('bot on the loop..')

client.on_connect = on_connect
client.on_message = on_message
client.loop_forever()



while 1:
    time.sleep(10)


