# -*- coding: utf-8 -*-

"""
/***************************************************************************
 RoadSlopeCalculator
                                 A QGIS plugin
 This algorithm is used to calculate the longitudinal slope of forest paths and roads, based on a 2D line vector layer and a DEM (Digital Elevation Model). 
It should not be used on national road systems, such as highways, motorways, national and regional roads, which have engineering works designed to smooth the slope (bridges, excavations, landfills, etc.), unless the user has access to a high precision Digital Surface Model (DSM).
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2021-03-09
        copyright            : (C) 2021 by Antonio Sobral Almeida
        email                : 66124.almeida@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

__author__ = 'Antonio Sobral Almeida'
__date__ = '2021-03-09'
__copyright__ = '(C) 2021 by Antonio Sobral Almeida'

# This will get replaced with a git SHA1 when you do a git archive

__revision__ = '$Format:%H$'

from qgis.core import QgsProcessingProvider
from .road_slope_calculator_algorithm import RoadSlopeCalculatorAlgorithm


class RoadSlopeCalculatorProvider(QgsProcessingProvider):

    def __init__(self):
        """
        Default constructor.
        """
        QgsProcessingProvider.__init__(self)

    def unload(self):
        """
        Unloads the provider. Any tear-down steps required by the provider
        should be implemented here.
        """
        pass

    def loadAlgorithms(self):
        """
        Loads all algorithms belonging to this provider.
        """
        self.addAlgorithm(RoadSlopeCalculatorAlgorithm())
        # add additional algorithms here
        # self.addAlgorithm(MyOtherAlgorithm())

    def id(self):
        """
        Returns the unique provider id, used for identifying the provider. This
        string should be a unique, short, character only string, eg "qgis" or
        "gdal". This string should not be localised.
        """
        return 'Road slope'

    def name(self):
        """
        Returns the provider name, which is used to describe the provider
        within the GUI.

        This string should be short (e.g. "Lastools") and localised.
        """
        return self.tr('Road slope')

    def icon(self):
        """
        Should return a QIcon which is used for your provider inside
        the Processing toolbox.
        """
        return QgsProcessingProvider.icon(self)

    def longName(self):
        """
        Returns the a longer version of the provider name, which can include
        extra details such as version numbers. E.g. "Lastools LIDAR tools
        (version 2.2.1)". This string should be localised. The default
        implementation returns the same string as name().
        """
        return self.name()