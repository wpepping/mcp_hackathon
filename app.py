from fastapi import FastAPI
from router import main_router

def configure_app() -> FastAPI:
    app = FastAPI(title="mcp_hackathon", docs_url=None, redoc_url=None)
    app.include_router(router=main_router)
    return app
