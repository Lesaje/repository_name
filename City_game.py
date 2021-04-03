'''
The program reads a set of cities from a cities.txt file
Cities must start and end with a lowercase letter
After that, it displays all possible sequences that satisfy the condition
the last letter of the current word matches the first letter of the previous
'''

def iter_paths(adj, min_length=2, path=None):
    if not path:
        for start_node in range(len(adj)):
            yield from iter_paths(adj, min_length, [start_node])
    else:
        if len(path) >= min_length:
            yield path
        if path[-1] in path[:-1]:  
            return
        current_node = path[-1]
        for next_node in range(len(adj[current_node])):
            if adj[current_node][next_node] == 1:
                yield from iter_paths(adj, min_length, path + [next_node])

FILE_INPUT_NAME = 'cities.txt'
FILE_OUTPUT_NAME= 'sequences.txt'

i = 0
j = 0

with open(FILE_INPUT_NAME, 'r') as r:
    cities_list = r.read().split('\n')

adjacency_matrix = [[0] * len(cities_list) for i in range(len(cities_list))]

for city_1 in cities_list:     
    city_1_list = list(city_1)
    for city_2 in cities_list:
        city_2_list = list(city_2)
        if city_1_list[len(city_1_list)-1] == city_2_list[0]:
            adjacency_matrix[i][j] = 1
        j += 1
    i += 1
    j = 0

seq_list = list(iter_paths(adjacency_matrix))

with open(FILE_OUTPUT_NAME, 'w') as w:
    for s_list in seq_list:
        for i in s_list:
            w.write(cities_list[i] + ' ')
        w.write('\n')