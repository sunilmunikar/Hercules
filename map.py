
#bounding box to shapefile
import os, os.path, shutil
from osgeo import osr
from osgeo import ogr
from qgis.core import *
from qgis.gui import *
from qgis.utils import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *

# Open the source shapefile.
srcfile = ogr.Open("C:\devPython\TM_WORLD_BORDERS_SIMPL-0.3.shp")
srcLayer = srcfile.GetLayer(0)

# Open the output shapefile.
if os.path.exists("bounding-boxes"):
    shutil.rmtree("bounding-boxes")
os.mkdir("C:\devPython\ bounding-boxes")

spatialReference = osr.SpatialReference()
spatialReference.SetWellKnownGeogCS('WGS84')

driver = ogr.GetDriverByName("ESRI Shapefile")
dstPath = os.path.join("bounding-boxes", "boundingBoxes.shp")
dstFile = driver.CreateDataSource("boundingBoxes.shp")
dstLayer = dstFile.CreateLayer("layer", spatialReference)

fieldDef = ogr.FieldDefn("COUNTRY", ogr.OFTString)
fieldDef.SetWidth(50)
dstLayer.CreateField(fieldDef)

fieldDef = ogr.FieldDefn("CODE", ogr.OFTString)
fieldDef.SetWidth(3)
dstLayer.CreateField(fieldDef)

# Read the country features from the source shapefile.

assert isinstance(srcLayer, object)
for i in range(srcLayer.GetFeatureCount()):
    feature = srcLayer.GetFeature(i)

    countryCode = feature.GetField("ISO3")
    countryName = feature.GetField("NAME")

    geometry = feature.GetGeometryRef()

    minLong, maxLong, minLat, maxLat = geometry.GetEnvelope()

# Save the bounding box as a feature in the output shapefile.

    linearRing = ogr.Geometry(ogr.wkbLinearRing)
    linearRing.AddPoint(minLong, minLat)
    linearRing.AddPoint(maxLong, minLat)
    linearRing.AddPoint(maxLong, maxLat)
    linearRing.AddPoint(minLong, maxLat)
    linearRing.AddPoint(minLong, minLat)

    polygon = ogr.Geometry(ogr.wkbPolygon)
    polygon.AddGeometry(linearRing)

    feature = ogr.Feature(dstLayer.GetLayerDefn())
    feature.SetGeometry(polygon)
    feature.SetField("COUNTRY", countryName)
    feature.SetField("CODE", countryCode)
    dstLayer.CreateFeature(feature)

#All done
srcLayer.Destroy()
dstFile.Destroy()


#
# app = QgsApplication([], True)
# app.setPrefixPath("C:\OSGeo4W\apps\qgis", True)
# app.initQgis()
#
# canvas = QgsMapCanvas()
# canvas.setWindowTitle("PyQGIS Standalone Application Example")
# canvas.setCanvasColor(Qt.white)
# layer = QgsVectorLayer('LineString?crs=epsg:4326', 'MyLine', "memory")
# pr = layer.dataProvider()
# # point1 = QgsPoint(50, 50)
# # point2 = QgsPoint(100, 150)
# # pt = QgsFeature
# # pt.setGeometry(QgsGeometry.fromPoint(point1))
# # pr.addFeatures([pt])
#
# line = QgsFeature()
# line.setGeometry(QgsGeometry.fromPolyline([QgsPoint(10, 20), QgsPoint(20, 30)]))
# #pr.addFeatures([line])
#
# layer.updateExtents()
#
# QgsMapLayerRegistry.instance().addMapLayers([layer])
# canvas.setExtent(layer.extent())
# canvas.setLayerSet([QgsMapCanvasLayer(layer)])
# canvas.zoomToFullExtent()
# canvas.freeze(True)
# canvas.show()
# canvas.refresh()
# canvas.freeze(False)
# canvas.repaint()
# app.exec_()
# QgsApplication.exitQgis()
# sys.exit(app.exec_())