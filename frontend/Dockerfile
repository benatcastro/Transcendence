#FROM oven/bun:alpine AS builder -> TODO when creating the build release
FROM oven/bun:alpine  AS builder

WORKDIR /app


COPY . .
RUN bun install 
RUN bun run build

FROM oven/bun:alpine 

COPY --from=builder /app/build/. .
EXPOSE 3000/tcp
CMD [ "bun", "run", "index.js" ]
