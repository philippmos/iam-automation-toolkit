from fastapi import APIRouter, HTTPException
from app.graph import users as graph_users

router = APIRouter()

@router.get("/")
def get_all_users(top: int = 100):
    try:
        return {"users": graph_users.list_users(top=top), "count": top}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{user_id}")
def get_user(user_id: str):
    try:
        return graph_users.get_user(user_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))

@router.get("/{user_id}/groups")
def get_user_groups(user_id: str):
    return {"groups": graph_users.get_user_groups(user_id)}