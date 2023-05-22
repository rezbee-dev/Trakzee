# pull official base image
FROM postgres:15

# run create.sql on init
# extending the official postgres image by adding create.sql to the docker-entrypoint-initdb.d directory in the container so that create.sql will execute on init
COPY ./create.sql /docker-entrypoint-initdb.d