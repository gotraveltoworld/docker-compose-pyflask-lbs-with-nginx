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
After completet the building you can open the browser to access 'http://localhost:18088/hello_world/'.
You can see the node's name nad the PID number(JSON format).