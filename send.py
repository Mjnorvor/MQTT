import paho.mqtt.client as mqtt
import time

# from window import window, WIN_CLOSED




def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MJNORVOR")
        global connected 
        connected = True  

    else:
        print("Connection failed")

connected = False

client = mqtt.Client()
client.on_connect = on_connect

try:
    while not connected:
        client.connect("2.tcp.eu.ngrok.io", 17913, 60)
        client.loop_start()

    while connected:
        
        # event, values = window.read()
        # if event == WIN_CLOSED or event == 'Cancel': # if user closes window or clicks cancel
        #     connected = False
        #     raise KeyboardInterrupt()
        # message = values[0]
        message = input("Message: ")
        client.publish("glblcd/MJNORVOR", message)

except KeyboardInterrupt:
    client.disconnect()
    client.loop_stop()
    # window.close()