import requests
import paho.mqtt.client as mqtt

broker = '192.168.1.103'
client = mqtt.Client("P1")
client.username_pw_set('homeassistant', password='password')
client.connect(broker)
url = 'http://192.168.1.235/json'
x =  requests.get(url)
for k,v in x.json().items():
        try:
                client.publish("purpleair/"+str(k),v)
                print(str(k)+' - '+str(v))
                print('success')
        except:
                print('Failed: '+str(k))
                continue
