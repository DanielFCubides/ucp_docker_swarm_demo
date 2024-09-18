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

## Local swarm
1. Create a swarm
```
docker swarm init
```

## Running the swarm
1. Build docker images
```
docker compose -f deploy-compose.yml build
```

2. Push docker images
```
docker compose push
```

3. Run the stack
```
docker stack deploy --compose-file deploy-compose.yml reporting 
```

4. Check the stack reporting is deployed
```
docker stack ls
```

5. Check the services running under the reporting stack
```
docker stack services reporting
docker stack ps reporting -f "desired-state=running"
```

## Update the swarm
1. Scale the application
```
docker service scale reporting_report_service=2 reporting_rest-proxy=2
```

2. Update a service without downtime
```
docker service update reporting_report_service --image=127.0.0.1:5000/report-service:0.0.1
```

3. Rollback the last change
```
docker service update reporting_report_service --rollback
```
