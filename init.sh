#!/bin/bash
SECRETS_URL="https://raw.githubusercontent.com/adelcor/secret/main/secrets.txt"
GITHUB_TOKEN="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"



# Define una función para esperar la existencia de un archivo con tiempo máximo de espera
espera_archivo() {
  local archivo=$1
  local espera_maxima=$2
  local tiempo_espera=0

  echo "Esperando a que se genere el archivo $archivo..."
  while [ ! -f "$archivo" ]; do
    if [ "$tiempo_espera" -ge "$espera_maxima" ]; then
      echo "Tiempo máximo de espera alcanzado para $archivo. Saliendo..."
      exit 1
    fi

    echo "Esperando por $archivo..."
    sleep 5
    ((tiempo_espera+=5))
  done
  echo "Archivo $archivo encontrado."
}

# Cambia al directorio donde se encuentra vault.yml si es necesario
# cd /path/to/your/vault/directory

# Descarga los archivos de entorno
curl -H "Authorization: token $GITHUB_TOKEN" -o vault.env  "https://raw.githubusercontent.com/adelcor/secret/main/vault.env"
if [ $? -ne 0 ]; then
  echo "Error descargando vault.env"
  exit 1
fi

curl -H "Authorization: token $GITHUB_TOKEN" -o consul.env  "https://raw.githubusercontent.com/adelcor/secret/main/consul.env"
if [ $? -ne 0 ]; then
  echo "Error descargando consul.env"
  exit 1
fi

echo "Recuperando token del Host..."
./vault/start_vault.sh
if [ $? -ne 0 ]; then
  echo "Error iniciando Vault"
  exit 1
fi

# Espera a que se genere el archivo de inicio de vault
espera_archivo "./vault/init-vault.sh" 60

cat << "EOF"

 _______   _______ _________________ _____ _   _ _____   _____ _____  ___  ___  ___  
/  __ \ \ / / ___ \  ___| ___ \ ___ \  _  | \ | |  __ \ |_   _|  ___|/ _ \ |  \/  |_ 
| /  \/\ V /| |_/ / |__ | |_/ / |_/ / | | |  \| | |  \/   | | | |__ / /_\ \| .  . (_)
| |     \ / | ___ \  __||    /|  __/| | | | . ` | | __    | | |  __||  _  || |\/| |  
| \__/\ | | | |_/ / |___| |\ \| |   \ \_/ / |\  | |_\ \   | | | |___| | | || |  | |_ 
 \____/ \_/ \____/\____/\_| \_\_|    \___/\_| \_/\____/   \_/ \____/\_| |_/\_|  |_(_)
                                                                                     
                                                                                     
             _                                                                       
            | |                                                                      
  __ _  __ _| |_   ____ _ _ __ ___ ____                                              
 / _` |/ _` | \ \ / / _` | '__/ _ \_  /                                              
| (_| | (_| | |\ V / (_| | | |  __// /                                               
 \__,_|\__,_|_| \_/ \__,_|_|  \___/___|                                              
                                                                                     
                                                                                     
      _               _                                                              
     | |             | |                                                             
  ___| |__  _   _ ___| |_ __ _ _ __ ___   __ _                                       
 / __| '_ \| | | / __| __/ _` | '_ ` _ \ / _` |                                      
| (__| |_) | |_| \__ \ || (_| | | | | | | (_| |                                      
 \___|_.__/ \__,_|___/\__\__,_|_| |_| |_|\__,_|                                      
                                                                                     
                                                                                     
       _                                                                             
      | |                                                                            
  __ _| |__   ___ _ __ _ __ ___ _ __ ___                                             
 / _` | '_ \ / _ \ '__| '__/ _ \ '__/ _ \                                            
| (_| | | | |  __/ |  | | |  __/ | | (_) |                                           
 \__,_|_| |_|\___|_|  |_|  \___|_|  \___/                                            
                                                                                     
                                                                                     
 _                        _                                                          
| |                      | |                                                         
| |__   ___  ___ __ _ ___| |_ _ __ ___                                               
| '_ \ / _ \/ __/ _` / __| __| '__/ _ \                                              
| |_) |  __/ (_| (_| \__ \ |_| | | (_) |                                             
|_.__/ \___|\___\__,_|___/\__|_|  \___/                                              
                                                                                     
                                                                                     
           _      _                                                                  
          | |    | |                                                                 
  __ _  __| | ___| |______ ___ ___  _ __                                             
 / _` |/ _` |/ _ \ |______/ __/ _ \| '__|                                            
| (_| | (_| |  __/ |     | (_| (_) | |                                               
 \__,_|\__,_|\___|_|      \___\___/|_|                                               
                                                                                     	   
EOF
echo "Generando Secretos..."
docker compose -f vault.yml build
docker compose -f vault.yml up -d
if [ $? -ne 0 ]; then
  echo "Error ejecutando Docker Compose"
  exit 1
fi

# Espera a que se genere el archivo .env
espera_archivo "./env-output/.env" 60

# Mueve y copia los archivos necesarios
mv ./env-output/.env ./

# Espera a que se generen los archivos en los directorios correspondientes
espera_archivo "./.env" 60

# Ejecuta el script start_alerts.sh ubicado en /alertmanager
echo "Ejecutando el script start_alerts.sh para configurar alertas..."
./alertmanager/start_alerts.sh
if [ $? -ne 0 ]; then
  echo "Error ejecutando start_alerts.sh"
  exit 1
fi

# Espera a que se genere el archivo de configuración de AlertManager
espera_archivo "./alertmanager/config_mod.yml" 60
cat << "EOF"
 _____ _____ ______ ___________ _____ ___________    _    _ _____ _____ _   _    _     _____  _   _ _____  
/  ___/  __ \| ___ \_   _| ___ \_   _|  ___|  _  \  | |  | |_   _|_   _| | | |  | |   |  _  || | | |  ___| 
\ `--.| /  \/| |_/ / | | | |_/ / | | | |__ | | | |  | |  | | | |   | | | |_| |  | |   | | | || | | | |__   
 `--. \ |    |    /  | | |  __/  | | |  __|| | | |  | |/\| | | |   | | |  _  |  | |   | | | || | | |  __|  
/\__/ / \__/\| |\ \ _| |_| |     | | | |___| |/ /   \  /\  /_| |_  | | | | | |  | |___\ \_/ /\ \_/ / |___  
\____/ \____/\_| \_|\___/\_|     \_/ \____/|___/     \/  \/ \___/  \_/ \_| |_/  \_____/\___/  \___/\____/  
                                                                                                           
                                                                                                           
________   __    ___ ______ _____ _          _____ ___________                                             
| ___ \ \ / /   / _ \|  _  \  ___| |        /  __ \  _  | ___ \                                            
| |_/ /\ V /   / /_\ \ | | | |__ | |  ______| /  \/ | | | |_/ /                                            
| ___ \ \ /    |  _  | | | |  __|| | |______| |   | | | |    /                                             
| |_/ / | |    | | | | |/ /| |___| |____    | \__/\ \_/ / |\ \                                             
\____/  \_/    \_| |_/___/ \____/\_____/     \____/\___/\_| \_|  

EOF

echo "Ejecutando Secuencia de inicio de Cyberpong..."
make
if [ $? -ne 0 ]; then
  echo "Error ejecutando make"
  exit 1
fi

