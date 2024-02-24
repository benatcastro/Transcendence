

# Cambia al directorio donde se encuentra vault.yml si es necesario
# cd /path/to/your/vault/directory

curl -H "Authorization: token $GITHUB_TOKEN" -o vault.env  "https://raw.githubusercontent.com/adelcor/secret/main/vault.env"

curl -H "Authorization: token $GITHUB_TOKEN" -o consul.env  "https://raw.githubusercontent.com/adelcor/secret/main/consul.env"

echo "recuperando token del Host..."

./vault/start_vault.sh

echo "Generando Secretos..."
docker compose -f vault.yml build
docker compose -f vault.yml up -d

# Espera a que se cree el archivo .env
echo "Esperando a que se genere el archivo .env..."
while [ ! -f ".env" ]; do
  sleep 5
done

echo "Archivo .env encontrado."

# Ejecuta el script start_alerts.sh ubicado en /alertmanager
echo "Ejecutando el script start_alerts.sh para configurar alertas..."
./alertmanager/start_alerts.sh

# Espera a que se genere el archivo /alertmanager/config_mod.yml
echo "Esperando a generar archivo de configuracion de AlertManager de manera segura..."
while [ ! -f "./alertmanager/config_mod.yml" ]; do
  sleep 5
done

echo "Archivo /alertmanager/config_mod.yml encontrado. Continuando con la secuencia de inicio."

echo "Ejecutando Secuencia de inicio de Cyberpong..."
make

