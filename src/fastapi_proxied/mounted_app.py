"""
In this example we optionally wrap, ie mount, the normal FastAPI application in
another application under the given FASTAPI_ROOT_PATH.

Benefits are everything works properly, and we reuse the code from `simple_app`.
"""

from fastapi import FastAPI
import os

from .simple_app import app as orig_app

if root_path := os.environ.get("FASTAPI_ROOT_PATH"):
    app = FastAPI()
    app.mount(root_path, orig_app)
else:
    app = orig_app
