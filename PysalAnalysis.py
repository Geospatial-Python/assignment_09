from point_pattern import PointPattern
import pysal as ps
import random
"""
pysal "examples" gives an error
 
"""
shapefile = ps.open(ps.examples.get_path('new_haven_merged.shp'))
#dbf = ps.open(ps.examples.get_path('new_haven_merged.dbf'))
random.seed(12345)


nn = PointPattern.nearest_neighbor_KD(pattern)
print('This interesting mark has a nearest neighbor distance of {}'.format(nn))