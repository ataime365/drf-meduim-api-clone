FROM nginx:1.23.3-alpine

# Remove the normal default conf file and put our own default conf file there
RUN rm /etc/nginx/conf.d/default.conf

COPY ./default.conf /etc/nginx/conf.d/default.conf

