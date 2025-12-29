from fastapi import APIRouter, HTTPException
from services.metrics_service import get_system_metrics

router = APIRouter()

@router.get("/metrics",status_code=200)
def get_metrics():

    try:
        metrics = get_system_metrics()
        return metrics
    except:
        raise HTTPException(
            status_code=500,
            detail="Internal Server Error"
        )
