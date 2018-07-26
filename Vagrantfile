$install_devstack= <<PACKSTACK

sudo yum -y update
sudo yum -y install https://www.rdoproject.org/repos/rdo-release.rpm
sudo yum -y install openstack-packstack
sudo su -
#packstack --allinone
packstack --gen-answer-file=/root/myanswerfile.txt

packstack --answer-file=/root/myanswerfile.txt

PACKSTACK


Vagrant.configure("2") do |config|
  
  config.vm.box = "centos/7"
  config.vm.hostname = "packstack"
   #config.vm.network "private_network", type: "dhcp"
    config.vm.network "private_network", ip: "192.168.27.50"
  #config.vm.provision :shell, :inline => $install_devstack
  
  
  
	 config.vm.provider "virtualbox" do |vb|
	  # Display the VirtualBox GUI when booting the machine
	  #vb.gui = true

	  # Customize the amount of memory on the VM:
	  vb.memory = "3072"
	end
	#config.vm.provision "shell",
	#	inline: "sudo yum update ; sudo yum install -y python"
		
		
	config.vm.provision "ansible" do |ansible|
		ansible.compatibility_mode="2.0"
		ansible.playbook ="packstack.yml"
	
	end
end
