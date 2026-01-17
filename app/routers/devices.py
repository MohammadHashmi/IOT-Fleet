"""
Device-related API endpoints for IoT fleet management.
Handles device registration, heartbeats, and command operations.
"""
from fastapi import APIRouter
import uuid

# Create router for device endpoints
router = APIRouter()
key = 0

"""
Register a new IoT device in the fleet.

Returns:
    string: Registration confirmation message
    string: API Key 
    integer: Device ID
"""
@router.post("/register")
def register():
    global key
    new_id = uuid.uuid4()
    key += 1
    return {
    "Message":"Successful Register", 
    "API Key":f"{new_id}",
    "Device ID":f"{key}",
    }
    
@router.get("/register")
def getRegister():
    return {"Hello":"Sigma"}
#@router.post("/{id}/heartbeat")