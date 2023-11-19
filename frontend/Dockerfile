#FROM oven/bun:alpine AS builder -> TODO when creating the build release

FROM oven/bun:alpine

WORKDIR /app

COPY package*.json ./

RUN bun install &&\
	bun install @threlte/core three @types/three &&\
	bun install @threlte/extras &&\
	bun install @threlte/rapier @dimforge/rapier3d-compat
#	bunx @threlte/gltf@latest /path/to/Model.glb &&\


EXPOSE 5173

CMD bun --bun run dev -- --host 0.0.0.0
