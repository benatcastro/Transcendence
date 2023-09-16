FROM node:20-alpine3.18

ENV NODE_ENV development

WORKDIR /app

COPY package*.json .
RUN npm install

EXPOSE 5173

CMD npm run dev -- --host 0.0.0.0
