# ucp_docker_swarm_demo

### Run gRCP service

#### Make sure proto files exists with
```shell
python -m grpc_tools.protoc -I. --python_out=./report_service --grpc_python_out=./report_service services.proto
```

```shell
docker compose build
docker compose up
```
