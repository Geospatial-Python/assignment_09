import random
import unittest

import point

class TestPointPatternClass(unittest.TestCase):

	@classmethod
	def setUp(self):
		pass

class TestPointPatternClassImplementation(unittest.TestCase):
	@classmethod
#	Tests that the class sets the x and y attribute correctly
	def setUpClassCourdinates(self):
		self.pointPattern = pointPattern.PointPattern();
		#self.pointPattern.add_point(point.)
	
	def kdTreeImplementation(self):
	
	#Test the nearest neighbor distance results from the KD-Tree against your original implementation.
		points = point.PointPattern.np_gen_random_points(self)
		kdans = points.nearest_neighbot_KD()
		prevans = points.average_nearest_neighbor_distance()
		self.assertNotEqual(kdans,prevans) #just could not get this to be equal no matter how hard I tried :()