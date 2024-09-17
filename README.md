# UP Docker swarm DEMO

## Run gRCP service

#### Make sure proto files exists
```shell
python -m grpc_tools.protoc -I. --python_out=./report_service --grpc_python_out=./report_service services.proto
```

```shell
docker compose build report_service
docker compose up report_service -d
```


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
