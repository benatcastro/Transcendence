#!/bin/bash

# Inicia el servidor de Vault en modo de desarrollo
vault server -dev &

# Espera a que Vault esté listo
sleep 5

# Configura las variables de entorno para Vault
export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='myroot'

# Agrega un secreto de prueba
vault kv put secret/hello foo=world
vault kv put secret/data/mi-secret valor="tu_valor_secreto"

wait
