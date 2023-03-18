#from owslib.wfs import WebFeatureService
#wfs = WebFeatureService(url='https://geo.vliz.be/geoserver/Emodnetbio/wfs', version='2.0.0')

from owslib.wms import WebMapService
wms = WebMapService('https://ec.oceanbrowser.net/emodnet/Python/web/wms', version='1.3.0')

#Chlorophyll Index
#https://ec.oceanbrowser.net/emodnet/Python/web/wms?SERVICE=WMS&REQUEST=GetCapabilities&VERSION=1.3.0

#print(list(wms.contents)) #list all available datasets
dataset = wms['All_European_Seas/Water_body_chlorophyll-a.nc*Water body chlorophyll-a_L2']
print(dataset.boundingBoxWGS84)
print([op.name for op in wms.operations])
print(wms.getOperationByName('GetMap').methods)
print(wms.getOperationByName('GetMap').formatOptions)
print(dataset.crsOptions)
print(dataset.styles)

img = wms.getmap(   layers=['All_European_Seas/Water_body_chlorophyll-a.nc*Water body chlorophyll-a_L2'],
                    styles=['contourf'],
                    srs='EPSG:4326',
                    bbox=(-45.0, 24.0, 70.0, 83.0),
                    size=(300, 300),
                    format='image/png',
                    transparent=True
                    )
out = open('/mnt/c/Users/Andrew Johnson/Pictures/chlorophyll.png', 'wb')
out.write(img.read())
out.close()
