https://github.com/gopinathassrj/prometheus-custom-python

# prometheus-custom-python
prometheus-custom-python demo

This repo published to monitor the customer URL using Python along with Prometheus monitoring and Dashboard to Grafana


Pre-requesities:

Following software need to be installed before triggering the vagrant up command

1. Vagrant
2. VirtualBox 
3. Git

Execution steps: 

Please follow step by steps instruciton given below
1. git init 
2. git clone https://github.com/gopinathassrj/prometheus-custom-python.git
3. $ ls
Vagrantfile	master-playbook.yml	node-playbook.yml	postinstall.sh		updatehosts.sh

4. $ vagrant up
Wait for while the K8s cluster getting ready

5. $ vagrant status
Current machine states:

masterk8s                 running (virtualbox)
minions                   running (virtualbox)

This environment represents multiple VMs. The VMs are all listed
above with their current state. For more information about a specific
VM, run `vagrant status NAME`.

6. $ vagrant ssh masterk8s

7. Check if the promethus server started else start by invoking following command

vagrant@masterk8s:~$ sudo -i
root@masterk8s:~# ls
root@masterk8s:~# cd /home/vagrant/
root@masterk8s:/home/vagrant# ls
prometheus-2.4.2.linux-amd64  prometheus-2.4.2.linux-amd64.tar.gz  prometheus-custom-python
root@masterk8s:/home/vagrant# vi prometheus-2.4.2.linux-amd64
root@masterk8s:/home/vagrant# cd prometheus-2.4.2.linux-amd64/
root@masterk8s:/home/vagrant/prometheus-2.4.2.linux-amd64# ./prometheus &
[1] 27282
root@masterk8s:/home/vagrant/prometheus-2.4.2.linux-amd64# level=info ts=2020-03-14T21:02:56.428254563Z caller=main.go:238 msg="Starting Prometheus" version="(version=2.4.2, branch=HEAD, revision=c305ffaa092e94e9d2dbbddf8226c4813b1190a0)"
level=info ts=2020-03-14T21:02:56.428357923Z caller=main.go:239 build_context="(go=go1.10.3, user=root@dcde2b74c858, date=20180921-07:22:29)"
level=info ts=2020-03-14T21:02:56.428388363Z caller=main.go:240 host_details="(Linux 4.15.0-51-generic #55-Ubuntu SMP Wed May 15 14:27:21 UTC 2019 x86_64 masterk8s (none))"
level=info ts=2020-03-14T21:02:56.428408116Z caller=main.go:241 fd_limits="(soft=1024, hard=1048576)"
level=info ts=2020-03-14T21:02:56.428423717Z caller=main.go:242 vm_limits="(soft=unlimited, hard=unlimited)"
level=info ts=2020-03-14T21:02:56.429239332Z caller=web.go:397 component=web msg="Start listening for connections" address=0.0.0.0:9090
level=info ts=2020-03-14T21:02:56.429236802Z caller=main.go:554 msg="Starting TSDB ..."
level=info ts=2020-03-14T21:02:56.435133507Z caller=main.go:564 msg="TSDB started"
level=info ts=2020-03-14T21:02:56.435210559Z caller=main.go:624 msg="Loading configuration file" filename=prometheus.yml
level=info ts=2020-03-14T21:02:56.435986806Z caller=main.go:650 msg="Completed loading of configuration file" filename=prometheus.yml
level=info ts=2020-03-14T21:02:56.436088577Z caller=main.go:523 msg="Server is ready to receive web requests."

8. Invoke customer script to monitor the url

root@masterk8s:/home/vagrant/prometheus-custom-python# ls
README.md  Vagrantfile  http_check.py  master-playbook.yml  node-playbook.yml  postinstall.sh  updatehosts.sh
root@masterk8s:/home/vagrant/prometheus-custom-python# python3 http_check.py
DEBUG ---- Method Called
DEBUG ---- Method Called
DEBUG ---- Method Called
DEBUG ---- Method Called
DEBUG ---- Method Called


9. Access the Prometheus url with port number 9090, check the targets, Metrics and Graphs

 
 

 

10. Create a dashboard in Grafana accessing the url with port number 3000

 


