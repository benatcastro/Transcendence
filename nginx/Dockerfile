FROM nginx:stable-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
COPY localhost.csr /etc/nginx/localhost.csr
COPY localhost.crt /etc/nginx/localhost.crt
COPY localhost.key /etc/nginx/localhost.key
