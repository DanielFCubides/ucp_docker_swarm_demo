FROM node:20-alpine AS base
WORKDIR /app
COPY . /app

RUN npm install

COPY . .

WORKDIR /app

COPY . .
RUN npm run build

ENV NODE_ENV=production
EXPOSE 3005
ENV PORT=3005

ENV HOSTNAME="0.0.0.0"
CMD ["node", "server.js"]
