import paho.mqtt.client as mqtt


# This is the Publisher
def connect():
    client = mqtt.Client()
    client.connect("localhost", 1883, 60)
    client.publish("simon/things/dtg", "0;0;0;0;100;");
    client.disconnect();

if __name__ == '__main__':
    client = mqtt.Client()
    client.connect("localhost", 1883, 60)
    client.publish("simon/things/dtg", "onbsndfkbjnlsndfb");
    client.disconnect();