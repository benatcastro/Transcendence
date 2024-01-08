#FROM oven/bun:alpine AS builder -> TODO when creating the build release

FROM oven/bun:alpine

WORKDIR /app

COPY package.json ./

RUN bun install

EXPOSE 5173

CMD bun --bun run dev -- --host 0.0.0.0
