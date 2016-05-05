import unittest

from .. import pointPattern
from .. import point


class TestPointPattern(unittest.TestCase):
    def setUp(self):
        #initilize points into point pattern
        self.pointPattern = pointPattern.PointPattern() #create list
        #now add points into that list
        self.pointPattern.add_point(point.Point(1,1,'lavender'))
        self.pointPattern.add_point(point.Point(2,2,'orange'))
        self.pointPattern.add_point(point.Point(2,4,'orange'))
        self.pointPattern.add_point(point.Point(1,5,'ash'))
        self.pointPattern.add_point(point.Point(3,3,'rose'))
        self.pointPattern.add_point(point.Point(3,2,'rose'))
        self.pointPattern.add_point(point.Point(4,4,'ash'))
        self.pointPattern.add_point(point.Point(5,5,'violet'))
        self.pointPattern.add_point(point.Point(1,1,'lavender'))
        self.pointPattern.add_point(point.Point(1,1,'lavender'))
        self.pointPattern.add_point(point.Point(1,1,'lavender'))

    def test_coin(self):
        self.assertEqual(self.pointPattern.coin_count(),4)

    def test_markList(self):
        check = True
        list = self.pointPattern.mark_list()
        for l in list:
            if l not in ['lavender','orange','rose','ash','violet']:
                check = False
        self.assertTrue(check)
        #self.assertEqual(self.pointPattern.mark_list(),['lavender','orange','rose','ash','violet'])

    def test_mark_subset(self):
        m1 = self.pointPattern.mark_subset('lavender')
        m2 = self.pointPattern.mark_subset('violet')
        self.assertEqual(len(m1),4)
        self.assertEqual(len(m2),1)

    def test_random_points(self):
        #check with user passed n
        l1 = self.pointPattern.create_n_random_points(5)
        self.assertEqual(len(l1),5)

        l2 = self.pointPattern.create_n_random_points()
        self.assertEqual(len(l2),11)

    def test_k_realizations(self):
        self.assertEqual(len(self.pointPattern.create_k_patterns(10)),10)

  #  def test_g_function(self):
  #      self.assertAlmostEqual(self.pointPattern.compute_g(10), 0.111, places=3)
   #     self.assertAlmostEqual(self.pointPattern.compute_g(50), 0.020, places=3)
    #    self.assertAlmostEqual(self.pointPattern.compute_g(100), 0.010, places=3)

#    def test_g_function_numpy(self):
 #       self.assertAlmostEqual(self.pointPattern.numpy_compute_g(10), 0.111, places=3)
  #      self.assertAlmostEqual(self.pointPattern.numpy_compute_g(50), 0.020, places=3)
   #     self.assertAlmostEqual(self.pointPattern.numpy_compute_g(100), 0.010, places=3)

    #Test the nearest neighbor distance results from the KD-Tree against your original implementation.
    def test_kdtree_nearest_neighbor(self):
        #returns the average nearest neighbor distance for the points in the pointPattern, computed once.
        dist1 = self.pointPattern.average_nearest_neighbor()
        dist2 = self.pointPattern.kDTree_nearest_neighbor() #both of these take self.points
        self.assertEqual(dist1,dist2)

        #now check that the numpy average nearest neighbor is working properly too:
        dist3 = self.pointPattern.numpy_nearest_neighbor()#also uses self.points
        self.assertEqual(dist1,dist3)