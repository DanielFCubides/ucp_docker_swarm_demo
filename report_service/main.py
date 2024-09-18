import os
import grpc
from concurrent import futures
import socket
import threading
from datetime import datetime

import services_pb2
import services_pb2_grpc

from redis_client import get_redis_client

class VisitServiceServicer(services_pb2_grpc.VisitServiceServicer):
    def __init__(self):
        self.visit_count = 0
        self.host = os.environ.get('NAME', 'localhost')
        self.lock = threading.Lock()
        self.version = os.environ.get('VERSION', '0.0.1')
        self.redis_client = get_redis_client()

    def GetVisitCount(self, request, context):
        with self.lock:
            self.visit_count += 1

        general_count = int(self.redis_client.incr('visit_count'))
        response = services_pb2.VisitResponse(
            visit_count=general_count,
            local_visit_count=self.visit_count,
            host=self.host
        )
        return response

    def HealthCheck(self, request, context):
        current_timestamp = datetime.utcnow().isoformat()
        return services_pb2.HealthCheckResponse(
            version=self.version,
            timestamp=current_timestamp
        )

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_VisitServiceServicer_to_server(VisitServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print(f"Server started on host: {socket.gethostname()}")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
