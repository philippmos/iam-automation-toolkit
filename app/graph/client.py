import requests
from app.auth.msal_client import get_access_token
from app.config import settings


def graph_get(endpoint: str, params: dict = None) -> dict:
    """Generischer GET gegen die Graph API."""
    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}"}
    url = f"{settings.graph_api_base}{endpoint}"

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    return response.json()


def graph_get_all(endpoint: str, params: dict = None) -> list:
    """Folgt automatisch @odata.nextLink für paginierte Ergebnisse."""
    results = []
    data = graph_get(endpoint, params)
    results.extend(data.get("value", []))

    while next_link := data.get("@odata.nextLink"):
        token = get_access_token()
        response = requests.get(next_link, headers={"Authorization": f"Bearer {token}"})
        response.raise_for_status()
        data = response.json()
        results.extend(data.get("value", []))

    return results