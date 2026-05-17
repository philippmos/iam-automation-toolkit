from app.graph.client import graph_get_all, graph_get

def list_ca_policies() -> list:
    return graph_get_all("/identity/conditionalAccess/policies")

def get_ca_policy(policy_id: str) -> dict:
    return graph_get(f"/identity/conditionalAccess/policies/{policy_id}")

def list_named_locations() -> list:
    return graph_get_all("/identity/conditionalAccess/namedLocations")