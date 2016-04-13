
from point import Point
import analytics
import utils
import random
import numpy as np
import scipy.spatial as ss
import pysal as ps

class PointPattern(object):
    def __init__(self):
        self.points = []

    def add_point(self, point):
        self.points.append(point)

    def remove_point(self, index):
        try:
            del(self.points[index])
        except:
            pass

    def average_nearest_neighbor_distance(self, mark=None):
        return analytics.average_nearest_neighbor_distance(self.points, mark)


    def average_nearest_neighbor_distance_kdtree(self, mark=None):
        pointsWithMark = list()
        pointsWithoutMark = list()

        for p in self.points:
            if mark != None:
                if p.mark == mark:
                    pointsWithMark.append(p.getPoint())
            else:
                pointsWithoutMark.append(p.getPoint())

        nn_distances = list()
        if len(pointsWithMark) > 0:
            for p in pointsWithMark:
                kdtree = ss.KDTree(pointsWithMark)
                nearest_neighbor_distance = kdtree.query(p, k = 2)
                nn_distances.append(nearest_neighbor_distance[1])
            nn_distances = np.array(nn_distances)
            return np.mean(nn_distances)
        else:
            for p in pointsWithoutMark:
                kdtree = ss.KDTree(pointsWithoutMark)
                nearest_neighbor_distance = kdtree.query(p, k = 2)
                nn_distances.append(nearest_neighbor_distance[1])
            nn_distances = np.array(nn_distances)
            return np.mean(nn_distances)

    def average_nearest_neighbor_distance_numpy(self, mark=None):
        point_coords = []
        if mark != None:
            for point in self.points:
                if point.getMark() == mark:
                    point_coords.append(point.getPoint())
        else:
            for point in self.points:
                point_coords.append(point.getPoint())

        point_array = np.array(point_coords)
        nneighbors = []
        temp = None
        for i, coord_i in enumerate(point_array):
            for j, coord_j in enumerate(point_array):
                if i == j:
                    continue
                dist = ss.distance.euclidean(coord_i, coord_j)
                if temp is None:
                    temp = dist
                elif temp > dist:
                    temp = dist
            nneighbors.append(temp)
            temp = None
        return np.mean(nneighbors)


    def num_of_coincident(self):
        numCoin = 0
        accounted = []


        for i in range(len(self.points)):
            for j in range(len(self.points)):
                if i in accounted:
                    continue
                if i == j:
                    continue
                if self.points[i] == self.points[j]:
                    numCoin += 1
                    accounted.append(j)

        return numCoin

    def list_marks(self):
        marks = []
        for point in self.points:
            if point.mark != None and point.mark not in marks:
                marks.append(point.mark)
        return marks

    def find_subset_with_mark(self, mark):
        marked_points = []
        for points in self.points:
            if points.mark == mark:
                marked_points.append(points)
        return marked_points

    def generate_random_points(self, n=None):
        if n is None:
            n = len(self.points)
        rndmPoints = []
        self.marks = ['burrito', 'chimichanga', 'steak', 'burger', 'chillidog',
                 'sweetpotatofries', 'beans', 'bacon', 'beijingbeef', 'friedeggs',
                 'icecream', 'brownies', 'cookie', 'bananasplit', 'almondjoy']

        for i in range(n):
            rndmPoints.append(Point(round(random.random(), 2), round(random.random(), 2), random.choice(self.marks)))
        return rndmPoints

    def generate_realizations(self, k):
        return utils.permutations(k)

    def get_critical_points(self):
        return analytics.compute_critical(self.generate_realizations(100))

    def compute_g(self, nsteps):
        discStep = np.linspace(0, 1, nsteps)
        sum = 0
        for i in range(nsteps):
            i_step = discStep[i]
            minDist = -1
            for j in range(len(discStep)):
                if i == j:
                    continue
                if minDist == -1:
                    minDist = np.abs(discStep[j] - i_step)
                else:
                    if abs(discStep[j] - i_step) < minDist:
                        minDist = np.abs(discStep[j] - i_step)
                    else:
                        minDist = minDist
            sum += minDist

        return sum / nsteps

    def generate_random_points_domain(self, count = 2, maxRange = 1, minRange = 0, seed = None):
        self.marks = ['burrito', 'chimichanga', 'steak', 'burger', 'chillidog',
                 'sweetpotatofries', 'beans', 'bacon', 'beijingbeef', 'friedeggs',
                 'icecream', 'brownies', 'cookie', 'bananasplit', 'almondjoy']
        randomPoints = []
        if seed is None:
            rng = np.random()
        else:
            rng = np.random.RandomState(seed)
            random.seed(seed)
        coord = rng.uniform(minRange, maxRange, (count, 2))
        for i in range(len(coord)):
            randomPoints.append(Point(coord[i][0], coord[i][1], mark = random.choice(self.marks)))
        return randomPoints
