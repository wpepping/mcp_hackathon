import uvicorn
from app import configure_app

app = configure_app()

if __name__ == "__main__":
    uvicorn.run(app, port=8000, log_config=None, proxy_headers=True)
