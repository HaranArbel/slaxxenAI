# Slaxxen API

This repository contains the API for the Slaxxen application. The API is built using FastAPI and is deployed using docker.

## run locally
Build the docker image:

`docker buildx build --platform linux/amd64  -t slaxxenai .`

Run the docker container:

`docker run --name slaxxenai -p 8000:8000 --env-file .env slaxxenai`
