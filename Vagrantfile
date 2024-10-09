# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "archlinux/archlinux"
  
  # Port forwarding from guest VM port 5000 to host machine port 8080
  config.vm.network "forwarded_port", guest: 5000, host: 8080, auto_correct: true

  # File provisioner to upload hello.py to the VM
  config.vm.provision "file", source: "./hello.py", destination: "/home/vagrant/hello.py"

  # Shell provisioner to install necessary packages and configure the environment
  config.vm.provision "shell", inline: <<-SHELL
    # Update and install necessary packages
    sudo pacman -Syu --noconfirm
    sudo pacman -S --noconfirm python python-pip

    # Install Flask
    sudo pip install Flask

    # Ensure the hello.py is executable
    chmod +x /home/vagrant/hello.py

    # Command to run Flask app on boot
    echo "FLASK_APP=/home/vagrant/hello.py flask run --host=0.0.0.0 --port=5000" >> /home/vagrant/.bash_profile
  SHELL
end
