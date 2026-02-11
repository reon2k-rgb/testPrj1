from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="PRJ-Renewal Internal API", version="0.1.0")

class ScrapeRequest(BaseModel):
    project: str
    url: str
    priority: Optional[str] = "normal"

@app.post("/api/scrape", status_code=202)
def enqueue_scrape(req: ScrapeRequest):
    return {"job_id": "stub-123e4567-e89b-12d3-a456-426614174000"}

@app.get("/api/status/{job_id}")
def get_status(job_id: str):
    return {"job_id": job_id, "status": "pending", "result": None}

class GenerateRequest(BaseModel):
    page_id: int
    prompt: str
    options: Optional[dict] = None

@app.post("/api/generate")
def generate(req: GenerateRequest):
    return {"artifact_id": 1, "status": "queued"}

@app.get("/api/artifacts/{artifact_id}")
def get_artifact(artifact_id: int):
    return {"artifact_id": artifact_id, "path": f"/artifacts/{artifact_id}"}
