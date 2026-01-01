from fastapi import FastAPI
from app.routes.health_routes import router as health_router
from app.routes.log_routes import router as log_router
from app.routes.aws_routes import router as aws_router

app = FastAPI(title="DevOps Internal API", version="1.0")


# ROOT ENDPOINT
@app.get("/")
def root():
    return {
        "message": "Welcome to DevOps FastAPI Project",
        "endpoints": {
            "health": "/health",
            "logs": "/logs",
            "aws": "/aws",
            "docs": "/docs"
        }
    }


app.include_router(health_router)
app.include_router(log_router)
app.include_router(aws_router)
