# UP Docker swarm DEMO

## Rest Proxy
### Building the image
```
docker-compose build rest-proxy
```
### Running locally
```
docker compose up rest-proxy -d
```

### Build the production image
```
docker build -f rest_proxy/Dockerfile . -t ts/reporting/rest-proxy:development --target=production
```

# gRPC Service