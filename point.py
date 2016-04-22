import analytics

import math
import random

import numpy as np
import scipy.spatial as ss
import pysal as ps

class Point:

    def __init__(self, x = 0, y = 0, mark = ''):
        self.x = x
        self.y = y
        self.mark = mark

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __radd__(self, other):
        return Point(self.x + other, self.y + other)

    def check_coincident(self, b):

        if b.x == self.x and b.y == self.y:
            return True

    def shift_point(self, x_shift, y_shift):

        self.x += x_shift
        self.y += y_shift
    
    def to_array(self):
        return [self.x, self.y]

class PointPattern(object):
    
    def __init__(self):
        self.points = []

    def __len__(self):
        count = 0
        for item in self.points:
            count += 1
        return count

    def add_point(self, point):
        self.points.append(point)

    def remove_point(self, index):
        del(self.points[index])

    def average_nearest_neighbor(self, mark=None):
        return analytics.average_nearest_neighbor_distance(self.points, mark)

    def average_nearest_neighor_KDTree(self, mark=None):
        nn_distances = []
        points_to_measure = []
        ps2m = []

        if mark is not None:
            points_to_measure = self.points_by_mark(mark)
        else:
            points_to_measure = self.points

        for p in points_to_measure:
            ps2m.append((p.x, p.y))

        treeKD = ss.KDTree(ps2m)

        for p in ps2m:
            nearest_neighbor_d, nearest_neighbor = treeKD.query(p, k=2)
            nn_distances.append(nearest_neighbor_d[1])

        nn_distances = np.array(nn_distances)
        return np.mean(nn_distances)

    def average_nearest_neighbor_ndarray(self, mark=None):
        points_arrays = []

        for item in self.points:
            if item.mark is mark:
                points_arrays.append(item.to_array())
        stacked_array = np.array(points_arrays)

        dists = []
        for num1, point in enumerate(stacked_array):
            dists.append(None) 
            for num2, point2 in enumerate(stacked_array):
                if num1 is not num2:
                    new_dist = ss.distance.euclidean(point, point2)
                    if dists[num1] == None:
                        dists[num1] = new_dist
                    elif dists[num1] > new_dist:
                        dists[num1] = new_dist
        return np.mean(dists)

    def count_coincident(self):
        counted = []
        count = 0
        for index, point in enumerate(self.points):
            for index2, point2 in enumerate(self.points):
                if index != index2:
                    if point.check_coincident(point2) is True:
                        count += 1
        return count

    def list_marks(self):
        marks = []
        for point in self.points:
            if point.mark not in marks and point.mark is not None:
                marks.append(point.mark)
        return marks
                
    def points_by_mark(self, mark=None):
        points_to_return = []
        for point in self.points:
            if point.mark == mark:
                points_to_return.append(point)
        return points_to_return

    def generate_random_points(self, n = None, marks = None):
        if n is None:
            n = len(self.points)
        point_list = analytics.create_random_marked_points(n, marks)
        return point_list

    def numpy_point_generator(self, low=0, high=1, n = 100):
        nparray = np.random.uniform(low, high, (n, 2))
        point_list = []
        marks = ['black','white','ying','yang']
        for index in range(len(nparray)):
            point_list.append(Point(nparray[index][0], 
                nparray[index][1], random.choice(marks)))
        return point_list

    def generate_realizations(self, p = 99, marks = None):
        neighbor_perms = []
        for i in range(p):
            neighbor_perms.append(
                    analytics.average_nearest_neighbor_distance(
                        self.generate_random_points(100)))
        return neighbor_perms
           
    def get_critical(neighbor_perms):
        return max(neighbor_perms), min(neighbor_perms)

    def comupte_g(self, nsteps):
        ds = np.linspace(0, 1, nsteps)
        dist_counts = []
        for i, d in enumerate(ds):
            min_dist = None
            for n in range(nsteps):
                if n != i:
                    if min_dist is None or min_dist > d:
                        min_dist = d
            dist_counts.append(min_dist)
        dist_counts = np.array(dist_counts)
        return np.sum(dist_counts)/nsteps

    


