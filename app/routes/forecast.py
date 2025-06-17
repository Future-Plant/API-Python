from fastapi import APIRouter
from app.services.ia_service import forecast_moisture

router = APIRouter(prefix="/forecast", tags=["Previsão"])

@router.post("/")
def prever():
    return forecast_moisture()
