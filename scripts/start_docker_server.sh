#!/bin/bash

#echo "Your shell is currently working in '$(pwd)'"
'''cd /home/ubuntu/
sudo docker-compose up -d
sudo docker ps -a'''

cd ./buycom/scripts
docker-compose up -d
docker ps -a


