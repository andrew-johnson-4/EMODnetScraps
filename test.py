from owslib.wfs import WebFeatureService

wfs = WebFeatureService(url='https://ows.emodnet-bathymetry.eu/wfs', version='2.0.0')

print(wfs.identification.title)
