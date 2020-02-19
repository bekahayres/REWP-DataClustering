from math import *
from random import *

k=3

lines = open('data/samples.csv', 'r').readlines()
points=[]
for line in lines: points.append(tuple(map(float, line.strip().split(','))))

cluster_centers=[points[randrange(len(points))], points[randrange(len(points))], points[randrange(len(points))]]

cluster_num_allocations=[None]*len(points)
iteration_num=0
while iteration_num<10:
  for point_index in range(len(points)):
    point = points[point_index]
    distances_to_clusters = [None] * 3
    distances_to_clusters[0] = sqrt((point[0]-cluster_centers[0][0])**2 + (point[1]-cluster_centers[0][1])**2)
    distances_to_clusters[1] = sqrt((point[0]-cluster_centers[1][0])**2 + (point[1]-cluster_centers[1][1])**2)
    distances_to_clusters[2] = sqrt((point[0]-cluster_centers[2][0])**2 + (point[1]-cluster_centers[2][1])**2)
    cluster_num_allocations[point_index] = distances_to_clusters.index(min(distances_to_clusters))
  for cluster_num in range(3):
    points_in_cluster=[point for j, point in enumerate(points) if cluster_num_allocations[j] == cluster_num]
    new_mean=(sum([point[0] for point in points_in_cluster]) / len(points_in_cluster), sum([point[1] for point in points_in_cluster]) / len(points_in_cluster))
    cluster_centers[cluster_num]=new_mean
  iteration_num=iteration_num+1

for cluster_num in range(3):
  points_in_cluster=[point for j, point in enumerate(points) if cluster_num_allocations[j] == cluster_num]
  print("Cluster " + str(cluster_num) + " is centred at " + str(cluster_centers[cluster_num ]) + " and has " + str(len(points_in_cluster)) + " points.")