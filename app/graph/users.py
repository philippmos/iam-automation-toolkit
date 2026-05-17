from app.graph.client import graph_get, graph_get_all

def list_users(top: int = 100) -> list:
    return graph_get_all("/users", params={
        "$top": top,
        "$select": "id,displayName,userPrincipalName,accountEnabled,createdDateTime"
    })

def get_user(user_id: str) -> dict:
    return graph_get(f"/users/{user_id}")

def get_user_groups(user_id: str) -> list:
    return graph_get_all(f"/users/{user_id}/memberOf")