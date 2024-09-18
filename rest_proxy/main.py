import logging

from fastapi import FastAPI, APIRouter
import grpc

from lib import response_model
from lib.grpc_connection import GRPCClient

logger = logging.getLogger(__name__)

tags_metadata = [
    {
        "name": "ping",
        "description": "Used to determine the service status.",
    },
    {
        "name": "reports",
        "description": "Obtain information from Telesign customers.",
    },
]

server = os.environ.get('GRPC_SERVER', 'localhost:50051')
channel = grpc.insecure_channel(server)
stub = services_pb2_grpc.VisitServiceStub(channel)

app = FastAPI(openapi_tags=tags_metadata)
router = APIRouter()


@router.get("/ping/", tags=["ping"])
async def ping() -> response_model.PingResponse:
    client = GRPCClient(hostname="report_service", port="50051")
    response = client.execute(
        rpc_method_name="HealthCheck", protobuf_msg_name="Request", metadata=""
    )
    return response


@router.get("/report/visits/", tags=["reports"])
async def visit_report() -> response_model.VisitReportResponse:
    client = GRPCClient(hostname="report_service", port="50051")
    response = client.execute(
        rpc_method_name="GetVisitCount", protobuf_msg_name="Request", metadata=""
    )
    return response


app.include_router(router)
