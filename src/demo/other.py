from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route


async def homepage(request):
    return JSONResponse({'hello': 'world', 'health': f"{request.url_for('health')}"})

async def health(request):
    return JSONResponse({'message': 'ok'})


app = Starlette(debug=True, routes=[
    Route('/', homepage),
    Route('/health', health, name="health"),
])


# raw asgi application

class asgi_app:
    def __init__(self, scope):
        print(scope)
        pass

    async def __call__(self, receive, send):
        await send({
            'type': 'http.response.start',
            'status': 200,
            'headers': [
                [b'content-type', b'text/plain'],
            ]
        })
        await send({
            'type': 'http.response.body',
            'body': b'Hello, world!',
        })

# raw wsgi application
def wsgi_app(environ, start_response):
    status = '200 OK'
    output = b'Hello World!'
    print(environ)

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]

    start_response(status, response_headers)

    return [output]
