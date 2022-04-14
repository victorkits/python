import datetime
import ssl
from paho.mqtt import client as mqtt_client


user = '3_48dwip2cdv0gwc884kcow8ckcgg0sk4o4o0o88c4wg0gk404cs'
passw = '5odb2r0p6dc0wwgw8gg004o40wc48gsgssgg8g0480kokgo0o0'
host = 'mqtt.simon-cloud.com'
client_id = 'api_sns_Viktor'
topic  = 'simon/telemetry/b827eb5936cd/#'  # Jose Luis installation
# topic  = 'simon/telemetry/b827ebc5abf3/#'
topic1 = 'simon/telemetry/b827eb7699c1/#'
topic2 = 'simon/telemetry/b827ebccd81a/#'


def on_message(client, userdata, msg):
    now = datetime.datetime.now()
    time = now.strftime("%H:%M:%S")
    mes = msg.payload.decode()
    topic = msg.topic
    print(f'{time} received {topic} message: {mes}')


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    cert_required = ssl.CERT_REQUIRED
    client.tls_set(ca_certs=None, certfile=None, keyfile=None,
                   cert_reqs=cert_required)

    client.username_pw_set(user, passw)

    client.on_connect = on_connect
    client.connect(host, 8883)
    return client


def subscribe(client: mqtt_client):
    client.subscribe(topic)
    client.on_message = on_message


def subscribe1(client: mqtt_client):
    client.subscribe(topic1)
    client.on_message = on_message


def subscribe2(client: mqtt_client):
    client.subscribe(topic2)
    client.on_message = on_message


if __name__ == '__main__':
    client = connect_mqtt()
    subscribe(client)
    subscribe1(client)
    subscribe2(client)
    client.loop_forever()


