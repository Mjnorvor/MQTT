import paho.mqtt.client as mqtt
# import PySimpleGUI as sg

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("glblcd")

def on_message(client, userdata, msg):
    print(msg.topic + " \n " + msg.payload.decode("utf-8") + " \n ")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("2.tcp.eu.ngrok.io", 17913, 60)

client.loop_forever()

