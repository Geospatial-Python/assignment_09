from point import PointPattern
import pysal as ps
import point
from plistlib import Plist

# Open the shapefile using the example above and read in the points
# attributes[1], in the above example, is the mark
shapefile = ps.open(ps.examples.get_path('new_haven_merged.shp'))
dbf = ps.open(ps.examples.get_path('new_haven_merged.dbf'))

#empty list of soon to be points

pList = []

for geometry, attributes in zip(shapefile, dbf):
    pList.append(point.Point(geometry[0],geometry[1], attributes[1]))
    #print(attributes[4])
    
#print(pList[1].mark)

pattern = PointPattern()

for p in pList:
    pattern.add_point(p)
    
# Run a few tests to explore the dataset.
nn = PointPattern.nearest_neighbor_KD(pattern)
print('This interesting mark has a nearest neighbor distance of {}'.format(nn))
    


# Use your monte carlo simulation code to see if the result is statistically significant
smallest, largest = pattern.critical_points()
# 
# print(smallest)
# 
if pattern.check_significant(smallest, largest, nn):
     print('The mark is significant.')
else:
     print('The mark is not significant.')




