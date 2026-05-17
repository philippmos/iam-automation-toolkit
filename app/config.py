from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    tenant_id: str
    client_id: str
    client_secret: str
    graph_api_base: str = "https://graph.microsoft.com/v1.0"

    class Config:
        env_file = ".env"

settings = Settings()