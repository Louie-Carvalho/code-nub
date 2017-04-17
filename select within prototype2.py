pointLayer = iface.activeLayer()
layers = qgis.utils.iface.legendInterface().layers()#magic!
selectedPolyIds = layers[0].selectedFeaturesIds()
polyFeatures = layers[0].getFeatures()

for polyFeature in polyFeatures:
	geomPoly = polyFeature.geometry()
	pointFeatures = pointLayer.getFeatures(QgsFeatureRequest().setFilterRect(geomPoly.boundingBox()))
	for pointFeature in pointFeatures:
		if pointFeature.geometry().within(geomPoly) and polyFeature.id() in selectedPolyIds:
			pointLayer.select(pointFeature.id())