import pandas as pd
from collections import deque

base_path = "C:/Users/PedroMoreira/OneDrive - BLACK WHEELS/Área de Trabalho/harvard/degrees/degrees/small/"

people_small_df = pd.read_csv(base_path + 'people.csv')
movies_small_df = pd.read_csv(base_path + 'movies.csv')
stars_small_df = pd.read_csv(base_path + 'stars.csv')

movies_mapping = dict(zip(movies_small_df['id'], zip(movies_small_df['title'], movies_small_df['year'])))
people_mapping = dict(zip(people_small_df['id'], people_small_df['name']))

person_movies_mapping = {}
for _, row in stars_small_df.iterrows():
    if row['person_id'] not in person_movies_mapping:
        person_movies_mapping[row['person_id']] = set()
    person_movies_mapping[row['person_id']].add(row['movie_id'])

def neighbors_for_person(person_id):
    neighbors = set()
    for movie_id in person_movies_mapping.get(person_id, []):
        for _, row in stars_small_df[stars_small_df['movie_id'] == movie_id].iterrows():
            if row['person_id'] != person_id:
                neighbors.add((movie_id, row['person_id']))
    return neighbors

def shortest_path(source, target):
    if source == target:
        return []

    queue = deque([((None, source), [])])
    visited = set([source])
    
    while queue:
        (prev_person, current_person), path = queue.popleft()
        
        if current_person == target:
            return path + [(prev_person, current_person)]
        
        for movie_id, neighbor in neighbors_for_person(current_person):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(((current_person, neighbor), path + [(movie_id, current_person)]))
    
    return None

source_person_id = 102
target_person_id = 129
shortest_path_result = shortest_path(source_person_id, target_person_id)

print(shortest_path_result)
