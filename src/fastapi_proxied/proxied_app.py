"""
In this example we use a custom ProxyPrefixMiddleware
"""

from fastapi import FastAPI, Request
import os

from .proxy_middleware import ProxyPrefixMiddleware
from .simple_app import app as app

# root_path = os.environ.get("FASTAPI_ROOT_PATH")
# app = FastAPI(root_path=root_path)
if os.environ.get("FASTAPI_ROOT_PATH"):
    app.add_middleware(ProxyPrefixMiddleware)
