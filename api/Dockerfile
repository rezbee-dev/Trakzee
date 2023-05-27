# pull official base image
FROM python:3.11.2-slim-buster

# set working directory
WORKDIR /usr/app/api

# set environment variables
# Prevents python from writing pyc (compiled) files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents python from buffering stdout and stderr
# this ensures that the python output streams are sent straight to terminal w/o being buffered first
# for more info, see: https://stackoverflow.com/a/59812588
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
COPY ./requirements-dev.txt .
RUN pip install -r requirements-dev.txt

# add app
COPY . .

# make startup script executable
# RUN chmod +x /usr/app/backend/docker-entrypoint.sh

# Starting flask app w/o waiting for db startup
CMD ["python", "src/main.py", "run", "-h", "0.0.0.0"]