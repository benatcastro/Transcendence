#!/bin/bash

echo "Esperando a que elastic esté listo..."
until curl -s localhost:9200/_cat/health | grep -q 'green\|yellow'; do
    echo "elastic no está listo. Esperando..."
    sleep 5
done
echo "Elasticsearch está listo."

# Cambiar la contraseña del usuario kibana_system.
curl -X POST "elasticsearch:9200/_security/user/kibana_system/_password" -H 'Content-Type: application/json' -d'
{
  "password" : "123456"
}
' -u elastic:123456

