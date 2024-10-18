"""
Just a normal FastAPI application
"""

from fastapi import FastAPI, Request

app = FastAPI()


@app.get("/")
async def index(request: Request):
    return {"message": "Hello World", "root_path": request.scope.get("root_path")}


@app.get("/health")
async def health(request: Request):
    return {"status": "ok"}


@app.get("/get-health-url")
async def get_health_url(request: Request):
    return {"status": "ok", "health-url": request.url_for("health")._url}
