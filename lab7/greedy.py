import networkx as nx
from heapq import heappush, heappop
import matplotlib.pyplot as plt
import time
import random

def kruskal(graph):
    min_spanning_tree = nx.Graph()
    sorted_edges = sorted(graph.edges(data=True), key=lambda x: x[2]["weight"])

    for edge in sorted_edges:
        min_spanning_tree.add_edge(edge[0], edge[1], weight=edge[2]["weight"])

        if len(list(nx.connected_components(min_spanning_tree))) > 1:
            min_spanning_tree.remove_edge(edge[0], edge[1])

    return min_spanning_tree


def prim(graph):
    min_spanning_tree = nx.Graph()
    unvisited_nodes = set(graph.nodes())

    while unvisited_nodes:
        edge_heap = []
        current_node = unvisited_nodes.pop()
        min_spanning_tree.add_node(current_node)

        for edge in graph.edges(current_node, data=True):
            if edge[1] in unvisited_nodes:
                heappush(edge_heap, (edge[2]["weight"], edge[0], edge[1]))

        while edge_heap and edge_heap[0][2] not in unvisited_nodes:
            heappop(edge_heap)

        while edge_heap:
            weight, node1, node2 = heappop(edge_heap)

            if node2 in unvisited_nodes:
                min_spanning_tree.add_edge(node1, node2, weight=weight)
                unvisited_nodes.remove(node2)

                for edge in graph.edges(node2, data=True):
                    if edge[1] in unvisited_nodes:
                        heappush(edge_heap, (edge[2]["weight"], edge[0], edge[1]))

    return min_spanning_tree


def measure_running_times(algorithm, graph_sizes):
    running_times = []
    minimum_spanning_trees = []

    for size in graph_sizes:
        graph = nx.gnm_random_graph(size, size * 2, seed=random.randint(0, 100), directed=False)
        nx.set_edge_attributes(graph, {(u, v): {"weight": random.randint(1, 100)} for u, v in graph.edges()})

        start_time = time.time()
        mst = algorithm(graph)
        end_time = time.time()

        running_times.append(end_time - start_time)
        minimum_spanning_trees.append(mst)

    return running_times, minimum_spanning_trees


graph_sizes = list(range(10, 301, 5))

running_times_prim, msts_prim = measure_running_times(prim, graph_sizes)
running_times_kruskal, msts_kruskal = measure_running_times(kruskal, graph_sizes)

plt.plot(graph_sizes, running_times_prim, label="Prim", color="black")
plt.plot(graph_sizes, running_times_kruskal, label="Kruskal", color="cyan")
plt.xlabel("Vertices")
plt.ylabel("Execution Time, sec")
plt.title("Time Complexity")
plt.legend()
plt.show()

draw_graph_sizes = [10, 30, 50]
for i in range(len(draw_graph_sizes)):
    plt.figure(i + 1)
    plt.title(f"Minimum Spanning Tree (Size: {draw_graph_sizes[i]})")
    pos = nx.spring_layout(msts_prim[i])
    weights = nx.get_edge_attributes(msts_prim[i], "weight")
    nx.draw(msts_prim[i], pos, with_labels=True, node_color='lightblue', edge_color='gray', width=1, font_size=8)
    nx.draw_networkx_edge_labels(msts_prim[i], pos, edge_labels=weights, font_color='red', font_size=6)
    plt.axis("equal")
    plt.show()
