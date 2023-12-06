#FROM oven/bun:alpine AS builder -> TODO when creating the build release

FROM oven/bun:alpine

WORKDIR /app

COPY package*.json ./

<<<<<<< HEAD
RUN bun install && bun install @threlte/core three @types/three @threlte/extras @threlte/rapier @dimforge/rapier3d-compat three postprocessing
=======
RUN bun install && bun install bootstrap @threlte/core three @types/three @threlte/extras @threlte/rapier @dimforge/rapier3d-compat
>>>>>>> main-v2

EXPOSE 5173

CMD bun --bun run dev -- --host 0.0.0.0
