from pydantic import BaseModel

class PingResponse(BaseModel):
    timestamp: int
    version: int

class VisitReportResponse(BaseModel):
    local_visits: int
    shared_visits: int