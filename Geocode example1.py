import os
from geopy.geocoders import GoogleV3 # ensure the GeoCoding plugin is installed
geocoder = GoogleV3()

file = os.path.abspath("C:\\QGIS\\glen eira baps Viv test2.xlsx")
#file = os.path.abspath("C:\\Users\\vivianmig\\Downloads\\test locations.xlsx")
#specify the file path in " ", folders serapated with \\
dataLayer = QgsVectorLayer(file, "importedFile", "ogr") #changed this variable and layer name to a more informative name
#changed the below variable to a more informative name also
pointLayer = QgsVectorLayer('Point?crs=epsg:4326&field=Year:string(4)&field=Lodged Date:string(10)&field=Property Address:string(150)&field=Application Description:string(255)','GlenEiraBAP',"memory")
if not dataLayer.isValid(): #use of new variable name
    print "Layer %s did not load" % dataLayer.name() #use of new variable name

''' <- To comment out multiple lines at once, use three '
if not newlayer.isValid():
    print "Layer %s did not load" % layer.name()
    Three ' also signifies the close of a multiple line comment -> '''

#QgsMapLayerRegistry.instance().addMapLayers([dataLayer]) #add the dataLayer to prove validation works

features = dataLayer.getFeatures() #use of new variable name
#all = geocoder.geocode(feature[0])

for feature in features:
    if not feature[0]: #This is a method of string checking called falsy - preferred to string ==''
        print "Error in import data! %s is non contiguous" % dataLayer.name()
        break
    elif not feature[1]:
        print "Error in import data! %s is non contiguous" % dataLayer.name()
        break
    elif not feature[2]:
        print "Error in import data! %s is non contiguous" % dataLayer.name()
        break
    elif not feature[3]:
        print "Error in import data! %s is non contiguous" % dataLayer.name()
        break
    elif not feature[4]:
        print "Error in import data! %s is non contiguous" % dataLayer.name()
        break
    all = geocoder.geocode(feature[0]) #changed to suit my excel file
    vpr = pointLayer.dataProvider() #use of new variable name
    point = QgsGeometry.fromPoint(QgsPoint(all.longitude, all.latitude))
    fields = pointLayer.fields() #this was the main issue; was calling from the wrong layer. Shows the importance of using good variable names. I've also changed it
    f = QgsFeature(fields)
    f.setGeometry(point)
    f['Year'] = feature[1] #changed to suit my excel file
    f['Lodged Date'] = feature[2] #changed to suit my excel file
    f['Property Address'] = feature[4] #changed to suit my excel file
    f['Application Description'] = feature[5] #changed to suit my excel file
    vpr.addFeatures([f])

pointLayer.updateExtents() #use of new variable name

QgsMapLayerRegistry.instance().addMapLayers([pointLayer]) #use of new variable name