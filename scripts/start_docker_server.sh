#!/bin/bash

echo "Your shell is currently working in '$(pwd)'"

echo "123456@" | sudo -S docker-compose up -d
echo "123456@" | sudo -S docker-compose ps -a


