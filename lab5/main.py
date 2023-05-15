import time
import random
import numpy as np
import matplotlib.pyplot as plt


def generate_graph(n, density):
    # Generate an adjacency matrix for a random graph with n vertices and specified density
    graph = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            if random.random() < density:
                weight = random.randint(1, 100)
                graph[i][j] = weight
                graph[j][i] = weight
    return graph


def dijkstra(graph, start):
    # Implementation of Dijkstra's algorithm for finding shortest paths in a graph
    n = len(graph)
    visited = [False] * n
    distances = [float('inf')] * n
    distances[int(start)] = 0
    for i in range(n):
        # Find the vertex with the minimum distance that has not been visited yet
        min_distance = float('inf')
        for j in range(n):
            if not visited[j] and distances[j] < min_distance:
                min_distance = distances[j]
                min_vertex = j
        # Update distances for neighbors of the current vertex
        visited[min_vertex] = True
        for k in range(n):
            if graph[min_vertex][k] > 0 and not visited[k]:
                new_distance = distances[min_vertex] + graph[min_vertex][k]
                if new_distance < distances[k]:
                    distances[k] = new_distance
    return distances


def floyd_warshall(graph):
    # Implementation of Floyd-Warshall algorithm for finding shortest paths in a graph
    n = len(graph)
    distances = np.copy(graph)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if distances[i][j] > distances[i][k] + distances[k][j]:
                    distances[i][j] = distances[i][k] + distances[k][j]
    return distances


def compare(graph, start):
    # Compare Dijkstra's and Floyd-Warshall's algorithms on the given graph
    start_time = time.time()
    dijkstra_distances = dijkstra(graph, start)
    dijkstra_time = time.time() - start_time
    start_time = time.time()
    floyd_distances = floyd_warshall(graph)
    floyd_time = time.time() - start_time
    return dijkstra_time, floyd_time


def generate_weights_graph(n):
    # Generate a plot of the weights of a graph with n vertices
    weights = []
    for i in range(n):
        for j in range(i + 1, n):
            weights.append(random.randint(1, 100))
    plt.hist(weights, bins=range(0, 101, 5))
    plt.xlabel('Weight')
    plt.ylabel('Frequency')
    plt.title('Distribution of edge weights')
    plt.show()


# Test the algorithms on graphs of varying density and size
n_values = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]  # different values of n
density_values = [0.2, 0.4, 0.6, 0.8, 1.0]  # different values of density
start = '0'

for density in density_values:
    dense_times_dijkstra = []
    dense_times_floyd = []
    sparse_times_dijkstra = []
    sparse_times_floyd = []
for n in n_values:
    dense_graph = generate_graph(n, density)
    sparse_graph = generate_graph(n, density / 2)
    dense_time_dijkstra, dense_time_floyd = compare(dense_graph, start)
    sparse_time_dijkstra, sparse_time_floyd = compare(sparse_graph, start)
    dense_times_dijkstra.append(dense_time_dijkstra)
    dense_times_floyd.append(dense_time_floyd)
    sparse_times_dijkstra.append(sparse_time_dijkstra)
    sparse_times_floyd.append(sparse_time_floyd)

plt.plot(n_values, dense_times_dijkstra, label='Dijkstra (dense)', color='blue')
plt.plot(n_values, dense_times_floyd, label='Floyd (dense)', color='black')
plt.plot(n_values, sparse_times_dijkstra, label='Dijkstra (sparse)', color='cyan')
plt.plot(n_values, sparse_times_floyd, label='Floyd (sparse)', color='purple')

plt.xlabel('Number of vertices')
plt.ylabel('Execution time (seconds)')
plt.title(f'Time Complexity')
plt.legend()
plt.show()