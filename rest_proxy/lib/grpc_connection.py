import grpc
from typing import Sequence
from google.protobuf import json_format

from proto.services_pb2_grpc import VisitServiceStub
from proto import services_pb2

class GRPCClient:
    def __init__(self, hostname: str, port: str):
        self.channel = grpc.insecure_channel(f'{hostname}:{port}')
        self.stub = VisitServiceStub(self.channel)

    def _get_request(self, protobuf_msg_name, **kwargs):
        msg_type = getattr(services_pb2, protobuf_msg_name)
        try:
            request = msg_type(**kwargs)
        except Exception as e:
            raise ValidationError('Invalid Request: gRPC request failed')

        return request


    def execute(
            self,
            rpc_method_name: str,
            protobuf_msg_name: str,
            metadata: Sequence[tuple] = (),
            **kwargs,
    ):
        request_msg = self._get_request(protobuf_msg_name, **kwargs)
        rpc_method = getattr(self.stub, rpc_method_name)

        print(f'Calling RPC "{rpc_method_name}" at {str(self.channel._channel.target())}')

        try:
            response = rpc_method(request_msg, metadata=metadata)
        except grpc.RpcError as e:
            print(f'grpc.RpcError: code={e.code()}, details={e.details()}')
            raise
        except Exception as e:
            print(f'Unexpected Error: {e}')
            raise

        return json_format.MessageToDict(
            message=response,
            preserving_proto_field_name=True,
        )
