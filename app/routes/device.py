from fastapi import APIRouter
from app.services.mqtt_service import publish_valve

router = APIRouter(prefix="/valvula", tags=["Dispositivo"])

@router.post("/")
def ativa_valvula():
    return publish_valve("on")
