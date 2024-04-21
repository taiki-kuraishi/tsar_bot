# Install git stage
FROM alpine:3.14 as git

RUN apk update && apk add --no-cache git

# Base stage
FROM python:3.11.8-alpine as base

WORKDIR /DiscordBot

COPY docker/discord-bot/requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# COPY discord-bot/src ./discord-bot/src

# Development stage
FROM base as development

COPY --from=git /usr/ /usr/

COPY .git /DiscordBot/.git

WORKDIR /DiscordBot

# COPY discord-bot/pyproject.toml .

# COPY .vscode/cspell.json .vscode/cspell.json

RUN pip install --no-cache-dir mypy ruff
