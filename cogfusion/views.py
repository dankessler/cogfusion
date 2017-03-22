from pyramid.view import view_config
import pandas, pkg_resources


@view_config(route_name='home', renderer='templates/home.mako')
def home(request):
    return {}

@view_config(route_name='images', renderer='templates/images.mako')
def images(request):
    csvfile = 'nv_tagging/2016-09-06-neurovault_metadata.csv'
    csvfile = pkg_resources.resource_filename('cogfusion', '../' + csvfile)
    data = pandas.read_csv(csvfile)
    labeledImages = data['cognitive_contrast_cogatlas'].dropna()
    return {'data':labeledImages}

@view_config(route_name='contrasts', renderer='templates/contrasts.mako')
def contrasts(request):
    data = {}
    for view in ('concepts','contrasts','conceptsByContrasts'):
        csvfile = 'data/{}.csv'.format(view)
        csvfile = pkg_resources.resource_filename('cogfusion', '../'+csvfile)
        data[view] = pandas.read_csv(csvfile, encoding='utf-8')
    return data

@view_config(route_name='contrast', renderer='templates/contrast.mako')
def contrast(request):
    cnt = request.matchdict['contrast']
    data = {}
    for view in ('concepts','contrasts','conceptsByContrasts'):
        csvfile = 'data/{}.csv'.format(view)
        csvfile = pkg_resources.resource_filename('cogfusion', '../' + csvfile)
        data[view] = pandas.read_csv(csvfile, encoding='utf-8')
    data['contrastid'] = cnt
    contrasts = data['contrasts']
    contrast = contrasts[contrasts['id']==cnt].iloc[0]
    data['contrast'] = contrast
    return data





