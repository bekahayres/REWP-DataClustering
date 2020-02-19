import timeit
import matplotlib.pyplot as plt
import numpy as np

from random import *
from clustering import cluster as plain_cluster
from clustering_numpy import cluster as numpy_cluster


def generate_random_points(n):
    '''
        Generate n random points, used to pass variable point numbers to
        clustering to measure time. Coordinates are randomly drawn from 
        -10 to 10, with 5 decimal places to match samples.csv

        This saves having to make lots of files with different numbers of points in
    '''
    limit = 1000000
    div = 100000.0
    points = []
    for i in range(n):
        points.append((randrange(-limit, limit) / div, randrange(-limit, limit) / div))
    return points


times_plain = []
times_numpy = []
point_nums = []

# Increment points 50 at a time to keep execution time down 
for point_num in range(100, 10000, 50):
    points = generate_random_points(point_num)

    # Numpy cluster function expects a numpy array as input
    points_numpy = np.array(points)

    # Take average for 10 runs 
    time_plain = timeit.timeit(lambda: plain_cluster(points, iterations=10), number=10) / 10.0
    time_numpy = timeit.timeit(lambda: numpy_cluster(points_numpy, iterations=10), number=10) / 10.0

    times_plain.append(time_plain)
    times_numpy.append(time_numpy)

    point_nums.append(point_num)

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_title("Compare performance of plain python and numpy implementations\nof k-means clustering", fontsize=11)

# Plot both lines on same axis
ax.plot(point_nums, times_plain, label='Plain clustering')
ax.plot(point_nums, times_numpy, label='Numpy clustering')
ax.legend()
ax.set_xlabel("Number of points", fontsize=11)
ax.set_ylabel("Execution time (s)", fontsize=11)
fig.savefig('performance.png')
