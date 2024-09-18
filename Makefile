proto-build:
	python -m grpc_tools.protoc -I. --python_out=./report_service --grpc_python_out=./report_service services.proto
	python -m grpc_tools.protoc -I. --python_out=./rest_proxy --grpc_python_out=./rest_proxy services.proto