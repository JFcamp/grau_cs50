import sys
from collections import deque

actors = {
    "Emma Watson": ["Harry Potter and the Order of the Phoenix"],
    "Brendan Gleeson": ["Harry Potter and the Order of the Phoenix", "Trespass Against Us"],
    "Michael Fassbender": ["Trespass Against Us", "X-Men: First Class"],
    "Jennifer Lawrence": ["X-Men: First Class"]
}

def build_graph(actors):
    graph = {}
    for actor, movies in actors.items():
        for movie in movies:
            if movie not in graph:
                graph[movie] = set()
            graph[movie].add(actor)
    return graph

def degrees_of_separation(graph, start_actor, target_actor):
    queue = deque([(start_actor, 0)])
    visited = set([start_actor])
    
    while queue:
        current_actor, degree = queue.popleft()
        
        if current_actor == target_actor:
            return degree
        
        for movie in graph:
            if current_actor in graph[movie]:
                for actor in graph[movie]:
                    if actor not in visited:
                        visited.add(actor)
                        queue.append((actor, degree + 1))
    
    return None

def main():
    start_actor = "Emma Watson"
    target_actor = "Jennifer Lawrence"
    
    graph = build_graph(actors)
    
    degree = degrees_of_separation(graph, start_actor, target_actor)
    
    if degree is None:
        print(f"Não foi possível encontrar uma conexão entre {start_actor} e {target_actor}.")
    else:
        print(f"{start_actor} e {target_actor} estão a {degree} graus de separação.")
        queue = deque([(start_actor, 0)])
        visited = set([start_actor])

        path = []
        while queue:
            current_actor, degree = queue.popleft()  # Certificando-se de desempacotar corretamente
            for movie in graph:
                if current_actor in graph[movie]:
                    for actor in graph[movie]:
                        if actor == target_actor:
                            path.append(f"{current_actor} e {actor} atuaram em {movie}.")
                            print(f"3 graus de separação.")
                            print(path)
                            queue.clear()  # Esvaziando a fila para sair do loop
                            break

main()
