from math import *
from random import *
import argparse
import numpy as np

def get_points_from_file(file):
    '''
        Reads a csv file containing points and returns a list of tuples,
        one for each point
    '''
    lines = open("data/" + file, 'r').readlines()
    points = [tuple(map(float, line.strip().split(','))) for line in lines]
    numpy_array = np.array(points)
    return numpy_array

def distance_between_points(pt1, pt2):
    '''
        Takes 2 points, pt1 and pt2, and returns the distance between them
    '''
    return np.sqrt((pt1[0]-pt2[0])**2 + (pt1[1]-pt2[1])**2)


def cluster(points, iterations=10):
    '''
        Takes a list of points and performs k-means clustering on them (k=3), then 
        prints out the cluster centers and number of points in each cluster
    '''
    k=3
    cluster_centers = np.array([points[randrange(len(points))], points[randrange(len(points))], points[randrange(len(points))]])
    cluster_num_allocations = [None]*len(points)

    for _ in range(iterations):
        distances_to_clusters = [None] * k
        distances_to_clusters[0] = np.linalg.norm(cluster_centers[0] - points, axis=1)
        distances_to_clusters[1] = np.linalg.norm(cluster_centers[1] - points, axis=1)
        distances_to_clusters[2] = np.linalg.norm(cluster_centers[2] - points, axis=1)
        cluster_num_allocations = np.argmin(distances_to_clusters, axis=0)

        for cluster_num in range(k):
            points_in_cluster = points[cluster_num_allocations == cluster_num]

            # If no points in cluster do not change the cluster center
            if len(points_in_cluster) > 0:
                new_mean = np.mean(points_in_cluster, axis=0)
                cluster_centers[cluster_num] = new_mean

    
    for cluster_num in range(k):
        points_in_cluster = points[cluster_num_allocations == cluster_num]
        print(f"Cluster {str(cluster_num)} is centred at {str(cluster_centers[cluster_num ])} and has {str(len(points_in_cluster))} points.")


if __name__ == '__main__':
    # Parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('points_file', help='A csv file defining a list of x and y coordinates of points')
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
