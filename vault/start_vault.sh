#!/bin/bash


SECRETS_URL="https://raw.githubusercontent.com/adelcor/secret/main/secrets.txt"

# El archivo de entrada que contiene el texto a ser modificado
ARCHIVO_ENTRADA="./vault/init-vault-template.sh"
# El archivo de salida donde se guardará el resultado
ARCHIVO_SALIDA="./vault/init-vault.sh"

echo "SECRETS_URL es: $SECRETS_URL"
# Lee el valor actual de la variable de entorno GITHUB_TOKEN
TOKEN_URL="$SECRETS_URL"


# Verifica si la variable SECRETS_URL tiene contenido
if [ -z "$TOKEN_URL" ]; then
    echo "La variable SECRETS_URL está vacía. Por favor, asegúrate de que está correctamente configurada."
    exit 1
fi


# Aplica la sustitución de la URL en el archivo ya modificado para evitar sobreescribir los cambios
sed "s#\$SECRETS_URL#${TOKEN_URL}#g" "$ARCHIVO_ENTRADA" > "$ARCHIVO_SALIDA"

echo "Archivo modificado creado: $ARCHIVO_SALIDA"

