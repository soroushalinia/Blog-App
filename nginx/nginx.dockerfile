FROM nginx
RUN rm -f /etc/nginx/conf.d/default.conf
RUN rm -f /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx