from math import *
from random import *
import argparse

def get_points_from_file(file):
    '''
        Reads a csv file containing points and returns a list of tuples,
        one for each point
    '''
    lines = open('data/' + file, 'r').readlines()
    return [tuple(map(float, line.strip().split(','))) for line in lines]

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
        Takes a list of points and performs k-means clustering on them (k=3), then 
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
        print(f"Cluster {str(cluster_num)} is centred at {str(cluster_centers[cluster_num ])} and has {str(len(points_in_cluster))} points.")


if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('points_file', help='A csv file defining the points')
    parser.add_argument('--iters', action="store", help='Number of iterations to run k-means clustering')
    args = parser.parse_args()

    # Read in points from file
    points_file = args.points_file
    points = get_points_from_file(points_file)

    # Run clustering
    iterations = args.iters
    if iterations:
        cluster(points, int(iterations))
    else:
        cluster(points)