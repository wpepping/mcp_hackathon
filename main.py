import uvicorn
from app import configure_app
from settings import PORT

app = configure_app()

if __name__ == "__main__":
    uvicorn.run(app, port=PORT, log_config=None, proxy_headers=True)
