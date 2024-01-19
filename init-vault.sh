#!/bin/bash

# Inicia el servidor de Vault en modo de desarrollo
vault server -dev &

# Espera a que Vault esté listo
sleep 5

# Configura las variables de entorno para Vault
export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='myroot'

# Agrega secretos desde un archivo de texto (solo para corrección)
while IFS='=' read -r key value; do
    vault kv put secret/myapp/$key value="$value"
done < usr/local/bin/secrets.txt

wait
