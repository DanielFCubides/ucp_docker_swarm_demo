FROM node:20-alpine AS base
WORKDIR /app
COPY . /app

RUN npm install

COPY . .

WORKDIR /app

COPY . .
RUN npm run build
EXPOSE 3005
CMD ["npm","start"]
