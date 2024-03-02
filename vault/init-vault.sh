#!/bin/bash



# Inicia el servidor de Vault en modo de desarrollo
vault server -dev &

# Espera a que Vault esté listo
echo "Esperando a que Vault esté listo..."
until vault status; do
    echo "Vault no está listo. Esperando..."
    sleep 5
done
echo "Vault está listo."



# Configura las variables de entorno para Vault
export VAULT_ADDR='http://127.0.0.1:8200'
export VAULT_TOKEN='myroot'

SECRETS_URL="https://raw.githubusercontent.com/adelcor/secret/main/secrets.txt"
GITHUB_TOKEN="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"

# Agrega secretos desde un archivo de texto (solo para corrección)
apk add --no-cache curl
curl -H "Authorization: token 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" -o secrets.txt  "$SECRETS_URL"
curl -H "Authorization: token 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" -o localhost.key  "https://raw.githubusercontent.com/adelcor/secret/main/localhost.key"
curl -H "Authorization: token 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" -o localhost.csr  "https://raw.githubusercontent.com/adelcor/secret/main/localhost.csr"
curl -H "Authorization: token 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" -o localhost.crt  "https://raw.githubusercontent.com/adelcor/secret/main/localhost.crt"

while IFS='=' read -r key value; do
    vault kv put secret/myapp/$key value="$value"
done < secrets.txt

vault kv put secret/mykey key=@localhost.key
vault kv put secret/mycsr csr=@localhost.csr
vault kv put secret/mycrt crt=@localhost.crt

wait
