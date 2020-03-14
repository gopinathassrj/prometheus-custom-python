#Using Vagrant Cloud - Ubuntu-18.04 version.
IMAGE_NAME = "bento/ubuntu-18.04"


Vagrant.configure("2") do |config|
    config.ssh.insert_key = false

    # Master Node 
    config.vm.define "masterk8s" do |master|
        master.vm.provider "virtualbox" do |v|
            v.memory = 2048
            v.cpus = 2
        end
        master.vm.box = IMAGE_NAME
        master.vm.network "private_network", ip: "192.168.100.20"
        master.vm.hostname = "masterk8s"
        master.vm.provision "updatehosts", type: "shell", :path => "updatehosts.sh"
        master.vm.provision "ansible" do |ansible|
            ansible.playbook = "k8s/master-playbook.yml"
            ansible.extra_vars = {
                node_ip: "192.168.100.20",
            }
        master.vm.provision "postinstall", type: "shell", :path => "postinstall.sh"
        end
    end
    #  Worker Node 
        config.vm.define "minions" do |node|
            node.vm.provider "virtualbox" do |v|
                v.linked_clone = true
                v.memory = 1024
                v.cpus = 1
            end
            node.vm.box = IMAGE_NAME
            node.vm.network "private_network", ip: "192.168.100.11"
            node.vm.hostname = "minions"
            node.vm.provision "updatehosts", type: "shell", :path => "k8s/updatehosts.sh"
            node.vm.provision "ansible" do |ansible|
                ansible.playbook = "k8s/node-playbook.yml"
                ansible.extra_vars = {
                    node_ip: "192.168.100.11",
                }
            end
        end
    
end

