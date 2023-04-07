import networkx as nx
import random

import matplotlib.pyplot as plt
import timeit


def unbalanced(v_count):
    G = nx.Graph()
    G.add_nodes_from(range(v_count))
    for u in range(v_count):
        e_count = random.randint(0, v_count - 1)
        for v in random.sample(range(v_count), e_count):
            if u != v:
                G.add_edge(u, v)
    return G


def balanced(v_count):
    if v_count % 2 == 1:
        raise ValueError("Number of vertices must be even")
    d = v_count // 2
    G = nx.Graph()
    for i in range(v_count // 2):
        for j in range(i + 1, i + d):
            G.add_edge(i, j % v_count)
    for i in range(v_count // 2, v_count):
        for j in range(i + 1, v_count):
            G.add_edge(i, j)

    return G


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    if not graph.has_node(start):
        raise ValueError(f"Starting node {start} is not in the graph.")

    visited.add(start)

    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

    return visited


def bfs(graph, start):
    visited_nodes = set()
    nodes_to_visit = [start]

    while nodes_to_visit:
        current_node = nodes_to_visit.pop(0)
        if current_node not in visited_nodes:
            visited_nodes.add(current_node)
            for neighbor in graph.neighbors(current_node):
                nodes_to_visit.append(neighbor)

    return visited_nodes


# Set start node
start_node = 0

# Generate inputs for balanced graph
balanced_graphs = [
    {
        "name": "BFS",
        "algorithm": lambda arr: bfs(balanced(arr), start_node),
        "color": "b"
    },
    {
        "name": "DFS",
        "algorithm": lambda arr: dfs(balanced(arr), start_node),
        "color": "c"
    }
]

# Generate inputs for unbalanced graph
unbalanced_graphs = [
    {
        "name": "BFS",
        "algorithm": lambda arr: bfs(unbalanced(arr), start_node),
        "color": "r"
    },
    {
        "name": "DFS",
        "algorithm": lambda arr: dfs(unbalanced(arr), start_node),
        "color": "m"
    }
]

# Set up subplots for balanced and unbalanced graphs
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))

# Plot execution time for each algorithm on a balanced graph
ax1.set_title('Time Complexity, Balanced Graph')
ax1.set_xlabel('Number of vertices')
ax1.set_ylabel('Execution Time, s')

for coord in balanced_graphs:
    x_balanced = []
    y_balanced = []
    total_start_time = timeit.default_timer()
    for i in range(1, 51):
        start_time = timeit.default_timer()
        n_vertices = i * 10
        coord["algorithm"](n_vertices)
        end_time = timeit.default_timer()
        x_balanced.append(n_vertices)
        y_balanced.append(end_time - start_time)

    ax1.plot(x_balanced, y_balanced, label=coord["name"], color=coord["color"])

ax1.legend()

# Plot execution time for each algorithm on an unbalanced graph
ax2.set_title('Time Complexity, Unbalanced Graph')
ax2.set_xlabel('Number of vertices')
ax2.set_ylabel('Execution Time, s')

for coord in unbalanced_graphs:
    x_unbalanced = []
    y_unbalanced = []
    start_all = timeit.default_timer()
    for i in range(1, 51):
        start = timeit.default_timer()
        v_count = 10 * i
        coord["algorithm"](v_count)
        end = timeit.default_timer()
        x_unbalanced.append(v_count)
        y_unbalanced.append(end - start)

    ax2.plot(x_unbalanced, y_unbalanced, label=coord["name"], color=coord["color"])

ax2.legend()
plt.show()

# Generate inputs for balanced graph
balanced_graphs = [{"name": "BFS Balanced", "algorithm": lambda arr: bfs(balanced(arr), start_node), "color": "b"},
                   {"name": "DFS Balanced", "algorithm": lambda arr: dfs(balanced(arr), start_node), "color": "c"}]

# Generate inputs for unbalanced graph
unbalanced_graphs = [
    {"name": "BFS Unbalanced", "algorithm": lambda arr: bfs(unbalanced(arr), start_node), "color": "m"},
    {"name": "DFS Unbalanced", "algorithm": lambda arr: dfs(unbalanced(arr), start_node), "color": "k"}]

plt.title('Empirical comparison')
plt.xlabel('Number of vertices')
plt.ylabel('Execution Time, s')

for graph in balanced_graphs + unbalanced_graphs:
    x = []
    y = []
    start_all = timeit.default_timer()
    for i in range(1, 51):
        start = timeit.default_timer()
        v_count = 10 * i
        graph["algorithm"](v_count)
        end = timeit.default_timer()
        x.append(v_count)
        y.append(end - start)

    plt.plot(x, y, label=graph["name"], color=graph["color"])

plt.legend()
plt.show()

# Generate an unbalanced graph with 10 nodes
G_unbalanced = unbalanced(10)
# Draw the unbalanced graph with title
plt.title('Unbalanced Graph')
nx.draw(G_unbalanced, with_labels=True)
plt.show()

# Generate a balanced graph with 10 nodes
G_balanced = balanced(10)
# Draw the balanced graph with title
plt.title('Balanced Graph')
nx.draw(G_balanced, with_labels=True)
plt.show()
