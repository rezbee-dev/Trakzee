# pull official base image
FROM python:3.11.2-slim-buster

# set working directory
WORKDIR /usr/app

# set environment variables
# Prevents python from writing pyc (compiled) files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents python from buffering stdout and stderr
# this ensures that the python output streams are sent straight to terminal w/o being buffered first
# for more info, see: https://stackoverflow.com/a/59812588
ENV PYTHONUNBUFFERED 1

# install system dependencies
# need this for docker-entrypoint.sh
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql \
  && apt-get clean

# add and install requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .

# make startup script executable
RUN chmod +x /usr/app/scripts/docker-entrypoint.sh

# Starting flask app w/o waiting for db startup
# CMD ["python", "src/main.py", "run", "-h", "0.0.0.0"]