polyLayer = QgsVectorLayer("C://QGIS//test polygon.shx", "test poly", "ogr")
pointLayer = QgsVectorLayer("C://QGIS//GlenEiraBAP.shp", "GlenEiraBAP", "ogr")

QgsMapLayerRegistry.instance().addMapLayers([pointLayer, polyLayer])

polyFeatures = polyLayer.getFeatures()

for polyFeature in polyFeatures:
    geomPoly = polyFeature.geometry()
    pointFeatures = pointLayer.getFeatures(QgsFeatureRequest().setFilterRect(geomPoly.boundingBox()))
    for pointFeature in pointFeatures:
        if pointFeature.geometry().within(geomPoly):
            pointLayer.select(pointFeature.id())

iface.setActiveLayer(polyLayer)
#iface.zoomToActiveLayer()