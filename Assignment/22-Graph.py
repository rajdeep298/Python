# class Graph:
#     def __init__(self):
#         self.src = []
#         self.dest = []
#         self.status = []
#         self.front = self.rear = -1
#         self.queue = []
#         self.n = 0
#         self.graph = []
#         self.el0 = []
#         self.el1 = []
#
#     def edgelistInitialize(self):
#         n = int(input("Enter the number of edges in edgelist: "))
#         for i in range(n):
#             print("Enter the source vertex:")
#             self.el0.append(int(input()))
#             print("Enter the destination vertex:")
#             self.el1.append(int(input()))
#
#     def graphFromEdgeList(self):
#         self.n = max(max(self.el0), max(self.el1)) + 1
#         self.graph = [[0] * self.n for _ in range(self.n)]
#         for i in range(len(self.el0)):
#             self.graph[self.el0[i]][self.el1[i]] = 1
#
#     def nodeRemove(self, node):
#         for i in range(len(self.graph)):
#             self.graph[i][node] = 0
#             self.graph[node][i] = 0
#
#     def edgeAdd(self, sv, ev):
#         self.graph[sv][ev] = 1
#         self.graph[ev][sv] = 1
#
#     def nodeAdd(self, node):
#         for i in range(len(self.graph)):
#             self.graph[i][node] = 0
#             self.graph[node][i] = 0
#
#     def edgeRemove(self, sv, ev):
#         self.graph[sv][ev] = 0
#         self.graph[ev][sv] = 0
#
#     def vertexDegree(self, node):
#         degree = 0
#         for i in range(len(self.graph)):
#             if self.graph[node][i] == 1:
#                 degree += 1
#         return degree
#
#     def neighbours(self, node):
#         neighbours = []
#         for i in range(len(self.graph)):
#             if self.graph[node][i] == 1:
#                 neighbours.append(i)
#         return neighbours
#
#     def printNodeEdges(self):
#         for i in range(len(self.graph)):
#             print(i, end=" ")
#         print()
#         for i in range(len(self.graph)):
#             for j in range(len(self.graph)):
#                 if self.graph[i][j] == 1:
#                     print(i, "->", j, end=", ")
#
#     def clustering_coefficient(self):
#         coefficients = {}
#         for node in range(self.n):
#             neighbors = self.neighbours(node)
#             if len(neighbors) < 2:
#                 coefficients[node] = 0.0
#             else:
#                 total_triangles = 0
#                 for neighbor1 in neighbors:
#                     for neighbor2 in neighbors:
#                         if neighbor1 != neighbor2 and self.graph[neighbor1][neighbor2] == 1:
#                             total_triangles += 1
#                 coefficients[node] = total_triangles / (len(neighbors) * (len(neighbors) - 1))
#         return coefficients
#
#     def degree_distribution(self):
#         return {node: sum(self.graph[node]) for node in range(self.n)}
#
#     def connected_components(self):
#         visited = set()
#         components = []
#
#         for node in range(self.n):
#             if node not in visited:
#                 component = self._dfs(node, visited)
#                 components.append(component)
#
#         return components
#
#     def _dfs(self, start, visited):
#         component = set()
#         stack = [start]
#
#         while stack:
#             current_node = stack.pop()
#             if current_node not in visited:
#                 visited.add(current_node)
#                 component.add(current_node)
#                 stack.extend(neighbor for neighbor in self.neighbours(current_node) if neighbor not in visited)
#
#         return component
#
#     def connected_components_as_graphs(self):
#         connected_components = self.connected_components()
#         graphs = []
#
#         for component in connected_components:
#             subgraph = Graph()
#             subgraph.n = max(component) + 1
#             subgraph.graph = [[0] * subgraph.n for _ in range(subgraph.n)]
#             for i in component:
#                 for j in component:
#                     subgraph.graph[i][j] = self.graph[i][j]
#             graphs.append(subgraph)
#
#         return graphs
#
#     def enqueue(self, node):
#         self.queue.append(node)
#
#     def dequeue(self):
#         return self.queue.pop(0) if self.queue else None
#
#     def BFS(self, start):
#         self.queue.append(start)
#         self.status[start] = '!'
#         self.src[start] = '*'
#
#         while self.queue:
#             node = self.dequeue()
#             if node is not None:
#                 for neighbor in self.neighbours(node):
#                     if self.status[neighbor] == '?' and self.dest[neighbor] == '?':
#                         self.enqueue(neighbor)
#                         self.status[neighbor] = '#'
#                         self.src[neighbor] = node
#
#         print("BFS->", self.queue)
#
#
# # Example usage
# graph = Graph()
#
# # Edge list
# graph.edgelistInitialize()
# print("Edge List ->", graph.el0, graph.el1)
#
# # Graph from edge list
# graph.graphFromEdgeList()
# print("Graph ->", graph.graph)
#
# # Add node
# graph.nodeAdd(8)
# print("Graph after adding node ->", graph.graph)
#
# # Add edge
# graph.edgeAdd(8, 9)
# print("Graph after adding edge ->", graph.graph)
#
# # Remove node
# graph.nodeRemove(8)
# print("Graph after removing node ->", graph.graph)
#
# # Remove edge
# graph.edgeRemove(8, 9)
# print("Graph after removing edge ->", graph.graph)
#
# # Print node edges
# print("Node Edges:")
# graph.printNodeEdges()
# print()
#
# # Degree Distribution
# print("Degree Distribution ->", graph.degree_distribution())
# print()
#
# # Clustering Coefficient
# print("Clustering Coefficient ->", graph.clustering_coefficient())
# print()
#
# # Connected Components
# print("Connected Components ->", graph.connected_components())
# print()
#
# # Connected Components as Graphs
# print("Connected Components as Graphs:")
# subgraphs = graph.connected_components_as_graphs()
# for idx, subgraph in enumerate(subgraphs):
#     print(f"Subgraph {idx + 1} ->", subgraph.graph)
# print()
#
# # BFS
# graph.BFS(0)

from collections import deque


class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def read_edge_list(self, filename):
        with open(filename, "r") as file:
            for line in file:
                u, v = map(int, line.strip().split())
                self.add_edge(u, v)

    def add_node(self, node):
        self.nodes.add(node)

    def remove_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)
            for neighbor in self.edges.pop(node, []):
                self.remove_edge(neighbor, node)

    def add_edge(self, u, v):
        self.nodes.add(u)
        self.nodes.add(v)
        self.edges.setdefault(u, []).append(v)
        self.edges.setdefault(v, []).append(u)

    def remove_edge(self, u, v):
        self.edges[u].remove(v)
        self.edges[v].remove(u)

    def print_graph(self):
        print("Nodes:", self.nodes)
        print("Edges:")
        for node, neighbors in self.edges.items():
            print(f"{node} -> {neighbors}")

    def degree_distribution(self):
        degrees = [len(self.edges[node]) for node in self.nodes]
        return degrees

    def clustering_coefficient(self):
        clustering_coefficients = {}
        for node in self.nodes:
            neighbors = self.edges[node]
            if len(neighbors) > 1:
                possible_edges = len(neighbors) * (len(neighbors) - 1) / 2
                existing_edges = 0
                for neighbor1 in neighbors:
                    for neighbor2 in neighbors:
                        if neighbor2 in self.edges[neighbor1]:
                            existing_edges += 1
                clustering_coefficients[node] = existing_edges / possible_edges
            else:
                clustering_coefficients[node] = 0.0
        return clustering_coefficients

    def connected_components(self):
        components = []
        visited = set()
        for node in self.nodes:
            if node not in visited:
                component = Graph()
                self._dfs_connected_component(node, component, visited)
                components.append(component)
        return components

    def _dfs_connected_component(self, node, component, visited):
        visited.add(node)
        component.add_node(node)
        for neighbor in self.edges[node]:
            if neighbor not in visited:
                component.add_edge(node, neighbor)
                self._dfs_connected_component(neighbor, component, visited)

    def neighbors(self, node):
        return self.edges[node]

    def shortest_paths(self, source):
        distances = {node: float("inf") for node in self.nodes}
        distances[source] = 0
        queue = deque([source])

        while queue:
            current = queue.popleft()
            for neighbor in self.edges[current]:
                if distances[neighbor] == float("inf"):
                    distances[neighbor] = distances[current] + 1
                    queue.append(neighbor)
        return distances


graph = Graph()
graph.read_edge_list("edges.txt")
graph.print_graph()
components = graph.connected_components()
print("Distribution: ", graph.degree_distribution())
print("Clustering coefficient: ", graph.clustering_coefficient())
print("Neighbour of node 3")
neighbors_of_node_3 = graph.neighbors(3)
print(neighbors_of_node_3)
print("Shortest Path from node 1")
shortest_paths_from_node_1 = graph.shortest_paths(1)
print(shortest_paths_from_node_1)
