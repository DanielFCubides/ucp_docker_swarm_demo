import os

from fastapi import FastAPI, APIRouter
import grpc

from lib import response_model
import services_pb2
import services_pb2_grpc

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
    return stub.HealthCheck(services_pb2.Request())


@router.get("/report/visits/", tags=["reports"])
async def visit_report() -> response_model.VisitReportResponse:
    return stub.GetVisitCount(services_pb2.Request())


app.include_router(router)
