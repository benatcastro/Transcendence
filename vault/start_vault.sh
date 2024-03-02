#!/bin/bash


SECRETS_URL="https://raw.githubusercontent.com/adelcor/secret/main/secrets.txt"
GITHUB_TOKEN="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"

# El archivo de entrada que contiene el texto a ser modificado
ARCHIVO_ENTRADA="./vault/init-vault-template.sh"
# El archivo de salida donde se guardará el resultado
ARCHIVO_SALIDA="./vault/init-vault.sh"

echo "GITHUB_TOKEN es: $GITHUB_TOKEN"
echo "SECRETS_URL es: $SECRETS_URL"
# Lee el valor actual de la variable de entorno GITHUB_TOKEN
TOKEN_ACTUAL="$GITHUB_TOKEN"
TOKEN_URL="$SECRETS_URL"

# Verifica si la variable GITHUB_TOKEN tiene contenido
if [ -z "$TOKEN_ACTUAL" ]; then
    echo "La variable GITHUB_TOKEN está vacía. Por favor, asegúrate de que está correctamente configurada."
    exit 1
fi

# Verifica si la variable SECRETS_URL tiene contenido
if [ -z "$TOKEN_URL" ]; then
    echo "La variable SECRETS_URL está vacía. Por favor, asegúrate de que está correctamente configurada."
    exit 1
fi

# Sustituye $GITHUB_TOKEN en el archivo de entrada con el valor actual de la variable de entorno
# y escribe el resultado al archivo de salida
sed "s#\$GITHUB_TOKEN#${TOKEN_ACTUAL}#g" "$ARCHIVO_ENTRADA" > "$ARCHIVO_SALIDA"

# Aplica la sustitución de la URL en el archivo ya modificado para evitar sobreescribir los cambios
sed -i "s#\$SECRETS_URL#${TOKEN_URL}#g" "$ARCHIVO_SALIDA"

echo "Archivo modificado creado: $ARCHIVO_SALIDA"

