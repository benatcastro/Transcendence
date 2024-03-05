#!/bin/bash

# Detener todos los contenedores de Docker
echo "Deteniendo todos los contenedores..."
sudo docker stop $(sudo docker ps -aq)

# Eliminar todos los contenedores
echo "Eliminando todos los contenedores..."
sudo docker rm $(sudo docker ps -aq)

# Eliminar todas las imágenes de Docker
echo "Eliminando todas las imágenes..."
sudo docker rmi $(sudo docker images -q) --force

# Eliminar todos los volúmenes de Docker
echo "Eliminando todos los volúmenes..."
sudo docker volume rm $(sudo docker volume ls -q)

# Eliminar todas las redes de Docker
echo "Eliminando todas las redes..."
sudo docker network rm $(sudo docker network ls -q) 2> /dev/null

# Limpiar todos los recursos no utilizados (incluyendo imágenes, contenedores, volúmenes y redes)
echo "Ejecutando Docker system prune..."
sudo docker system prune -a -f --volumes

echo "Limpieza completa."

