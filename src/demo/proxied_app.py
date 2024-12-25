"""
In this example we use a custom StripProxyPrefixMiddleware
"""

# from fastapi import FastAPI, Request
import os

from .proxy_middleware import StripProxyPrefixMiddleware
from .simple_app import app as app

# root_path = os.environ.get("FASTAPI_ROOT_PATH")
# app = FastAPI(root_path=root_path)
if os.environ.get("FASTAPI_ROOT_PATH"):
    app.add_middleware(StripProxyPrefixMiddleware)
