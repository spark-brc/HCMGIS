#!/usr/bin/env python
# -*- coding: utf-8 -*-

# --------------------------------------------------------
#    hcmgis_menu - QGIS plugins menu class
##  --------------------------------------------------------

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from qgis.core import *
from .hcmgis_dialogs import *
from .hcmgis_library import *

# ---------------------------------------------

class hcmgis_menu:
	def __init__(self, iface):
		self.iface = iface
		self.hcmgis_menu = None

	basemap_provider = [ 'Google Maps'		
						]
	basemap_url = ['tmt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}'
					]

	def hcmgis_add_submenu(self, submenu):
		if self.hcmgis_menu != None:
			self.hcmgis_menu.addMenu(submenu)
		else:
			self.iface.addPluginToMenu("&hcmgis", submenu.menuAction())

	def initGui(self):
		# Uncomment the following two lines to have hcmgis accessible from a top-level menu
		self.hcmgis_menu = QMenu(QCoreApplication.translate("hcmgis", "HCMGIS"))
		self.iface.mainWindow().menuBar().insertMenu(self.iface.firstRightStandardMenu().menuAction(), self.hcmgis_menu)
		
		# OpenData_basemap submenu
		self.basemap_menu = QMenu(u'BaseMap')		
		self.hcmgis_add_submenu(self.basemap_menu)

		##https://mc.bbbike.org/mc/?num=2&mt0=mapnik&mt1=watercolor
		#https://gitlab.com/GIS-projects/Belgium-XYZ-tiles/tree/b538df2c2de0d16937641742f25e4709ca94e42e
		
		#############
		#Google Maps
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_googlemaps.png")
		self.googlemaps_action = QAction(icon, u'Google Maps', self.iface.mainWindow())
		self.googlemaps_action.triggered.connect(self.googlemaps_call)		
		self.basemap_menu.addAction(self.googlemaps_action)
		
		#Google Satellite
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_googlemaps.png")
		self.googlesatellite_action = QAction(icon, u'Google Satellite', self.iface.mainWindow())
		self.googlesatellite_action.triggered.connect(self.googlesatellite_call)		
		self.basemap_menu.addAction(self.googlesatellite_action)

		#Google Satellite Hybrid
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_googlemaps.png")
		self.hcmgis_googlesatellitehybrid_action = QAction(icon, u'Google Satellite Hybrid', self.iface.mainWindow())
		self.hcmgis_googlesatellitehybrid_action.triggered.connect(self.googlesatellitehybrid_call)		
		self.basemap_menu.addAction(self.hcmgis_googlesatellitehybrid_action)

				
		#Google Terrain
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_googlemaps.png")
		self.hcmgis_googleterrain_action = QAction(icon, u'Google Terrain', self.iface.mainWindow())
		self.hcmgis_googleterrain_action.triggered.connect(self.googleterrain_call)		
		self.basemap_menu.addAction(self.hcmgis_googleterrain_action)

		#Google Terrain Hybrid
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_googlemaps.png")
		self.hcmgis_googleterrainhybrid_action = QAction(icon, u'Google Terrain Hybrid', self.iface.mainWindow())
		self.hcmgis_googleterrainhybrid_action.triggered.connect(self.googleterrainhybrid_call)		
		self.basemap_menu.addAction(self.hcmgis_googleterrainhybrid_action)

		
		#############
		#Bing Virtual Earth
		#############
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_bing.png")
		self.bingaerial_action = QAction(icon, u'Bing VirtualEarth', self.iface.mainWindow())
		self.bingaerial_action.triggered.connect(self.bingaerial_call)		
		self.basemap_menu.addAction(self.bingaerial_action)
 

		#Carto Antique
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_carto.png")
		self.cartoantique_action = QAction(icon, u'Carto Antique', self.iface.mainWindow())
		self.cartoantique_action.triggered.connect(self.cartoantique_call)		
		self.basemap_menu.addAction(self.cartoantique_action)

		#Carto Dark
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_carto.png")
		self.cartodark_action = QAction(icon, u'Carto Dark', self.iface.mainWindow())
		self.cartodark_action.triggered.connect(self.cartodark_call)		
		self.basemap_menu.addAction(self.cartodark_action)

		#Carto Eco
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_carto.png")
		self.cartoeco_action = QAction(icon, u'Carto Eco', self.iface.mainWindow())
		self.cartoeco_action.triggered.connect(self.cartoeco_call)		
		self.basemap_menu.addAction(self.cartoeco_action)

		#Carto Light
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_carto.png")
		self.cartolight_action = QAction(icon, u'Carto Light', self.iface.mainWindow())
		self.cartolight_action.triggered.connect(self.cartolight_call)		
		self.basemap_menu.addAction(self.cartolight_action)

		
		#########################		
		# ESRI https://gitlab.com/GIS-projects/Belgium-XYZ-tiles/tree/b538df2c2de0d16937641742f25e4709ca94e42e
		#####################
		#Esri Boundaries and Places 
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_esri.png")
		self.esriboundary_action = QAction(icon, u'Esri Boundaries and Places', self.iface.mainWindow())
		self.esriboundary_action.triggered.connect(self.esriboundary_call)		
		self.basemap_menu.addAction(self.esriboundary_action)

		#Esri Dark Gray 
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_esri.png")
		self.esridarkgray_action = QAction(icon, u'Esri Dark Gray', self.iface.mainWindow())
		self.esridarkgray_action.triggered.connect(self.esridarkgray_call)		
		self.basemap_menu.addAction(self.esridarkgray_action)

		#Esri DeLorme World Base Map
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_esri.png")
		self.esridelorme_action = QAction(icon, u'ESri DeLorme', self.iface.mainWindow())
		self.esridelorme_action.triggered.connect(self.esridelorme_call)		
		self.basemap_menu.addAction(self.esridelorme_action)

		#Esri Imagery 
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_esri.png")
		self.esriimagery_action = QAction(icon, u'Esri Imagery', self.iface.mainWindow())
		self.esriimagery_action.triggered.connect(self.esriimagery_call)		
		self.basemap_menu.addAction(self.esriimagery_action)
	
		#Esri Light Gray 
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_esri.png")
		self.esrilightgray_action = QAction(icon, u'Esri Light Gray', self.iface.mainWindow())
		self.esrilightgray_action.triggered.connect(self.esrilightgray_call)		
		self.basemap_menu.addAction(self.esrilightgray_action)

		#Esri National Geographic World Map
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_esri.png")
		self.esrinational_action = QAction(icon, u'Esri National Geographic', self.iface.mainWindow())
		self.esrinational_action.triggered.connect(self.esrinational_call)		
		self.basemap_menu.addAction(self.esrinational_action)

		#Esri Ocean Basemap
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_esri.png")
		self.esriocean_action = QAction(icon, u'Esri Ocean', self.iface.mainWindow())
		self.esriocean_action.triggered.connect(self.esriocean_call)		
		self.basemap_menu.addAction(self.esriocean_action)

		#Esri Physical Map
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_esri.png")
		self.esriphysical_action = QAction(icon, u'Esri Physical', self.iface.mainWindow())
		self.esriphysical_action.triggered.connect(self.esriphysical_call)		
		self.basemap_menu.addAction(self.esriphysical_action)

		#Esri Shaded Relief
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_esri.png")
		self.esrishaded_action = QAction(icon, u'Esri Shaded Relief', self.iface.mainWindow())
		self.esrishaded_action.triggered.connect(self.esrishaded_call)		
		self.basemap_menu.addAction(self.esrishaded_action)

		#Esri Street Map
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_esri.png")
		self.esristreet_action = QAction(icon, u'Esri Street', self.iface.mainWindow())
		self.esristreet_action.triggered.connect(self.esristreet_call)		
		self.basemap_menu.addAction(self.esristreet_action)

		#Esri Terrain Map
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_esri.png")
		self.esriterrain_action = QAction(icon, u'Esri Terrain', self.iface.mainWindow())
		self.esriterrain_action.triggered.connect(self.esriterrain_call)		
		self.basemap_menu.addAction(self.esriterrain_action)
		
		#Esri World Topo Map
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_esri.png")
		self.esritopo_action = QAction(icon, u'Esri Topographic', self.iface.mainWindow())
		self.esritopo_action.triggered.connect(self.esritopo_call)		
		self.basemap_menu.addAction(self.esritopo_action)

		# """ #Esri World Transportation
		# icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_esri.png")
		# self.esritransport_action = QAction(icon, u'Esri Transport', self.iface.mainWindow())
		# self.esritransport_action.triggered.connect(self.esritransport_call)		
		# self.basemap_menu.addAction(self.esritransport_action)
		#  """
		
		##############################
		# F4map - 2D
		#############################
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_f4map.png")
		self.f4map_action = QAction(icon, u'F4 Map - 2D', self.iface.mainWindow())
		self.f4map_action.triggered.connect(self.f4map_call)		
		self.basemap_menu.addAction(self.f4map_action)

		##############################
		# OpenTopoMap
		#############################
		# """ icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_opentopomap.png")
		# self.opentopomap_action = QAction(icon, u'OpenTopoMap', self.iface.mainWindow())
		# self.opentopomap_action.triggered.connect(self.opentopomap_call)		
		# self.basemap_menu.addAction(self.opentopomap_action) """
		

		
		#Stamen Toner
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_stamen.png")
		self.stamentoner_action = QAction(icon, u'Stamen Toner', self.iface.mainWindow())
		self.stamentoner_action.triggered.connect(self.stamentoner_call)		
		self.basemap_menu.addAction(self.stamentoner_action)

		# Stamen Toner Background
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_stamen.png")
		self.stamentonerbkg_action = QAction(icon, u'Stamen Toner Background', self.iface.mainWindow())
		self.stamentonerbkg_action.triggered.connect(self.stamentonerbkg_call)		
		self.basemap_menu.addAction(self.stamentonerbkg_action)

		# Stamen Toner Hybrid
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_stamen.png")
		self.stamentonerhybrid_action = QAction(icon, u'Stamen Toner Hybrid', self.iface.mainWindow())
		self.stamentonerhybrid_action.triggered.connect(self.stamentonerhybrid_call)		
		self.basemap_menu.addAction(self.stamentonerhybrid_action)

		# Stamen Toner Lite
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_stamen.png")
		self.stamentonerlite_action = QAction(icon, u'Stamen Toner Lite', self.iface.mainWindow())
		self.stamentonerlite_action.triggered.connect(self.stamentonerlite_call)		
		self.basemap_menu.addAction(self.stamentonerlite_action)
		
		# Stamen Terrain
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_stamen.png")
		self.stamenterrain_action = QAction(icon, u'Stamen Terrain', self.iface.mainWindow())
		self.stamenterrain_action.triggered.connect(self.stamenterrain_call)		
		self.basemap_menu.addAction(self.stamenterrain_action)

		# Stamen Terrain Background
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_stamen.png")
		self.stamenterrainbkg_action = QAction(icon, u'Stamen Terrain Background', self.iface.mainWindow())
		self.stamenterrainbkg_action.triggered.connect(self.stamenterrainbkg_call)		
		self.basemap_menu.addAction(self.stamenterrainbkg_action)
		
		# Stamen Watercolor
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_stamen.png")
		self.stamenwatercolor_action = QAction(icon, u'Stamen Watercolor', self.iface.mainWindow())
		self.stamenwatercolor_action.triggered.connect(self.stamenwatercolor_call)		
		self.basemap_menu.addAction(self.stamenwatercolor_action)
				
		# Wikimedia Maps
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_wikimedia.png")
		self.wikimedia_action = QAction(icon, u'Wikimedia Maps', self.iface.mainWindow())
		self.wikimedia_action.triggered.connect(self.wikimedia_call)		
		self.basemap_menu.addAction(self.wikimedia_action)
	# """ 
	# 	# Strava Run
	# 	icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_strava.png")
	# 	self.stravarun_action = QAction(icon, u'Strava Run', self.iface.mainWindow())
	# 	self.stravarun_action.triggered.connect(self.stravarun_call)		
	# 	self.basemap_menu.addAction(self.stravarun_action)

	# 	# Strava All
	# 	icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_strava.png")
	# 	self.stravaall_action = QAction(icon, u'Strava All', self.iface.mainWindow())
	# 	self.stravaall_action.triggered.connect(self.stravaall_call)		
	# 	self.basemap_menu.addAction(self.stravaall_action) """	

	# """ # Wikimedia Hike Bike
	# 	icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_wikimedia.png")
	# 	self.wikimediahikebike_action = QAction(icon, u'Wikimedia Hike Bike', self.iface.mainWindow())
	# 	self.wikimediahikebike_action.triggered.connect(self.wikimediahikebike_call)		
	# 	self.basemap_menu.addAction(self.wikimediahikebike_action)
	# 	 """

		#Viet Ban do
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_vbd.png")
		self.hcmgis_vbd_action = QAction(icon, u'Vietbando Maps', self.iface.mainWindow())
		self.hcmgis_vbd_action.triggered.connect(self.vbd_call)		
		self.basemap_menu.addAction(self.hcmgis_vbd_action)

		#HCMGIS Aerial Image
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_opendata.png")
		self.hcmgisaerial_action = QAction(icon, u'HCMGIS Aerial Images', self.iface.mainWindow())
		self.hcmgisaerial_action.triggered.connect(self.hcmgisaerial_call)		
		self.basemap_menu.addAction(self.hcmgisaerial_action)
		
		# Batch Converter Submenu
		self.batch_converter_menu = QMenu(u'Batch Converter')	
		self.hcmgis_add_submenu(self.batch_converter_menu)

		# Vector Format Converter
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_opendata.png")
		self.formatconvert_action = QAction(icon, u'Vector Format Converter', self.iface.mainWindow())
		self.formatconvert_action.triggered.connect(self.formatconvert)
		self.batch_converter_menu.addAction(self.formatconvert_action)

		# CSV point to Shapefile
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_opendata.png")
		self.csv2shp_action = QAction(icon, u'CSV to Point', self.iface.mainWindow())
		self.csv2shp_action.triggered.connect(self.csv2shp)
		self.batch_converter_menu.addAction(self.csv2shp_action)

		# TXT to CSV
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_opendata.png")
		self.txt2csv_action = QAction(icon, u'TXT to CSV', self.iface.mainWindow())
		self.txt2csv_action.triggered.connect(self.txt2csv)
		self.batch_converter_menu.addAction(self.txt2csv_action)

		
		# XLS to CSV
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_opendata.png")
		self.xls2csv_action = QAction(icon, u'XLSX to CSV', self.iface.mainWindow())
		self.xls2csv_action.triggered.connect(self.xls2csv)
		self.batch_converter_menu.addAction(self.xls2csv_action)

		#HCMGIS OpenData submenu
		self.covid19_menu = QMenu(u'Download COVID-19 Data')		
		self.hcmgis_add_submenu(self.covid19_menu)	
		
		#Global CoVID-19 live update
		self.hcmgis_add_submenu(self.covid19_menu)
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_covid19.png")
		self.covid19_action = QAction(icon, u'Global COVID-19 Live Update - Johns Hopkins CSSE', self.iface.mainWindow())
		self.covid19_action.triggered.connect(self.covid19)		
		self.covid19_menu.addAction(self.covid19_action)

		
		#Global CoVID-19 Timeseries 
		self.hcmgis_add_submenu(self.covid19_menu)
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_covid19.png")
		self.covid19_timeseries_action = QAction(icon, u'Global COVID-19 Time Series - Johns Hopkins CSSE', self.iface.mainWindow())
		self.covid19_timeseries_action.triggered.connect(self.covid19_timeseries)		
		self.covid19_menu.addAction(self.covid19_timeseries_action)

		#Vietnam CoVID-19 live update 
		self.hcmgis_add_submenu(self.covid19_menu)
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_opendata.png")
		self.covid19_vietnam_action = QAction(icon, u'Vietnam COVID-19 Live Update - HCMGIS OpenData', self.iface.mainWindow())
		self.covid19_vietnam_action.triggered.connect(self.covid19_vietnam)		
		self.covid19_menu.addAction(self.covid19_vietnam_action)


		#HCMGIS OpenData submenu
		self.opendata_menu = QMenu(u'Download OpenData')		
		self.hcmgis_add_submenu(self.opendata_menu)	

		#OSM Data from Geofabrik 
		self.hcmgis_add_submenu(self.opendata_menu)
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_geofabrik.png")
		self.geofabrik_action = QAction(icon, u'OSM Data by Country from Geofabrik', self.iface.mainWindow())
		self.geofabrik_action.triggered.connect(self.geofabrik)		
		self.opendata_menu.addAction(self.geofabrik_action)

		#OSM Data from Geofabrik 
		self.hcmgis_add_submenu(self.opendata_menu)
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_gadm.png")
		self.gadm_action = QAction(icon, u'Global Administrative Areas by Country from GADM', self.iface.mainWindow())
		self.gadm_action.triggered.connect(self.gadm)		
		self.opendata_menu.addAction(self.gadm_action)


		# #Open Development Mekong
		# self.hcmgis_add_submenu(self.opendata_menu)
		# icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_odmekong.png")
		# self.opendevelopmentmekong_action = QAction(icon, u'Open Development Mekong', self.iface.mainWindow())
		# self.opendevelopmentmekong_action.triggered.connect(self.opendevelopmentmekong)		
		# self.opendata_menu.addAction(self.opendevelopmentmekong_action)

		#HCMGIS OpenData
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_opendata.png")
		self.opendata_action = QAction(icon, u'HCMGIS OpenData and other WFS Servers', self.iface.mainWindow())
		self.opendata_action.triggered.connect(self.opendata)		
		self.opendata_menu.addAction(self.opendata_action)


		
		# VN-2000 Projections submenu
		self.projections_menu = QMenu(u'VN-2000/TM-3')		
		self.hcmgis_add_submenu(self.projections_menu)
		
		# VN-2000 Projections
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_projections.png")
		self.projections_action = QAction(icon, u'EPSG Code for VN-2000/TM-3', self.iface.mainWindow())
		self.projections_action.triggered.connect(self.projections)		
		self.projections_menu.addAction(self.projections_action)

		
		# Merge_Split submenu
		self.geoprocessing_menu = QMenu(u'Geometry Processing')		
		self.hcmgis_add_submenu(self.geoprocessing_menu)
		
		# MediAxis Submenu
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_skeleton.png")
		self.medialaxis_action = QAction(icon, u'Skeleton/ Medial Axis', self.iface.mainWindow())
		self.medialaxis_action.triggered.connect(self.medialaxis)
		self.geoprocessing_menu.addAction(self.medialaxis_action)
		
		# Centerline Submenu
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_centerline.png")
		self.centerline_action = QAction(icon, u"Centerline in Polygons' Gaps", self.iface.mainWindow())
		self.centerline_action.triggered.connect(self.centerline)
		self.geoprocessing_menu.addAction(self.centerline_action)

		# Closest pair of Points Submenu
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_closestpair.png")
		self.closestpair_action = QAction(icon, u"Closest/ farthest pair of Points", self.iface.mainWindow())
		self.closestpair_action.triggered.connect(self.closestpair)
		self.geoprocessing_menu.addAction(self.closestpair_action)

		
		# Largest Empty Circle Submenu
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_lec.png")
		self.lec_action = QAction(icon, u"Largest Empty Circle", self.iface.mainWindow())
		self.lec_action.triggered.connect(self.lec)
		self.geoprocessing_menu.addAction(self.lec_action)
		

		#Merge
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_merge.png")
		self.merge_action = QAction(icon, u'Merge Layers', self.iface.mainWindow())
		self.merge_action.triggered.connect(self.merge)		
		self.geoprocessing_menu.addAction(self.merge_action)
		
		#Splits
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_split.png")
		self.split_action = QAction(icon, u'Split Layer', self.iface.mainWindow())
		self.split_action.triggered.connect(self.split)
		self.geoprocessing_menu.addAction(self.split_action)
		
		# Tool Submenu
		self.tool_menu = QMenu(u'Calculate Field')	
		self.hcmgis_add_submenu(self.tool_menu)
				
		
		# Merge Field Submenu
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_merge_field.png")
		self.mergefield_action = QAction(icon, u'Merge Fields', self.iface.mainWindow())
		self.mergefield_action.triggered.connect(self.mergefield)
		#QObject.connect(self.mergefield_action, SIGNAL("triggered()"), self.mergefield)
		self.tool_menu.addAction(self.mergefield_action)
		
		# Split Field Submenu
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_split_field.png")
		self.splitfield_action = QAction(icon, u'Split Field', self.iface.mainWindow())
		self.splitfield_action.triggered.connect(self.splitfield)
		#QObject.connect(self.splitfield_action, SIGNAL("triggered()"), self.splitfield)
		self.tool_menu.addAction(self.splitfield_action)

		# FontConverter Submenu
		icon = QIcon(os.path.dirname(__file__) + "/icons/hcmgis_font_converter.png")
		self.fontconverter_action = QAction(icon, u'Vietnamese Font Converter', self.iface.mainWindow())
		self.fontconverter_action.triggered.connect(self.fontconverter)
		#QObject.connect(self.fontconverter_action, SIGNAL("triggered()"), self.fontconverter)
		self.tool_menu.addAction(self.fontconverter_action)	

		
		
	def unload(self):
		if self.hcmgis_menu != None:
			self.iface.mainWindow().menuBar().removeAction(self.hcmgis_menu.menuAction())
		else:
			self.iface.removePluginMenu("&hcmgis", self.basemap_menu.menuAction())
			self.iface.removePluginMenu("&hcmgis", self.batch_converter_menu.menuAction())
			self.iface.removePluginMenu("&hcmgis", self.covid19_menu.menuAction())						
			self.iface.removePluginMenu("&hcmgis", self.openddata_menu.menuAction())
			self.iface.removePluginMenu("&hcmgis", self.projections_menu.menuAction())			
			self.iface.removePluginMenu("&hcmgis", self.geoprocessing_menu.menuAction())
			self.iface.removePluginMenu("&hcmgis", self.tool_menu.menuAction())
			

	##############
	# Google
	############
	def basemaps_call(self, basemap_index):		
		hcmgis_basemap(self.iface,self.basemap_url[basemap_index],self.basemap_provider[basemap_index])

	def googlemaps_call(self):
		service_url ="mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}"
		name = "Google Maps"
		hcmgis_basemap(self.iface,service_url, name)


	def googlesatellite_call(self):
		service_url ="mt1.google.com/vt/lyrs=s&x={x}&y={y}&z={z}" 
		name = "Google Satellite"
		hcmgis_basemap(self.iface,service_url, name)
	

	def googlesatellitehybrid_call(self):
		service_url ="mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}"
		name = "Google Satellite Hybrid"
		hcmgis_basemap(self.iface,service_url, name)
	

	def googleterrain_call(self):
		service_url ="mt1.google.com/vt/lyrs=t&x={x}&y={y}&z={z}" 
		name = "Google Terrain"
		hcmgis_basemap(self.iface,service_url, name)

	def googleterrainhybrid_call(self):
		service_url ="mt1.google.com/vt/lyrs=p&x={x}&y={y}&z={z}"
		name = "Google Terrain Hybrid"
		hcmgis_basemap(self.iface,service_url, name)

	##############
	# Bing
	############
	def bingaerial_call(self):
		import requests
		import qgis.utils
		name = "Bing Virtual Earth"
		urlWithParams = 'type=xyz&url=http://ecn.t3.tiles.virtualearth.net/tiles/a{q}.jpeg?g=1'
		rlayer = QgsRasterLayer(urlWithParams, name, 'wms') 
		if rlayer.isValid():    
			QgsProject.instance().addMapLayer(rlayer)
		
		sources = []
		service_uri1 ="http://ecn.t3.tiles.virtualearth.net/tiles/a{q}.jpeg?g=1"
		sources.append(["connections-xyz",name,"","","",service_uri1,"","22","0"])
		for source in sources:
			connectionType = source[0]
			connectionName = source[1]
			QSettings().setValue("qgis/%s/%s/authcfg" % (connectionType, connectionName), source[2])
			QSettings().setValue("qgis/%s/%s/password" % (connectionType, connectionName), source[3])
			QSettings().setValue("qgis/%s/%s/referer" % (connectionType, connectionName), source[4])
			QSettings().setValue("qgis/%s/%s/url" % (connectionType, connectionName), source[5])
			QSettings().setValue("qgis/%s/%s/username" % (connectionType, connectionName), source[6])
			QSettings().setValue("qgis/%s/%s/zmax" % (connectionType, connectionName), source[7])
			QSettings().setValue("qgis/%s/%s/zmin" % (connectionType, connectionName), source[8])
		# Update GUI
		qgis.utils.iface.reloadConnections()
		 

	##############
	# Carto
	############
	def cartolight_call(self):
		service_url ="a.basemaps.cartocdn.com/light_all/{z}/{x}/{y}.png" 
		name = "Carto Light"
		hcmgis_basemap(self.iface,service_url, name)
		
	def cartodark_call(self):
		service_url ="a.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}.png" 
		name = "Carto Dark"
		hcmgis_basemap(self.iface,service_url, name)
	
	def cartoantique_call(self):
		service_url ="cartocdn_a.global.ssl.fastly.net/base-antique/{z}/{x}/{y}.png" 
		name = "Carto Antique"
		hcmgis_basemap(self.iface,service_url, name)

	def cartoeco_call(self):
		service_url ="cartocdn_a.global.ssl.fastly.net/base-eco/{z}/{x}/{y}.png" 
		name = "Carto Eco"
		hcmgis_basemap(self.iface,service_url, name)
	
		
	#########################		
	# ESRI
	#####################
	def esridelorme_call(self):
		service_url ="server.arcgisonline.com/arcgis/rest/services/Specialty/DeLorme_World_Base_Map/MapServer/tile/{z}/{y}/{x}" 
		name = "Esri DeLorme"
		hcmgis_basemap(self.iface,service_url, name)
	
	def esrinational_call(self):
		service_url ="server.arcgisonline.com/arcgis/rest/services/NatGeo_World_Map/MapServer/tile/{z}/{y}/{x}" 
		name = "Esri National Geographic"
		hcmgis_basemap(self.iface,service_url, name)
	
	def esriocean_call(self):
		service_url ="server.arcgisonline.com/arcgis/rest/services/Ocean_Basemap/MapServer/tile/{z}/{y}/{x}" 
		name = "Esri Ocean"
		hcmgis_basemap(self.iface,service_url, name)

	def esriboundary_call(self):
		service_url ="server.arcgisonline.com/ArcGIS/rest/services/Reference/World_Boundaries_and_Places/MapServer/tile/{z}/{y}/{x}" 
		name = "Esri Boundaries and Places"
		hcmgis_basemap(self.iface,service_url, name)
	
	def esridarkgray_call(self):
		service_url ="server.arcgisonline.com/arcgis/rest/services/Canvas/World_Dark_Gray_Base/MapServer/tile/{z}/{y}/{x}" 
		name = "Esri Dark Gray"
		hcmgis_basemap(self.iface,service_url, name)

	def esrilightgray_call(self):
		service_url ="server.arcgisonline.com/arcgis/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}" 
		name = "Esri Light Gray"
		hcmgis_basemap(self.iface,service_url, name)

	def esriimagery_call(self):
		service_url ="server.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer/tile/{z}/{y}/{x}" 
		name = "Esri Imagery"
		hcmgis_basemap(self.iface,service_url, name)

	def esriphysical_call(self):
		service_url ="server.arcgisonline.com/arcgis/rest/services/World_Physical_Map/MapServer/tile/{z}/{y}/{x}" 
		name = "Esri Physical"
		hcmgis_basemap(self.iface,service_url, name)
	
	def esristreet_call(self):
		service_url ="server.arcgisonline.com/arcgis/rest/services/World_Street_Map/MapServer/tile/{z}/{y}/{x}" 
		name = "Esri Street"
		hcmgis_basemap(self.iface,service_url, name)
	
	def esriterrain_call(self):
		service_url ="server.arcgisonline.com/arcgis/rest/services/World_Terrain_Base/MapServer/tile/{z}/{y}/{x}" 
		name = "Esri Terrain"
		hcmgis_basemap(self.iface,service_url, name)

	def esritopo_call(self):
		service_url ="server.arcgisonline.com/arcgis/rest/services/World_Topo_Map/MapServer/tile/{z}/{y}/{x}" 
		name = "Esri Topographic"
		hcmgis_basemap(self.iface,service_url, name)
	
	""" def esritransport_call(self):
		service_url ="server.arcgisonline.com/arcgis/rest/services/Reference/World_Transportation/MapServer/tile/{z}/{y}/{x}" 
		name = "Esri Transport"
		hcmgis_basemap(self.iface,service_url, name) """

	def esrishaded_call(self):
		service_url ="server.arcgisonline.com/arcgis/rest/services/World_Shaded_Relief/MapServer/tile/{z}/{y}/{x}" 
		name = "Esri Shaded Relief"
		hcmgis_basemap(self.iface,service_url, name)

	#########################		
	# F4 Map
	#####################
	def f4map_call(self):
		service_url ="tile1.f4map.com/tiles/f4_2d/{z}/{x}/{y}.png" 
		name = "F4map"
		hcmgis_basemap(self.iface,service_url, name)

	#########################		
	# OpenTopoMap
	#####################
	def opentopomap_call(self):
		import requests
		import qgis.utils
		name = "OpenTopoMap"	
		urlWithParams = 'type=xyz&url=tile.opentopomap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png'
		rlayer = QgsRasterLayer(urlWithParams,name, 'wms') 
		if rlayer.isValid():    
			QgsProject.instance().addMapLayer(rlayer)
		
		sources = []
		service_uri1 ="tile.opentopomap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png"
		sources.append(["connections-xyz",name,"","","",service_uri1,"","22","0"])
		for source in sources:
			connectionType = source[0]
			connectionName = source[1]
			QSettings().setValue("qgis/%s/%s/authcfg" % (connectionType, connectionName), source[2])
			QSettings().setValue("qgis/%s/%s/password" % (connectionType, connectionName), source[3])
			QSettings().setValue("qgis/%s/%s/referer" % (connectionType, connectionName), source[4])
			QSettings().setValue("qgis/%s/%s/url" % (connectionType, connectionName), source[5])
			QSettings().setValue("qgis/%s/%s/username" % (connectionType, connectionName), source[6])
			QSettings().setValue("qgis/%s/%s/zmax" % (connectionType, connectionName), source[7])
			QSettings().setValue("qgis/%s/%s/zmin" % (connectionType, connectionName), source[8])
		# Update GUI
		qgis.utils.iface.reloadConnections()
	
	#########################		
	# Stamen
	#####################	
	def stamenwatercolor_call(self):
		service_url = "c.tile.stamen.com/watercolor/{z}/{x}/{y}.jpg" 
		name = "Stamen Watercolor"
		hcmgis_basemap(self.iface,service_url, name)
	
	def stamentoner_call(self):
		service_url ="a.tile.stamen.com/toner/{z}/{x}/{y}.png"
		name = "Stamen Toner"
		hcmgis_basemap(self.iface,service_url, name)
	
	def stamentonerbkg_call(self):
		service_url ="a.tile.stamen.com/toner-background/{z}/{x}/{y}.png"
		name = "Stamen Toner Background"
		hcmgis_basemap(self.iface,service_url, name)

	def stamentonerhybrid_call(self):
		service_url ="a.tile.stamen.com/toner-hybrid/{z}/{x}/{y}.png"
		name = "Stamen Toner Hybrid"
		hcmgis_basemap(self.iface,service_url, name)

	def stamentonerlite_call(self):
		service_url ="a.tile.stamen.com/toner-lite/{z}/{x}/{y}.png"
		name = "Stamen Toner Lite"
		hcmgis_basemap(self.iface,service_url, name)

	
	def stamenterrain_call(self):
		service_url ="a.tile.stamen.com/terrain/{z}/{x}/{y}.png" 
		name = "Stamen Terrain"
		hcmgis_basemap(self.iface,service_url, name)
	
	def stamenterrainbkg_call(self):
		service_url ="a.tile.stamen.com/terrain-background/{z}/{x}/{y}.png" 
		name = "Stamen Terrain Background"
		hcmgis_basemap(self.iface,service_url, name)

	###################################
	# Strava
	#####################	

	def stravarun_call(self):
		import requests
		import qgis.utils
		name = "strava Run"
		urlWithParams = 'type=xyz&url=heatmap-external-b.strava.com/tiles/run/bluered/%7Bz%7D/%7Bx%7D/%7By%7D.png?v=19'
		rlayer = QgsRasterLayer(urlWithParams,name, 'wms') 
		if rlayer.isValid():    
			QgsProject.instance().addMapLayer(rlayer)
		
		sources = []
		service_uri1 ="heatmap-external-b.strava.com/tiles/run/bluered/%7Bz%7D/%7Bx%7D/%7By%7D.png?v=19"
		sources.append(["connections-xyz",name,"","","",service_uri1,"","22","0"])
		for source in sources:
			connectionType = source[0]
			connectionName = source[1]
			QSettings().setValue("qgis/%s/%s/authcfg" % (connectionType, connectionName), source[2])
			QSettings().setValue("qgis/%s/%s/password" % (connectionType, connectionName), source[3])
			QSettings().setValue("qgis/%s/%s/referer" % (connectionType, connectionName), source[4])
			QSettings().setValue("qgis/%s/%s/url" % (connectionType, connectionName), source[5])
			QSettings().setValue("qgis/%s/%s/username" % (connectionType, connectionName), source[6])
			QSettings().setValue("qgis/%s/%s/zmax" % (connectionType, connectionName), source[7])
			QSettings().setValue("qgis/%s/%s/zmin" % (connectionType, connectionName), source[8])
		# Update GUI
		qgis.utils.iface.reloadConnections()

	
	
	def stravaall_call(self):	
		import requests
		import qgis.utils
		name = "strava All"
		urlWithParams = 'type=xyz&url=heatmap-external-b.strava.com/tiles/all/bluered/%7Bz%7D/%7Bx%7D/%7By%7D.png'
		rlayer = QgsRasterLayer(urlWithParams, name, 'wms') 
		if rlayer.isValid():    
			QgsProject.instance().addMapLayer(rlayer)
		
		sources = []
		service_uri1 ="heatmap-external-b.strava.com/tiles/all/bluered/%7Bz%7D/%7Bx%7D/%7By%7D.png"
		sources.append(["connections-xyz",name,"","","",service_uri1,"","22","0"])
		for source in sources:
			connectionType = source[0]
			connectionName = source[1]
			QSettings().setValue("qgis/%s/%s/authcfg" % (connectionType, connectionName), source[2])
			QSettings().setValue("qgis/%s/%s/password" % (connectionType, connectionName), source[3])
			QSettings().setValue("qgis/%s/%s/referer" % (connectionType, connectionName), source[4])
			QSettings().setValue("qgis/%s/%s/url" % (connectionType, connectionName), source[5])
			QSettings().setValue("qgis/%s/%s/username" % (connectionType, connectionName), source[6])
			QSettings().setValue("qgis/%s/%s/zmax" % (connectionType, connectionName), source[7])
			QSettings().setValue("qgis/%s/%s/zmin" % (connectionType, connectionName), source[8])
		# Update GUI
		qgis.utils.iface.reloadConnections()


	##############
	# Vietbando Maps
	############
	def vbd_call(self):	
		import requests
		import qgis.utils
		name = "Vietbando"	
		urlWithParams = 'type=xyz&url=http://images.vietbando.com/ImageLoader/GetImage.ashx?Ver%3D2016%26LayerIds%3DVBD%26Y%3D%7By%7D%26X%3D%7Bx%7D%26Level%3D%7Bz%7D'
		rlayer = QgsRasterLayer(urlWithParams,name, 'wms') 
		if rlayer.isValid():    
			QgsProject.instance().addMapLayer(rlayer)
		
		sources = []
		service_uri1 ="http://images.vietbando.com/ImageLoader/GetImage.ashx?Ver%3D2016%26LayerIds%3DVBD%26Y%3D%7By%7D%26X%3D%7Bx%7D%26Level%3D%7Bz%7D"
		sources.append(["connections-xyz",name,"","","",service_uri1,"","22","0"])
		for source in sources:
			connectionType = source[0]
			connectionName = source[1]
			QSettings().setValue("qgis/%s/%s/authcfg" % (connectionType, connectionName), source[2])
			QSettings().setValue("qgis/%s/%s/password" % (connectionType, connectionName), source[3])
			QSettings().setValue("qgis/%s/%s/referer" % (connectionType, connectionName), source[4])
			QSettings().setValue("qgis/%s/%s/url" % (connectionType, connectionName), source[5])
			QSettings().setValue("qgis/%s/%s/username" % (connectionType, connectionName), source[6])
			QSettings().setValue("qgis/%s/%s/zmax" % (connectionType, connectionName), source[7])
			QSettings().setValue("qgis/%s/%s/zmin" % (connectionType, connectionName), source[8])
		# Update GUI
		qgis.utils.iface.reloadConnections()
		
	###################################
	def hcmgisaerial_call(self):
		service_url = "trueortho.hcmgis.vn/basemap/cache_lidar/{z}/{x}/{y}.jpg" 
		name = "HCMGIS Aerial Images"
		hcmgis_basemap(self.iface,service_url, name)
			
	###################################
	def wikimedia_call(self):
		service_url = "maps.wikimedia.org/osm-intl/{z}/{x}/{y}.png" 
		name = "Wikimedia Maps"
		hcmgis_basemap(self.iface,service_url, name)
	
	def wikimediahikebike_call(self):
		import requests
		import qgis.utils
		name = "Wikimedia Hike Bike"
		urlWithParams = 'tiles.wmflabs.org/hikebike/%7Bz%7D/%7Bx%7D/%7By%7D.png'
		rlayer = QgsRasterLayer(urlWithParams,name, 'wms') 
		if rlayer.isValid():    
			QgsProject.instance().addMapLayer(rlayer)
		
		sources = []
		service_uri1 ="tiles.wmflabs.org/hikebike/%7Bz%7D/%7Bx%7D/%7By%7D.png"
		sources.append(["connections-xyz",name,"","","",service_uri1,"","22","0"])
		for source in sources:
			connectionType = source[0]
			connectionName = source[1]
			QSettings().setValue("qgis/%s/%s/authcfg" % (connectionType, connectionName), source[2])
			QSettings().setValue("qgis/%s/%s/password" % (connectionType, connectionName), source[3])
			QSettings().setValue("qgis/%s/%s/referer" % (connectionType, connectionName), source[4])
			QSettings().setValue("qgis/%s/%s/url" % (connectionType, connectionName), source[5])
			QSettings().setValue("qgis/%s/%s/username" % (connectionType, connectionName), source[6])
			QSettings().setValue("qgis/%s/%s/zmax" % (connectionType, connectionName), source[7])
			QSettings().setValue("qgis/%s/%s/zmin" % (connectionType, connectionName), source[8])
		# Update GUI
		qgis.utils.iface.reloadConnections()
			
			

	##########################	
	def opendata(self):
		dialog = hcmgis_opendata_dialog(self.iface)
		dialog.exec_()
	
	# def opendevelopmentmekong(self):
	# 	dialog = hcmgis_opendevelopmentmekong_dialog(self.iface)
	# 	dialog.exec_()
	
	def geofabrik(self):
		dialog = hcmgis_geofabrik_dialog(self.iface)
		dialog.exec_()
	
	def gadm(self):
		dialog = hcmgis_gadm_dialog(self.iface)
		dialog.exec_()
	
		
	def covid19(self):
		import urllib.request
		import json
		import os 
		import qgis.utils
		from PyQt5.QtWidgets import QMessageBox
		uri_live_update = 'https://services1.arcgis.com/0MSEUqKaxRlEPj5g/arcgis/rest/services/Coronavirus_2019_nCoV_Cases/FeatureServer/2/query?where=1%3D1&outFields=*&outSR=4326&f=geojson'
		layer_name= 'global_covid19_live_update'
		json_name_live_update = os.path.join(os.getcwd(), layer_name + '.json')

		urllib.request.urlretrieve(uri_live_update, json_name_live_update)
		json_file_live_update  = QgsVectorLayer(json_name_live_update,layer_name,"ogr")

		if not json_file_live_update.isValid:
			QMessageBox.warning(None, "Invalid Layer", "Global COVID-19 Live Update Download failed!")
			return
		else:	
			QgsProject.instance().addMapLayer(json_file_live_update)					
	
	
	def covid19_timeseries(self):
		import urllib.request
		import os 
		import qgis.utils
		from PyQt5.QtWidgets import QMessageBox

		uri = ['https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_global.csv',
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_recovered_global.csv',
        'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_deaths_global.csv'
        ]
		layername = [
			'global_time_series_covid19_confirmed',
			'global_time_series_covid19_recovered',
			'global_time_series_covid19_deaths'
			]
		length = len(uri)
	
		from osgeo import ogr
		driver = ogr.GetDriverByName('ESRI Shapefile')
		driver.DeleteDataSource('path_to_your_shape.shp')

		for i in range(length):
			csv_name = os.path.join(os.getcwd(), layername[i] + '.csv')
			shapefile_name = os.path.join(os.getcwd(), layername[i] + '.shp')
			
			urllib.request.urlretrieve(uri[i], csv_name)
			hcmgis_csv2shp(csv_name, 'Lat', 'Long', shapefile_name)			
			covidlayer = QgsVectorLayer(shapefile_name, layername[i], "ogr")
			if not covidlayer.isValid():
				QMessageBox.warning(None, "Invalid Layer", layername[i] + ' download failed or Please remove Layers from Layers Panel before redownload!')			
			else:
				QgsProject.instance().addMapLayer(covidlayer)		
			#qgis.utils.iface.addVectorLayer(shapefile_name, layername[i],"ogr")
			

	def covid19_vietnam(self):
		uri_vietnam = 'https://opendata.hcmgis.vn/geoserver/geonode/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=geonode:covid_19_vietnam'
		
		vietnam = QgsVectorLayer(uri_vietnam, "Vietnam COVID-19 Live Update", "WFS")

		if not vietnam.isValid():
			QMessageBox.warning(None, "Invalid Layer", "Vietnam COVID-19 Live Update Download failed or Please remove Layers from Layers Panel before redownload!")	
			return		
		else:	
			QgsProject.instance().addMapLayer(vietnam)		
		
		
	def projections(self):
		dialog = hcmgis_customprojections_dialog(self.iface)
		dialog.exec_()
	

	def mergefield(self):
		dialog = hcmgis_merge_field_dialog(self.iface)
		dialog.exec_()
		
	def splitfield(self):
		dialog = hcmgis_split_field_dialog(self.iface)
		dialog.exec_()
		
			
	def medialaxis(self):
		dialog = hcmgis_medialaxis_dialog(self.iface)
		dialog.exec_()
	
	def centerline(self):
		dialog = hcmgis_centerline_dialog(self.iface)
		dialog.exec_()
	
	def closestpair(self):
		dialog = hcmgis_closestpair_dialog(self.iface)
		dialog.exec_()
	
	def lec(self):
		dialog = hcmgis_lec_dialog(self.iface)
		dialog.exec_()
			
		
	def merge(self):
		dialog = hcmgis_merge_dialog(self.iface)
		dialog.exec_()
	
	def split(self):
		dialog = hcmgis_split_dialog(self.iface)
		dialog.exec_()
	
	def fontconverter(self):
		dialog = hcmgis_font_convert_dialog(self.iface)
		dialog.exec_()	
	
	def formatconvert(self):
		dialog = hcmgis_format_convert_dialog(self.iface)
		dialog.exec_()

	def csv2shp(self):
		dialog = hcmgis_csv2shp_dialog(self.iface)
		dialog.exec_()
	
	def txt2csv(self):
		dialog = hcmgis_txt2csv_dialog(self.iface)
		dialog.exec_()
	
	def xls2csv(self):
		dialog = hcmgis_xls2csv_dialog(self.iface)
		dialog.exec_()
		

