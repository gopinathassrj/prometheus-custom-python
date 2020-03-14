#!/usr/bin/env python3
import requests as req
import time
from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily
from prometheus_client import start_http_server

def check_url(web_url):
    print("DEBUG ---- Method Called")
    res = req.request(method='GET',url=web_url)
    if res.status_code != 200:
        return 0
    else:
        return 1


class CustomCollector(object):
    def __init__(self):
        pass
    def collect(self):
        g = GaugeMetricFamily("sample_external_http_service", 'Website Status', labels=['website'])
        g.add_metric(["https://httpstat.us/503"], check_url("https://httpstat.us/503"))
        g.add_metric(["https://httpstat.us/200"], check_url("https://httpstat.us/200"))
        yield g

if __name__ == '__main__':
    start_http_server(8080)
    REGISTRY.register(CustomCollector())
    collector_obj = CustomCollector()
    while True:
        time.sleep(1)
        collector_obj.collect()
