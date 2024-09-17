import time

from fastapi import FastAPI, APIRouter

from lib import response_model

LOCAL_VISITS = 0

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


@router.get("/ping/", tags=["ping"])
async def ping() -> response_model.PingResponse:
    version = 1
    timestamp = int(time.time())
    return {"version": version, "timestamp": timestamp}


@router.get("/report/visits/", tags=["reports"])
async def visit_report() -> response_model.VisitReportResponse:
    global LOCAL_VISITS
    LOCAL_VISITS += 1
    shared = 1
    return {"local_visits": LOCAL_VISITS, "shared_visits": shared}


app.include_router(router)
