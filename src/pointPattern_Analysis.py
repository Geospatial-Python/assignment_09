#from . import pointPattern
#from . import point
import pysal as ps
import unittest
from src.point import Point
from src.pointPattern import PointPattern

#utilize the example shapefile
shapefile = ps.open(ps.examples.get_path('new_haven_merged.shp'))
dbf = ps.open(ps.examples.get_path('new_haven_merged.dbf'))
i = 0
for geometry, attributes in zip(shapefile,dbf):
    if i < 5:
        print(geometry,attributes)
    i = i +1

pointList = []
point_pattern = PointPattern()
for geometry,attributes in zip(shapefile,dbf):
    #create a list of points to then append to a pointPattern:
    point_pattern.add_point(Point(geometry[0],geometry[1],[attributes[0],attributes[1],attributes[2],attributes[3],attributes[4]])) #third parameters is a list of marks

#so now you have the points part of pointPattern, create an instance of pointPattern:

#add points to your self.points:
#for p in pointList:
 #       point_pattern.add_point(p)

#how many points have a nearest neighbor closer than the distance "band" step thing
    #okay, so now you actually have the data inside pointPattern's self.points. Now you can do some analysis:

    #illustrate the use of mean nearest neighbor on the entire dataset:
kd_avg_nn = point_pattern.kDTree_nearest_neighbor()
print("The new_haven_merged dataset has a total average nearest neighbor distance of: ", kd_avg_nn)

#illustrate the use of the mean nearest neighbor on a mark:
kd_avg_nn_mark = point_pattern.kDTree_nearest_neighbor(['animal-bites'])
print("The new_haven_merged dataset with the mark 'animal-bites' mark has a total average nearest neighbor distance of: ", kd_avg_nn_mark)

kd_avg_nn_mark2 = point_pattern.kDTree_nearest_neighbor(['animal-bites','assault-wdangerous-weapon'])
print("The new_haven_merged dataset with the mark 'animal-bites' and 'assault-wdangerous-weapon' marks has a total average nearest neighbor distance of", kd_avg_nn_mark2)


#ssssssillustrate the use of the g function:
np_compute_g = point_pattern.numpy_compute_g(12)
print("The new_haven_merged dataset's g function results are:")
for g in np_compute_g:
    print(g)

np_compute_g_mark  = point_pattern.numpy_compute_g(12,['animal-bites'])
print("The new_haven_merged dataset's g function results with a mark of 'animal-bites' are: ")
for g in np_compute_g_mark:
    print(g)

np_compute_g_mark2 = point_pattern.numpy_compute_g(12,['animal-bites','assault-wdangerous-weapon'])
print("The new_haven_merged dataset's g function results with a marks of 'animal-bites' and 'assault-wdangerous-weapon' are: ")
for g in np_compute_g_mark2:
    print(g)

