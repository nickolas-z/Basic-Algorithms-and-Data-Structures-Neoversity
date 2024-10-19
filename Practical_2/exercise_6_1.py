import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин (людей)
G.add_nodes_from(["Академмістечко", "Житомирська", "Charlie", "Diana", "Lonely"])

# Додавання ребер (зв'язків між людьми)
G.add_edges_from([("Академмістечко", "Житомирська"), ("Житомирська", "Charlie"), ("Charlie", "Diana"),
                  ("Diana", "Eva"), ("Eva", "Житомирська"), ("Житомирська", "Diana")])


# Візуалізація графа
nx.draw(G, with_labels=True)
plt.show()

# Кількість вершин
num_nodes = G.number_of_nodes()

# Кількість ребер
num_edges = G.number_of_edges()

print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
# Вивести ступені вершин