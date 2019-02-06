# docker-compose-pyflask-lbs-with-nginx
Use docker-compose to build a simple flask cluster with Nginx.

## Run
```shell
# Run and build.
docker-compose up -build
# Run
docker-compose up
# Rmove the volumes and containers.
docker-compose down -v
```
After completet the building you can open the browser to access 'http://localhost:18088/'.
You can see the node's name nad the PID number(JSON format).

## Env
You can set some env parameters in the `.env` file.