FROM node:18.19.0-alpine

WORKDIR /usr/src/app
COPY ./kitchen.yaml ./
COPY ./package*.json ./
COPY ./yarn.lock ./
RUN yarn add @stoplight/prism-cli
COPY . .

EXPOSE 3000
CMD [ "./node_modules/.bin/prism", "mock", "kitchen.yaml", "--port", "3000" ]