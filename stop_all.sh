#!/bin/bash

# Detiene todos los contenedores de Docker
sudo docker stop $(sudo docker ps -aq)

