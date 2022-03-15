from password import USERNAME, PASSWORD
import logging
import os
from osgeo import gdal
#import matplotlib.pyplot as plt
from sentinelloader import Sentinel2Loader
from shapely.geometry import Polygon

sl = Sentinel2Loader('./data_path',
                    USERNAME, PASSWORD,
                    apiUrl='https://scihub.copernicus.eu/dhus/', showProgressbars=True, cloudCoverage=(0,80), loglevel=logging.DEBUG)

# area = Polygon([(4.57, 5.82), (4.57, 10.00),
#         (-1.00, 5.82), (-1.00, 10.00)])
#lt, rt
#ll rl
# area = Polygon([(2.2, 9.85), (3.2, 9.85),
#         (3.2, 9), (9, 2.2)])
#rt, rl, ll, lt
# area = Polygon([(3.2, 9.85), (9, 2.2),
#          (3.2, 9), (2.2, 9.85)])
#ll, lt, rt, rl
# area = Polygon([(3.2, 9), (2.2, 9.85),
#          (3.2, 9.85), (9, 2.2)])
area = Polygon([(8, 1), (8, 2), (10, 2), (10, 1)])
geoTiffs = sl.getRegionHistory(area, 'TCI', '60m', '2021-12-20', '2022-01-30', daysStep=1)
for geoTiff in geoTiffs:
    print('Desired image was prepared at')
    print(geoTiff)
    os.remove(geoTiff)


def getRegionHistory(self, geoPolygon, bandOrIndexName, resolution, dateFrom, dateTo, daysStep=5, ignoreMissing=True,
                     minVisibleLand=0, visibleLandPolygon=None, keepVisibleWithCirrus=False,
                     interpolateMissingDates=False):
    """Gets a series of GeoTIFF files for a region for a specific band and resolution in a date range. It will make the best effort to get images near the desired dates and filter out images that have poor land visibility due to cloudy days"""