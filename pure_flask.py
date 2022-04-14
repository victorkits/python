from time import sleep

import consul
from consul import Check
from flask import Flask, Response

app = Flask(__name__)


def register_service(client):
    while True:
        try:
            client.agent.service.register(name='local', service_id='1', address='localhost', port=8000)  # integrated service registration <3
            break
        except (ConnectionError, consul.ConsulException):
            print('consul host is down, reconnecting...')
            sleep(0.5)


def register_agent(client):
    # check = Check.http("localhost:8000/health", interval='5s', timeout='10s', deregister='60')
    while True:
        try:
            req = client.agent.check.register(name='Test micro', check_id="1", notes="python micro", service_id="1", token=None, interval='10s', http="http://localhost:8000/health", timeout='10s')
            # integrated service registration <3
            break
        except Exception as ex:
            print(ex)
            print('consul1 host is down, reconnecting...')
            sleep(0.5)


c = consul.Consul(host='localhost', port=8500, token=None, scheme='http', consistency='default', dc='dc1', verify=True, cert=None)
# register_service(c)
# Health check
# register_agent(c)


@app.route('/')
def get_invoice():
    res = c.status.leader()
    return res


@app.route('/health', methods=['GET'])
def hc():
    resp = Response("Ok", status=200)
    return resp


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8000)
