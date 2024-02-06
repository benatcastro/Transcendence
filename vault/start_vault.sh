#!/bin/bash

# El archivo de entrada que contiene el texto a ser modificado
ARCHIVO_ENTRADA="init-vault-template.sh"
# El archivo de salida donde se guardará el resultado
ARCHIVO_SALIDA="init-vault.sh"

echo "GITHUB_TOKEN es: $GITHUB_TOKEN"
# Lee el valor actual de la variable de entorno GITHUB_TOKEN
TOKEN_ACTUAL="$GITHUB_TOKEN"

# Verifica si la variable GITHUB_TOKEN tiene contenido
if [ -z "$TOKEN_ACTUAL" ]; then
    echo "La variable GITHUB_TOKEN está vacía. Por favor, asegúrate de que está correctamente configurada."
    exit 1
fi

# Sustituye $GITHUB_TOKEN en el archivo de entrada con el valor actual de la variable de entorno
# y escribe el resultado al archivo de salida
sed "s/\$GITHUB_TOKEN/${TOKEN_ACTUAL}/g" "$ARCHIVO_ENTRADA" > "$ARCHIVO_SALIDA"

echo "Archivo modificado creado: $ARCHIVO_SALIDA"

