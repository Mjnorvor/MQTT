import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MJNORVOR")
        global Connected 
        Connected = True  

    else:
        print("Connection failed")
        
        
Connected = False
        
client = mqtt.Client()
client.on_connect = on_connect
client.connect("197.255.72.184", 1883, 60)
client.loop_start()

while Connected != True:
    time.sleep(0.1)
    
try:
    while True:
        message = input('Message: ')
        client.publish("glblcd/sam", message)

except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
    
