"""
Usage:
    app = FastAPI(root_path=root_path)
    if root_path:
        app.add_middleware(ProxyPrefixMiddleware)
"""


class ProxyPrefixMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] in {"http", "websocket"}:
            root_path = scope["root_path"].rstrip("/")
            scope["path"] = scope["path"].removeprefix(root_path)
        await self.app(scope, receive, send)
