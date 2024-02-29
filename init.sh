

# Cambia al directorio donde se encuentra vault.yml si es necesario
# cd /path/to/your/vault/directory

curl -H "Authorization: token $GITHUB_TOKEN" -o vault.env  "https://raw.githubusercontent.com/adelcor/secret/main/vault.env"

curl -H "Authorization: token $GITHUB_TOKEN" -o consul.env  "https://raw.githubusercontent.com/adelcor/secret/main/consul.env"

echo "recuperando token del Host..."

./vault/start_vault.sh

# Espera a que se genere el archivo de inicio de vault
echo "Esperando a que se genere el archivo ./vault/init-vault.sh"
while [ ! -f "./vault/init-vault.sh" ]; do
    echo "Esperando a init-vault.sh"
    sleep 5
done
echo "Archivo ./vault/init_vault.sh encontrado."

echo "Generando Secretos..."
docker compose -f vault.yml build
docker compose -f vault.yml up -d

# Espera a que se cree el archivo .env
echo "Esperando a que se genere el archivo .env..."
while [ ! -f "./env-output/.env" ]; do
  sleep 5
done

echo "Archivo .env encontrado."

mv ./env-output/.env ./
cp ./env-output/localhost.key ./django
mv ./env-output/localhost.key ./nginx

# Espera a que se genere el archivo .env en la raíz
echo "Esperando a que se genere el archivo .env en el directorio actual..."
while [ ! -f "./.env" ]; do
    echo "Esperando por .env..."
    sleep 5
done
echo "Archivo .env encontrado."

# Espera a que localhost.key esté disponible en ./django
echo "Esperando a que localhost.key esté disponible en ./django..."
while [ ! -f "./django/localhost.key" ]; do
    echo "Esperando por localhost.key en ./django..."
    sleep 5
done
echo "Archivo localhost.key encontrado en ./django."

# Espera a que localhost.key esté disponible en ./nginx
echo "Esperando a que localhost.key esté disponible en ./nginx..."
while [ ! -f "./nginx/localhost.key" ]; do
    echo "Esperando por localhost.key en ./nginx..."
    sleep 5
done
echo "Archivo localhost.key encontrado en ./nginx."

# Ejecuta el script start_alerts.sh ubicado en /alertmanager
echo "Ejecutando el script start_alerts.sh para configurar alertas..."
./alertmanager/start_alerts.sh

# Espera a que se genere el archivo de configuración de AlertManager
echo "Esperando a generar archivo de configuración de AlertManager de manera segura..."
while [ ! -f "./alertmanager/config_mod.yml" ]; do
    echo "Esperando por config_mod.yml..."
    sleep 5
done
echo "Archivo /alertmanager/config_mod.yml encontrado. Continuando con la secuencia de inicio."

echo "Ejecutando Secuencia de inicio de Cyberpong..."
make

