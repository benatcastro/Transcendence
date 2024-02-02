#!/bin/bash

# Cambia al directorio donde se encuentra vault.yml si es necesario
# cd /path/to/your/vault/directory

echo "Creando variables de entorno..."
docker compose -f vault.yml build
docker compose -f vault.yml up -d

# Espera a que se cree el archivo .env
echo "Esperando a que se genere el archivo .env..."
while [ ! -f ".env" ]; do
  sleep 5
done

echo "Archivo .env encontrado. Ejecutando Secuencia de inicio de Cyberpong..."
make

