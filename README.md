# UP Docker swarm DEMO

## Run gRCP service

#### Make sure proto files exists
```shell
make proto-build
```

```shell
docker compose build report_service
docker compose up report_service -d
```


## Rest Proxy

#### Make sure proto files exists
```shell
make proto-build
```

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
