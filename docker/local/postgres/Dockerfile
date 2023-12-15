FROM postgres:15-bullseye

#copy from local machine to docker
COPY ./docker/local/postgres/maintenance /usr/local/bin/maintenance

RUN chmod +x /usr/local/bin/maintenance/*

# Move the maintenance 'files' to the bin folder and remove the maintenance folder
RUN mv /usr/local/bin/maintenance/* /usr/local/bin && rmdir /usr/local/bin/maintenance


