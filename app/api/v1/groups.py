from fastapi import APIRouter, HTTPException
from app.graph import groups as graph_groups

router = APIRouter()

@router.get("/")
def get_all_groups(top: int = 100):
    try:
        return {"groups": graph_groups.list_groups(top=top)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{group_id}/members")
def get_group_members(group_id: str):
    try:
        return {"members": graph_groups.get_group_members(group_id)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))