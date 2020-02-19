from math import *
from random import *


def get_points_from_file(file):
    '''
        Reads a csv file containing points and returns a list of tuples,
        one for each point
    '''
    lines = open(file, 'r').readlines()
    points=[]
    for line in lines:
        points.append(tuple(map(float, line.strip().split(','))))
    return points

def mean_point(pts):
    '''
        Takes list of points, pts and returns the mean point coordinates
    '''
    mean_x = sum([pt[0] for pt in pts]) / len(pts)
    means_y = sum([pt[1] for pt in pts]) / len(pts)

    return (mean_x, means_y)
    

def distance_between_points(pt1, pt2):
    '''
        Takes 2 points, pt1 and pt2, and returns the distance between them
    '''
    return sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)


def cluster(points, iterations=10):
    '''
        Takes a list of points and performs clustering on them, then 
        prints out the cluster centers and number of points in each cluster
    '''

    k=3
    cluster_centers=[points[randrange(len(points))], points[randrange(len(points))], points[randrange(len(points))]]
    cluster_num_allocations=[None]*len(points)

    for _ in range(iterations):
        for point_index in range(len(points)):
            point = points[point_index]
            distances_to_clusters = [None] * k
            distances_to_clusters[0] = distance_between_points(point, cluster_centers[0])
            distances_to_clusters[1] = distance_between_points(point, cluster_centers[1])
            distances_to_clusters[2] = distance_between_points(point, cluster_centers[2])
            cluster_num_allocations[point_index] = distances_to_clusters.index(min(distances_to_clusters))
        for cluster_num in range(k):
            points_in_cluster=[point for j, point in enumerate(points) if cluster_num_allocations[j] == cluster_num]
            new_mean = mean_point(points_in_cluster)
            cluster_centers[cluster_num]=new_mean


    for cluster_num in range(k):
        points_in_cluster=[point for j, point in enumerate(points) if cluster_num_allocations[j] == cluster_num]
        print("Cluster " + str(cluster_num) + " is centred at " + str(cluster_centers[cluster_num ]) + " and has " + str(len(points_in_cluster)) + " points.")


points = get_points_from_file('data/samples.csv')
cluster(points)