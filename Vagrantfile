# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "archlinux/archlinux"
  config.vm.network "forwarded_port", guest: 5000, host: 8080, host_ip: "127.0.0.1"

  # Sync hello.py to the guest VM under /vagrant
  config.vm.synced_folder ".", "/vagrant", type: "virtualbox"

  config.vm.provision "shell", inline: <<-SHELL
    # Update system and install Python, pip, and Flask
    sudo pacman -Syu --noconfirm
    sudo pacman -S --noconfirm python python-pip
    sudo pip install Flask

    # Copy hello.py to the home directory and ensure it has correct permissions
    cp /vagrant/hello.py /home/vagrant/hello.py
    chmod +x /home/vagrant/hello.py

    # Start the Flask app
    FLASK_APP=/home/vagrant/hello.py flask run --host=0.0.0.0
  SHELL
end
