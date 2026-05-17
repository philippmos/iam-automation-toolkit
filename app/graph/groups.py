from app.graph.client import graph_get_all

def list_groups(top: int = 100) -> list:
    return graph_get_all("/groups", params={
        "$top": top,
        "$select": "id,displayName,description,groupTypes,membershipRule"
    })

def get_group_members(group_id: str) -> list:
    return graph_get_all(f"/groups/{group_id}/members")