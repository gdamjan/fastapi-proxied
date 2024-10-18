# FastAPI behind ALB, non-root url prefix

Research fastapi/uvicorn behaviour when proxied by AWS ALB, behind a non-root (`/`)
url path - `/api` in these examples. ALB doesn't rewrite the url request, so
when "mounting" a FastAPI application under a prefix (for ex. `/api`) the application
gets the whole url path (for ex. `/api/a/b/c`).


## Quickstart

```
uv sync
uv run pytest
```

```
FASTAPI_ROOT_PATH=/api/ uv run uvicorn fastapi_proxied:app
```

Expected response from all 3 variants:
```sh
$ curl http://127.0.0.1:8000/api/
{"message":"Hello World","root_path":"/api/"}

$ curl -s http://127.0.0.1:8000/api/openapi.json | jq '.servers[0].url'
"/api"
```

## References
* https://fastapi.tiangolo.com/advanced/behind-a-proxy/
* https://fastapi.tiangolo.com/advanced/sub-applications/
