FROM node:19

# set working directory
WORKDIR /usr/app/client

# add `/usr/src/app/node_modules/.bin` to $PATH
# see: https://stackoverflow.com/a/65407744
ENV PATH /usr/app/client/node_modules/.bin:$PATH

# install and cache app dependencies
COPY package.json .
COPY package-lock.json .
RUN npm ci

# start app
CMD ["npm", "run", "dev"]