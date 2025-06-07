FROM node:20-slim as builder

WORKDIR /opt/ui
COPY package.json package-lock.json ./
RUN npm install
RUN npm install -g serve

COPY . /opt/ui
RUN npm run build

EXPOSE 3000
CMD [ "npm", "start"]