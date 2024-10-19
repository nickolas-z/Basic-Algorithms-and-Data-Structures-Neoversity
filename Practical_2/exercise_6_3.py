import heapq

import networkx as nx
import matplotlib.pyplot as plt

# Створення вагового графа
G = nx.Graph()
G.add_edge("Alice", "Bob", weight=5)
G.add_edge("Bob", "Charlie", weight=3)
G.add_edge("Charlie", "Diana", weight=4)
G.add_edge("Diana", "Eva", weight=2)
G.add_edge("Eva", "Alice", weight=6)
G.add_edge("Bob", "Diana", weight=5)
G.add_edge("Diana", "Alice", weight=1)


# Реалізація алгоритму Дейкстри (є в матеріалах з поясненнями)
def dijkstra(graph, start):
    shortest_paths = {vertex: float('infinity') for vertex in graph}
    shortest_paths[start] = 0
    pq = [(0, start)]
    while pq:
        print("pq: ", pq)
        print("sp:", shortest_paths)
        current_distance, current_vertex = heapq.heappop(pq)

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight['weight']
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return shortest_paths


# Використання алгоритму Дейкстри
shortest_paths = dijkstra(G, "Alice")
print(shortest_paths)
# Візуалізація графа
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=700, node_color="skyblue", font_size=15, width=2)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()