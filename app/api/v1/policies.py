from fastapi import APIRouter, HTTPException
from app.graph import conditional_access as graph_ca

router = APIRouter()

@router.get("/conditional-access")
def get_ca_policies():
    try:
        return {"policies": graph_ca.list_ca_policies()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))