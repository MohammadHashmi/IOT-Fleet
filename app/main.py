from fastapi import FastAPI
from app.routers import devices

app = FastAPI()
@app.get("/")
def root():
    return {"Hello":"World"}

app.include_router(devices.router, prefix="/devices", tags=["devices"])