"""
Using the fastapi.APIRouter, problem is now we need to use the router
for all the handlers and there's more boilerplate (see app.include_router).
We can't reuse the existing `simple_app`.

Also `root_path` is inconsistent (see test)!
"""

from fastapi import FastAPI, Request, APIRouter
import os

app = FastAPI()
prefix = os.environ.get("FASTAPI_ROOT_PATH")
prefix_router = APIRouter(prefix=prefix)


@prefix_router.get("/")
async def root(request: Request):
    return {"message": "Hello World", "root_path": request.scope.get("root_path")}


@prefix_router.get("/health")
async def health(request: Request):
    return {"status": "ok"}


@prefix_router.get("/get-health-url")
async def get_health_url(request: Request):
    return {"status": "ok", "health-url": request.url_for("health")._url}


# It's mandatory this to be after all the routes
app.include_router(prefix_router)
