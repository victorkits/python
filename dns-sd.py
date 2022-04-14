import logging

import dns.query
import dns.resolver
import dns.resolver
from flask import Flask, request, Response

app = Flask(__name__)


class ServiceDiscovery:

    def __init__(self, domain):
        self.domain = domain
        pass

    def get_service(self, svc_name: str, ns_rec_type='SRV'):
        try:
            req = dns.resolver.resolve(svc_name + self.domain, ns_rec_type)
            service_info = {}
            if ns_rec_type == 'SRV':
                for srv in req:
                    service_info['weight'] = srv.weight
                    service_info['host'] = str(srv.target).rstrip('.')
                    service_info['priority'] = srv.priority
                    service_info['port'] = srv.port
            elif ns_rec_type == 'A':
                for srv in req:
                    service_info['address'] = srv.address

            return service_info
        except Exception as ex:
            print(f'ERROR:  {ex}')


@app.route('/')
def get_svc_param():

    app.logger.info(request.args.to_dict())
    q = request.args
    domain = q.get('domain')
    srvt = q.get('rtype')
    # in tomato
    # domain = '_logger._tcp.int.hub.local.'
    resp = ServiceDiscovery.get_service(domain, srvt)
    app.logger.info(f'_____DNS_response: {resp}')
    return Response(resp, status=200)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
