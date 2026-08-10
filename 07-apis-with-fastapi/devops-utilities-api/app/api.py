from fastapi import FastAPI
from routers import metrics, aws, logs

app = FastAPI(
    title="Internal DevOps Utilities API",
    description="Internal utilities API for system metrics, AWS usage, and log analysis.",
    version="1.2.0",
    docs_url="/docs",
    redoc_url="/redoc",
)


@app.get("/")
def hello():
    return {"message": "Hello Dosto, this is the DevOps Utilities API"}


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/version")
def version():
    return {"version": "1.2.0"}

app.include_router(metrics.router)
app.include_router(logs.router)
app.include_router(aws.router, prefix="/aws")