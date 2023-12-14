#FROM oven/bun:alpine AS builder -> TODO when creating the build release

FROM oven/bun:1.0.6-alpine

WORKDIR /app

COPY package*.json ./

RUN bun install && bun install @threlte/core three @types/three @threlte/extras @threlte/rapier @dimforge/rapier3d-compat postprocessing mdbsvelte

EXPOSE 5173

CMD bun --bun run dev -- --host 0.0.0.0
