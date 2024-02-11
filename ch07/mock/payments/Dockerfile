FROM node:18.19.0-alpine

WORKDIR /usr/src/app
COPY ./payments.yaml ./
COPY ./package*.json ./
COPY ./yarn.lock ./
RUN yarn add @stoplight/prism-cli
COPY . .

EXPOSE 3001
CMD [ "./node_modules/.bin/prism", "mock", "payments.yaml", "--port", "3001" ]
