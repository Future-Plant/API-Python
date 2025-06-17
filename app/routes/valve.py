from fastapi import APIRouter
from pydantic import BaseModel
from app.services.mqtt_service import publish_valve

router = APIRouter(prefix="/valve", tags=["Valve"])

@router.post("/publica")
def send_command(command: str):
    return publish_valve(command)
