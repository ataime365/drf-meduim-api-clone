FROM postgres:15-bullseye

#copy from local machine to docker
COPY ./docker/production/postgres/maintenance /usr/production/bin/maintenance

RUN chmod +x /usr/production/bin/maintenance/*

# Move the maintenance 'files' to the bin folder and remove the maintenance folder
RUN mv /usr/production/bin/maintenance/* /usr/production/bin && rmdir /usr/production/bin/maintenance


