import networkx as nx
import matplotlib.pyplot as plt

# Створення та налаштування графа (використовуємо граф з першого завдання)
G = nx.Graph()
G.add_edges_from([("Alice", "Bob"), ("Bob", "Charlie"), ("Charlie", "Diana"),
                  ("Eva", "Alice"), ("Bob", "Diana"), ("Diana", "Alice")])

# DFC через рекурсію (можна зробити й через stack)
def dfs(graph, start, visited=None, path=None, parent=None):
    if visited is None:
        visited = set()
        path = []
    # Є помилка і бо ми не перевіряємо чи ми вже відвідуємо пройдені вершини, 
    # потрібно використати visited для перевірки
    visited.add(start)
    print(f"DFC: visited {start}")
    if parent is not None:
        path.append((parent, start))
    for next in graph[start]:
        dfs(graph, next, visited, path, start)
    return path

# BFS через queue
def bfs(graph, start):
    visited, queue = {start}, [start]
    path = []

    while queue:
        vertex = queue.pop(0)
        print(f"BFC: visited {vertex}")
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
                path.append((vertex, neighbour))
    # Помилка в тому що повертаємо можливо?
    return visited


# Виконання DFS та BFS
dfs_path = dfs(G, "Alice")
bfs_path = bfs(G, "Alice")

print(f"DFS path: {dfs_path}")
print(f"BFS path: {bfs_path}")

# Візуалізація графа
nx.draw(G, with_labels=True)
plt.show()

# Використання вбудованих функцій networkX для DFS та BFS що є кращим ніж вигадувати щось своє, 
# але все ж варто знати як вони працюють всередині на майбутнє

# dfs_path = list(nx.dfs_edges(G, source="Alice"))
# bfs_path = list(nx.bfs_edges(G, source="Alice"))

# print(f"DFS path: {dfs_path}")
# print(f"BFS path: {bfs_path}")