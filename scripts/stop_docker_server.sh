#!/bin/bash

sudo docker ps -a
echo "Your shell is currently working in '$(pwd)'"
cd /home/ubuntu/
sudo docker-compose down
sudo docker ps -a
