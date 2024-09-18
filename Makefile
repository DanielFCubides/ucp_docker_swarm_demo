deps:
	pip install -r report_service/requirements.txt
	pip install -r rest_proxy/requirements.txt

proto-build:
	python -m grpc_tools.protoc -I. --python_out=./ --grpc_python_out=./ proto/services.proto

run-server:
	export PYTHONPATH=$(pwd):$PYTHONPATH
	python report_service/main.py

run-client:
	export PYTHONPATH=$(pwd):$PYTHONPATH
	fastapi dev rest_proxy/main.py