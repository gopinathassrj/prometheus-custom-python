#!/bin/bash
mv /home/vagrant/prometheus-custom-python/prometheus.yml /home/vagrant/prometheus-2.4.2.linux-amd64/prometheus.yml
cd /home/vagrant/prometheus-2.4.2.linux-amd64/
./prometheus & 
cd /home/vagrant/prometheus-custom-python/
python3 http_access.py &
