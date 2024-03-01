FROM owasp/modsecurity-crs:nginx-alpine

RUN rm /etc/nginx/conf.d/default.conf
COPY nginx.conf /etc/nginx/conf.d
COPY localhost.pem /etc/nginx/localhost.pem
COPY localhostkey.pem /etc/nginx/localhostkey.pem
