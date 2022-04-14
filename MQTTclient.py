import datetime
import time

import paho.mqtt.client as mqtt

# This is the Subscriber

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("#")


def on_message(client, userdata, msg):
    now = datetime.datetime.now()
    time = now.strftime("%H:%M:%S:%f")
    gtd = '=>'

    dtg = '<='
    color = '\033[1;34m'
    multy = ' =BCast= '
    if 'gtd' in msg.topic:
        str = gtd
        color = '\033[0;32m'
    elif 'dtg' in msg.topic:
        str = dtg
        color = '\033[1;36m'
    elif 'telemetry' in msg.topic:
        str = 'telemetry'
    else:
        str = multy
    mes = msg.payload.decode().strip('\n')
    if '24;' in mes or '25;' in mes:
        pass
    else:
        # print(f'{time}    GW {str} {msg.topic} message: {mes}')
        print(f'{color}{time} GW {str} {msg.topic} message: {mes}')


if __name__ == '__main__':
    pass
    client = mqtt.Client()
    client.username_pw_set('admin', 'password')
    client.connect(host='localhost', port=1883, keepalive=60, )

    client.on_connect = on_connect
    client.on_message = on_message

    client.loop_forever()
