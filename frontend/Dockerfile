# stage 1: build
from oven/bun:canary-debian
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /app

COPY package*.json ./

RUN <<EOF
bun install
bun install @threlte/core three @types/three @threlte/extras @threlte/rapier @dimforge/rapier3d-compat postprocessing mdbsvelte
apt-get update -y
apt-get upgrade -y
apt-get install --no-install-recommends net-tools dnsutils -y
EOF
EXPOSE 5173

CMD bun --bun run dev -- --host 0.0.0.0

















