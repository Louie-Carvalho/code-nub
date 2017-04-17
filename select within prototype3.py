layers = qgis.utils.iface.legendInterface().layers()#magic!
boundaryLayer = layers[0]
targetLayer = layers[1]
boundaryFeatures = boundaryLayer.getFeatures()
boundaryFeatureIds = boundaryLayer.selectedFeaturesIds()

for boundaryFeature in boundaryFeatures:
	geomPoly = boundaryFeature.geometry()
	targetFeatures = targetLayer.getFeatures(QgsFeatureRequest().setFilterRect(geomPoly.boundingBox()))
	
	for targetFeature in targetFeatures:
		if targetFeature.geometry().within(geomPoly) and boundaryFeature.id() in boundaryFeatureIds:
			targetLayer.select(targetFeature.id())