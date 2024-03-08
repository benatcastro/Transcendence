#!/bin/bash

# Detiene todos los contenedores de Docker
docker stop $(docker ps -aq)

