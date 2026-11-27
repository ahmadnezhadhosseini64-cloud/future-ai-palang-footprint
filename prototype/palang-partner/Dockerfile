FROM node:22-alpine
WORKDIR /app
COPY package.json ./
RUN npm install --omit=dev --ignore-scripts --no-audit --no-fund --package-lock=false
COPY server.mjs policy.mjs ./
ENV PORT=8080
EXPOSE 8080
CMD ["npm", "start"]
