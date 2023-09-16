FROM node:20-alpine3.18

ENV NODE_ENV development

WORKDIR /app

COPY package*.json .
RUN npm install

EXPOSE 3000

CMD npm run start:dev
