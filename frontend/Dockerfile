FROM node:16

WORKDIR /app

COPY package.json package-lock.json ./
RUN rm -rf ./node_modules
RUN npm install

ENV NODE_TLS_REJECT_UNAUTHORIZED=0

COPY . ./

ENTRYPOINT [ "node", "webhook.js"]
