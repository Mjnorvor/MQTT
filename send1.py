import paho.mqtt.client as mqtt


connected = False

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to HTU")
        global connected 
        connected = True  

    else:
        print("Connection failed")


client = mqtt.Client()
client.on_connect = on_connect
client.connect("2.tcp.eu.ngrok.io", 17913, 60)
client.loop_start()
while connected:
    message = input("Message: ")
    client.publish("UG/MJNORVOR", message)
    
client.loop_forever()