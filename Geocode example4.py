import os
from PyQt4.QtGui import *
from geopy.geocoders import GoogleV3 #ensure the GeoCoding plugin is installed
geocoder = GoogleV3()
showInput = True
#cb = QComboBox()
#cb.addItems(["Year", "Lodged Date", "Property Address", "Application Description"])
#cb.resize(200,35)
#cb.show()
file = QFileDialog.getOpenFileName()
dataLayer = QgsVectorLayer(file, "importedFile", "ogr")


if not dataLayer.isValid():
    print "Layer %s did not load" % dataLayer.name()
    showInput = False

if showInput == True:
    layerName,bool = QInputDialog.getText(None, "Layer Name", "Enter Layer Name")
    if bool == False or layerName == '':
        print "Layer Name not specified, using default"
        layerName = "Layer"
    pointLayer = QgsVectorLayer('Point?crs=epsg:4326&field=Year:string(4)&field=Lodged Date:string(10)&field=Property Address:string(150)&field=Application Description:string(255)',layerName,"memory")
    QgsMapLayerRegistry.instance().addMapLayers([pointLayer])

features = dataLayer.getFeatures()

failedGeo = []
for feature in features:
    if not feature[0]: #This is a method of string checking called falsy - preferred to string ==''
        print "Address field not found! Assuming end of file"
        break
    else:
        location = geocoder.geocode(feature[0]) #changed to suit my excel file
        if location is None:
            print "Address cannot be found"
            failedGeo.append(feature[0])
            continue
        else:
            print location.address, location.longitude, location.latitude
    vpr = pointLayer.dataProvider()
    point = QgsGeometry.fromPoint(QgsPoint(location.longitude, location.latitude))
    fields = pointLayer.fields() #this was the main issue; was calling from the wrong layer. Shows the importance of using good variable names. I've also changed it
    f = QgsFeature(fields)
    f.setGeometry(point)
    f['Year'] = feature[1]
    f['Lodged Date'] = feature[2]
    f['Property Address'] = feature[4]
    f['Application Description'] = feature[5]
    vpr.addFeatures([f])

pointLayer.updateExtents()
print "Records that Failed to GeoCode:"
print failedGeo