from pyramid.view import view_config
import pandas


@view_config(route_name='home', renderer='templates/home.mako')
def home(request):
    return {}

@view_config(route_name='images', renderer='templates/images.mako')
def images(request):
    csvpath = 'nv_tagging/2016-09-06-neurovault_metadata.csv'
    data = pandas.read_csv(csvpath) 
    labeledImages = data['cognitive_contrast_cogatlas'].dropna()
    return {'data':labeledImages}



