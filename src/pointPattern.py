import random
import math
from . import point
from . import analytics
from . import utils
import numpy as np
import scipy.spatial as ss


class PointPattern(object):
    #initialize to list of points
    def __init__(self):
        self.points = []
        self.marks = ['lavender','orange','rose','ash','violet','magenta','cerulean']

    def add_point(self,point):
        self.points.append(point)

    def remove_point(self,index):
        del(self.points[index])

    def average_nearest_neighbor(self,mark=None):
        return analytics.average_nearest_neighbor_distance(self.points,mark)

    #find the number of coincident points
    def coin_count(self):
        count = 0
        clist = []
        for num1, point1 in enumerate(self.points):
            for num2, point2 in enumerate(self.points):
                #check that you're not comparing the same point
                if num1 != num2 and num2 not in clist: # if they are not the same point, and already counted
                    if point1 == point2:
                        count = count +1
                        clist.append(num2)
        return count

    #creating a point pattern for each of the 99 times.
    def create_pointPattern(self):
        point_pat = PointPattern()
        #Point(random.uniform(-72.8,-72.999),random.uniform(41.2,41.3999),random.choice(marks))
        for x in range(13): #create 13 points, like the pointPattern you are checking it against
            point_pat.add_point(point.Point(random.uniform(-72.8,-72.99),random.uniform(41.2,41.3999)))

        #return the pointPattern that you created
        return point_pat

    #list all the different marks
    def mark_list(self):
        markList = []

        #go through each point and add a new mark to the mark listss
        for point in self.points:
            if point.mark not in markList:
                markList.append(point.mark)
        return markList

    #return a subset of point by mark type
    def mark_subset(self,mark):
        subset = []
        for p in self.points:
            if p.mark == mark:
                subset.append(p)
        return subset

    #where n is either provided by the user or equal to the current size of pointPattern
    def create_n_random_points(self,n =None):
        randomPoints = []
        if(n is None):
            n = len(self.points)

        for i in range(n):
            randomPoints.append(point.Point(random.randint(1,100),random.randint(1,100),random.choice(self.marks)))

        return randomPoints

    #simulate k random points patterns for Monte Carlo
    def create_k_patterns(self,k):
        return analytics.permutation_nearest_distance(self.marks,k)

    def critical_points(self):
        return analytics.critical_points(self.create_k_patterns(99))
        #return analytics.critical_points(self.points)

    def g_critical_points(self,distBands):
        #99 times, create a point pattern:
        first = True
        for y in range(99):
            point_pat = PointPattern()
            for x in range(13): #create 12 points, like the pointPattern you are checking it against
                point_pat.add_point(point.Point(random.uniform(-72.8,-72.99),random.uniform(41.2,41.3999)))

            #once you've created that point pattern, get the g function value of that point pattern:
            gList = point_pat.numpy_compute_g(12,None,distBands) #created a list like [1,2,3,4,5,5,66,,7,8], want to make a matrix with that
            #create a "matrix" with that stuff:
            if first:
                g_array = gList
                first = False
            else:
               # g_array = np.vstack(g_array,gList)
                g_array = np.vstack((g_array,gList))

        #after 99 times of that, you have a 99 x 12 matrix,
        #find the min and max of each column:
        min_arrayi = g_array.argmin(0)
        max_arrayi = g_array.argmax(0)

        min_array = []
        max_array = []

        #now min_array and max_array hold the min and max indices for
        #each column.
        i = 0 # the column index for g_array:
        k = 0
        #i'm given how far down I should go, not how far accross I should go
        #I'm given what row the min is on
        for minindex in min_arrayi:
            #the first time, i =0, and you also want to get stuff from row 0:
            #g[i] = [1,2,3,4,5]
            min_val = g_array[minindex][i]
            min_array.append(min_val)
            i = i + i #so the next time, you're go to the minindex row and go to the 1st column

        for maxindex in max_arrayi:
            max_val = g_array[maxindex][k]
            max_array.append(max_val)
            k = k + 1


        return min_array,max_array,g_array


    def compute_g(self,nsteps,mark=None):
        """

        Parameters
        ----------
        nsteps: The numer of discrete d that are used to compute G(d)

        Returns
        -------

        """
        point_array = []
        if not mark:
            for p in self.points:
                point_array.append(p.return_array())
        else:
            #that means a mark(s) was passed in
            for p in self.points:
                if p.mark in mark:
                    point_array.append(p.return_array())
        shDistL = [] # list keeps track of all the nearest neighbor distances for each point
        gFuncL = []
        #for pointPattern range 0-5, the highest distance between them is < 8
        ds = np.linspace(0,8,nsteps)
        sums = 0
        N = np.point_array.size() #get a count of how many points there are
        for dstep in ds:          #for every distance band dstep
            for num1, p in enumerate(point_array):
                shortestDistance = math.inf
                for num2, dp in enumerate(point_array):
                    if num1 != num2: #if they aren't the same point, find the distance between the two points
                        p1 = (p.x,p.y)
                        p2 = (dp.x,dp.y)
                        dist = utils.euclidean_distance(p1, p2)
                        if(shortestDistance > dist):
                            shortestDistance = dist
                #now add the shortest distance of that point before it moves on to a new point
                shDistL.append(shortestDistance)
            #now you have the minimum nearest neighbor distances of each point stored in shDistL.
            #Check how many of those distances are less than the current distance band:
            for d in shDistL:
                count = 0
                if d < dstep: #then it should be included in the count
                    count = count + 1
            #now I've got the count, compute the g function:
            gFuncL.append(count/N)
        return gFuncL


#utilize a scipy.spatial.KDTree to compute the nearest neighbor distance

    def kDTree_nearest_neighbor(self,mark=None):
        point_array = [] # is the "tuple" that holds the arrays to be stacked
        if not mark:
            #then you dont want to look for a specific mark, and you can just find the average nearest neighbor of everything
            for p in self.points:            #add every point to the point_array
                point_array.append(p.return_array())
        else:
            #that means that there was something passed into mark and you have to only computer the nearest neighbor with that mark
            for p in self.points:
                for m in mark: # passed in a possible list of marks
                    if m in p.mark:
                        point_array.append(p.return_array())
                        break #so that you don't add duplicates if it has both marks for example

        #now you have the vstack parameter:
        point_ndarray = np.vstack(point_array)

        #now you have the ndarray needed for kdtree, create your tree:
        kdTree = ss.KDTree(point_array)

        #now computer the nearest neighbors:
        nn_dist = []
        for p in point_ndarray:
            nearest_neighbor_distance, nearest_neighbor_point = kdTree.query(p,k=2)
            nn_dist.append(nearest_neighbor_distance[1]) #appending the second one to allow for self-neighbor

        average = np.mean(nn_dist)
        return average

    #compute the nearest neighbor distance using numpy (ndarray and mean)
    def numpy_nearest_neighbor(self,mark=None):
        shDistL = []
        point_array = []
        if not mark:
            for p in self.points:
                point_array.append(p.return_array())
        else:
            #that means a mark was passed in
            for p in self.points:
                if mark in p.mark:
                    point_array.append(p.return_array())

        #point_array = [ [1,2],[3,4],[5,6],[7.8] ]
        #using the same logic that's in analytics:
        for num1, p in enumerate(point_array):    # p = [1,2]
            shortestDistance = math.inf
            for num2, dp in enumerate(point_array):
                if num1 != num2:
                    dist = ss.distance.euclidean(p,dp)
                    if(shortestDistance > dist):
                        shortestDistance = dist
            #now add the shortest distance of that point before it moves on to a new point:
            shDistL.append(shortestDistance)
        mean_d = np.mean(shDistL) #returns the average of the array of elements, so pass in shDistL

        return mean_d

    #compute the G function using numpy
    def numpy_compute_g(self,nsteps,mark=None,distBands=None):
        point_array = []

        if not mark:
            for p in self.points:
                point_array.append(p.return_array())
        else:
            #that means a mark(s) was passed in
            for p in self.points:
                for m in mark:
                    if m in p.mark:
                        point_array.append(p.return_array())
                        break # so that you don't add duplicates if it has both marks for example
        shDistL = [] # list keeps track of all the nearest neighbor distances for each point
        gFuncL = []

        #first get the nearest neighbor distance for each point:
        for num1, p in enumerate(point_array):
            shortestDistance = math.inf
            for num2, dp in enumerate(point_array):
                if num1 != num2:
                #    print(p)
                #    print(dp)
                #    p1 = (p.x,p.y)
                #    p2 = (dp.x,dp.y)
                #    dist = utils.euclidean_distance(p1, p2)
                    dist = ss.distance.euclidean(p,dp)
                    if(shortestDistance > dist):
                            shortestDistance = dist
            shDistL.append(shortestDistance)
           # print("the shortest distance: ",shortestDistance)
        #now you have the minimum nearest neighbor distances of each point stored in shDistL.
        #use that to compute the steps:
        if distBands is None:
            min = np.amin(shDistL)
            max = np.amax(shDistL)*1.5 #so that the last max distance on the g function will fall under a distance band just a little bit larger.
            ds = np.linspace(min,max,nsteps)
        else:
            ds = distBands
            min = np.amin(ds)
            max = np.amax(ds)
            ds = np.linspace(min,max,nsteps)
        N = np.size(point_array) #get a count of how many points there are

        #now calculate the g function for every distance band:
        for dstep in ds:
            count = np.where(shDistL < dstep)
            count = len(count[0])
            #now you have the count of observations under that distance band.
            #divide by N and add it to the gFuncL.
            gFuncL.append(count/N)
        return gFuncL, ds


    #Generate random points within some domain
    def random_points_domain(self,numPoints = 2,start=0,stop=1,seed =None):
        randomp = None
        pointsList = []
        if seed is None: #meaning no passed in starting value
            randomp = np.random
        else:
            randomp = np.random.RandomState(seed) #instantiate seed
            random.seed(seed)
        points = randomp.uniform(start,stop, (numPoints,2))    #create ndarray
        for x in range(points): #for all the points
            pointsList.append(point.Point(points[x][0],points[x][1],np.random.choice(self.marks)))
        return pointsList






