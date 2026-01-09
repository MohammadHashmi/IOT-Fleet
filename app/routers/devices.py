from fastapi import APIRouter
router = APIRouter()

@router.post("/register")
def register():
    return {"Message":"Successful Register"}
@router.post("/{id}/heartbeat")