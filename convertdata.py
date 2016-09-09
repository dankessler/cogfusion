import pickle

contrastsDict = pickle.load(open('data/conceptsByContrasts.pickle','rb'))

associations = []
for contrastid, contrastConcepts in concepts.items():
    for concept in contrastConcepts:
        if hasattr(concept, 'keys'):
            associations.append({'contrast':contrastid, 'concept': concept['id']})


assocDf = pandas.DataFrame(associations)
assocDf.to_csv('data/conceptsByContrasts.csv', encoding='utf-8')


