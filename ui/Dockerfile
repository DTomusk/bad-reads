FROM node:20-slim as builder
ENV PNPM_HOME="/pnpm"
ENV PATH="$PNPM_HOME:$PATH"
RUN corepack enable pnpm 
RUN corepack prepare pnpm@latest --activate

WORKDIR /opt/ui
COPY pnpm-lock.yaml /opt/ui
RUN pnpm fetch

COPY . /opt/ui
RUN pnpm run build

EXPOSE 3000
CMD [ "pnpm", "start"]