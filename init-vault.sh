#!/bin/bash

# Inicia el servidor de Vault en modo de desarrollo
vault server -dev &

# Espera a que Vault esté listo
sleep 5

# Configura las variables de entorno para Vault
export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='myroot'

# Agrega un secreto de prueba
# vault kv put secret/myapp clave1="valor1" clave2="valor2" clave3="valor3"
while IFS='=' read -r key value; do
    vault kv put secret/myapp/$key value="$value"
done < usr/local/bin/secrets.txt

wait
