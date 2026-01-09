"""
Main FastAPI application entry point for IoT Fleet Management backend.
"""
from fastapi import FastAPI
from routers import devices

# Initialize FastAPI application
app = FastAPI()
@app.get("/")
def root():
    return {"Hello":"World"}

# Handle device-related routes under /devices prefix
app.include_router(devices.router, prefix="/devices", tags=["devices"])