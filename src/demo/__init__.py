# default re-export
from .mounted_app import app as app

from .other import wsgi_app, asgi_app, app as starlette
