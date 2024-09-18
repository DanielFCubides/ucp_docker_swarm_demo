from pydantic import BaseModel, Field


class PingResponse(BaseModel):
    timestamp: str = Field(..., description="Time when the request was made")
    version: str = Field(..., description="Service version")


class VisitReportResponse(BaseModel):
    local_visit_count: int
    visit_count: int
    host: str
