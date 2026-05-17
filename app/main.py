from fastapi import FastAPI
from app.api.v1 import users, groups, policies

app = FastAPI(
    title="IAM Automation Toolkit",
    description="Graph API Automation for Microsoft Entra ID",
    version="0.1.0"
)

app.include_router(users.router, prefix="/api/v1/users", tags=["Users"])
app.include_router(groups.router, prefix="/api/v1/groups", tags=["Groups"])
app.include_router(policies.router, prefix="/api/v1/policies", tags=["Policies"])

@app.get("/health")
def health_check():
    return {"status": "ok"}