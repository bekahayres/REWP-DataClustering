import json 
from clustering import cluster

def read_json_file(file):
    '''
        Takes a json filename and returns a python dictionary of contents
    '''
    with open(file) as json_file:
        return json.load(json_file)

def combine_cities_libraries(cities, libraries):
    '''
        Takes list of cities and libraries and reaturn a dict of the format
        {
            city_name: {
                population: xxxx,
                books: xxxx
            },
            ...
        }
    '''
    combined_data = {}
    for city in cities:
        city_name = city['name']
        combined_data[city_name] = {}
        books_num = sum([library['books'] for library in libraries if library['city'] == city_name ])
        combined_data[city_name]['population'] = city['population']
        combined_data[city_name]['books'] = books_num
    
    return combined_data

def get_points_for_clustering(data):
    '''
        Takes combined city and libray data and returns list of tuples
        of population and books suitable for point clustering
    '''
    points_for_clustering = []
    for city in data.keys():
        pop = data[city]['population']
        books = data[city]['books']
        points_for_clustering.append((pop, books))

    return points_for_clustering

def write_data_to_file(json_data, filename):
    '''
        writes a python dictionary to a json file 
    '''
    with open(filename, 'w') as outfile:
        json.dump(json_data, outfile)

if __name__ == '__main__':
    # Read data 
    cities = read_json_file('data/cities.json')
    libraries = read_json_file('data/libraries.json')

    # Combine data and get points for clustering 
    combined_data = combine_cities_libraries(cities, libraries)

    # Write to file 
    write_data_to_file(combined_data, 'combined.json')

    # Get points for clustering
    points_for_clustering = get_points_for_clustering(combined_data)

    # Run (non numpy) clustering 
    cluster(points_for_clustering, iterations=20)



