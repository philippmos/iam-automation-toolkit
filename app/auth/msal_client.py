import msal
from app.config import settings

_app = msal.ConfidentialClientApplication(
    client_id=settings.client_id,
    client_credential=settings.client_secret,
    authority=f"https://login.microsoftonline.com/{settings.tenant_id}",
)

SCOPES = ["https://graph.microsoft.com/.default"]

def get_access_token() -> str:
    result = _app.acquire_token_silent(SCOPES, account=None)
    if not result:
        result = _app.acquire_token_for_client(scopes=SCOPES)
    if "access_token" not in result:
        raise RuntimeError(f"Token-Fehler: {result.get('error_description')}")
    return result["access_token"]