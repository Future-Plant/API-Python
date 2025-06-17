from fastapi import APIRouter
from app.services.mqtt_service import publish_valve

router = APIRouter(prefix="/valve", tags=["Valve"])

@router.post("/")
def send_command(command: str):
    return publish_valve(command)
