#!/bin/bash

echo "Your shell is currently working in '$(pwd)'"
cd /home/ubuntu/
echo "ubuntu@" | sudo -S docker-compose up -d
echo "ubuntu@" | sudo -S docker ps -a


