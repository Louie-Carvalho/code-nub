import os
from PyQt4.QtGui import *
from geopy.geocoders import GoogleV3 # ensure the GeoCoding plugin is installed
geocoder = GoogleV3()
file = QFileDialog.getOpenFileName()
dataLayer = QgsVectorLayer(file, "importedFile", "ogr") #changed this variable and layer name to a more informative name
#changed the below variable to a more informative name also
layerName,bool = QInputDialog.getText(None, "Layer Name", "Enter Layer Name")
if bool == False:
    print "Layer Name not specified, using default"
    layerName = "Layer"    
pointLayer = QgsVectorLayer('Point?crs=epsg:4326&field=Year:string(4)&field=Lodged Date:DateTime(10)&field=Property Address:string(150)&field=Application Description:string(255)',layerName,"memory")
if not dataLayer.isValid(): #use of new variable name
    print "Layer %s did not load" % dataLayer.name() #use of new variable name
else:
    QgsMapLayerRegistry.instance().addMapLayers([pointLayer]) #use of new variable name

features = dataLayer.getFeatures() #use of new variable name

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
    vpr = pointLayer.dataProvider() #use of new variable name
    point = QgsGeometry.fromPoint(QgsPoint(location.longitude, location.latitude))
    fields = pointLayer.fields() #this was the main issue; was calling from the wrong layer. Shows the importance of using good variable names. I've also changed it
    f = QgsFeature(fields)
    f.setGeometry(point)
    f['Year'] = feature[1] #changed to suit my excel file
    f['Lodged Date'] = feature[2] #changed to suit my excel file
    f['Property Address'] = feature[4] #changed to suit my excel file
    f['Application Description'] = feature[5] #changed to suit my excel file
    vpr.addFeatures([f])

pointLayer.updateExtents() #use of new variable name
print "Records that Failed to GeoCode:"
print failedGeo