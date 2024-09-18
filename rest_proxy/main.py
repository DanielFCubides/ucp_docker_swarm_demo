import logging
import os

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

app = FastAPI(openapi_tags=tags_metadata)
router = APIRouter()
client = GRPCClient(hostname="report_service", port="50051")


@router.get("/ping/", tags=["ping"])
async def ping() -> response_model.PingResponse:
    response = client.execute(
        rpc_method_name="HealthCheck", protobuf_msg_name="Request", metadata=""
    )
    return response


@router.get("/report/visits/", tags=["reports"])
async def visit_report() -> response_model.VisitReportResponse:
    response = client.execute(
        rpc_method_name="GetVisitCount", protobuf_msg_name="Request", metadata=""
    )
    return response


app.include_router(router)
