#!/bin/bash

echo "123456@" | sudo -S docker-compose ps -a
echo "Your shell is currently working in '$(pwd)'"

echo "123456@" | sudo -S docker-compose down -d
echo "123456@" | sudo -S docker-compose ps -a
