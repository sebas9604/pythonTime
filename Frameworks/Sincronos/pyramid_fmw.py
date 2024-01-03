from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def hello_world(request):
    return Response('<h1>Hello World!</h1>')

def good_bye(request):
    return Response("Adios")

if __name__ == '__main__':
    with Configurator() as config:
        config.add_route('hello', '/hello')
        config.add_route('bye', '/bye')
        config.add_view(hello_world, route_name='hello')
        config.add_view(good_bye, route_name='bye')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 6543, app)
    server.serve_forever()