#!/bin/bash

echo "Your shell is currently working in '$(pwd)'"

sudo docker-compose up -d
sudo docker ps -a


