FROM node:20

WORKDIR /usr/src/app

COPY src/package*.json ./

RUN npm install

COPY src .

CMD ["node", "server.js"]
