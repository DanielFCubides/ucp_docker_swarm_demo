from pydantic import BaseModel

class PingResponse(BaseModel):
    timestamp: str
    version: str

class VisitReportResponse(BaseModel):
    local_visit_count: int
    visit_count: int
    host: str
