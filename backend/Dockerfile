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

# add and install requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add app
COPY . .

# run server
CMD ["python", "src/main.py", "run", "-h", "0.0.0.0"]