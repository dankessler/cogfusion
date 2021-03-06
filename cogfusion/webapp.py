from pyramid.config import Configurator
import waitress, os
#from cogfusion.dependencies import Dependencies


def serve():
    wsgiapp = main(None)
    waitress.serve(wsgiapp, host='0.0.0.0', port=80)

def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_mako')
    config.add_static_view('static', 'static', cache_max_age=10)
    config.add_route('home', '/')
    config.add_route('images', '/images')
    config.add_route('contrasts', '/contrasts')
    config.add_route('contrast', '/contrasts/{contrast}')
    #config.add_request_method(lambda r: Dependencies(), 
    #    'dependencies', reify=True)
    config.scan()
    return config.make_wsgi_app()

"""
Documentation:
PasteDeploy: http://pythonpaste.org/deploy/
(Handles reading config from file and picking server and app settings)
Waitress: http://waitress.readthedocs.org/en/latest/
(How to start and configure waitress)
"""
