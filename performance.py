from random import *

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


print(generate_random_points(10))