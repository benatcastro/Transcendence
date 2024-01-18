FROM nginx:stable-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
COPY server.crt /etc/nginx/server.crt
COPY server.key /etc/nginx/server.key