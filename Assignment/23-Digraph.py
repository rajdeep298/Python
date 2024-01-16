class Graph:
    def __init__(self):
        self.src = []
        self.dest = []
        self.status = []
        self.front = self.rear = -1
        self.queue = []
        self.n = 0
        self.graph = []
        self.el0 = []
        self.el1 = []

    def edgelistInitialize(self):
        n=int(input("Enter the number of edges in edgelist:"))
        for i in range(n):
            print("Enter the source vertex:")
            self.el0.append(int(input()))
            print("Enter the destination vertex:")
            self.el1.append(int(input()))

    def graphFromEdgeList(self):
        for i in range(len(self.el0)):
            self.graph[self.el0[i]][self.el1[i]] = 1

    def nodeRemove(self, node):
        for i in range(len(self.graph)):
            self.graph[i][node] = 0
            self.graph[node][i] = 0

    def edgeAdd(self, sv, ev):
        self.graph[sv][ev] = 1
        self.graph[ev][sv] = 1

    def nodeAdd(self, node):
        for i in range(len(self.graph)):
            self.graph[i][node] = 0
            self.graph[node][i] = 0

    def edgeRemove(self, sv, ev):
        self.graph[sv][ev] = 0
        self.graph[ev][sv] = 0

    def vertexDegree(self, node):
        degree = 0
        for i in range(len(self.graph)):
            if self.graph[node][i] == 1:
                degree += 1
        return degree

    def neighbours(self, node):
        neighbours = []
        for i in range(len(self.graph)):
            if self.graph[node][i] == 1:
                neighbours.append(i)
        return neighbours

    def printNodeEdges(self, ):
        for i in range(len(self.graph)):
            print(i, end=" ")
        print()
        for i in range(len(self.graph)):
            for j in range(len(self.graph)):
                if self.graph[i][j] == 1:
                    print(i, "->", j, end=",")

    def clustering_coefficient(self):
        coefficients = {}
        for node in self.graph:
            neighbors = self.graph[node]
            if len(neighbors) < 2:
                coefficients[node] = 0.0
            else:
                total_triangles = 0
                for neighbor1 in neighbors:
                    for neighbor2 in neighbors:
                        if neighbor1 != neighbor2 and neighbor1 in self.graph[neighbor2]:
                            total_triangles += 1
                coefficients[node] = total_triangles / (len(neighbors) * (len(neighbors) - 1))
        return coefficients

    def degree_distribution(self):
        return {node: len(neighbors) for node, neighbors in self.graph.items()}

    def connected_components(self):
        visited = set()
        components = []

        for node in self.graph:
            if node not in visited:
                component = self._dfs(node, visited)
                components.append(component)

        return components

    def _dfs(self, start, visited):
        component = set()
        stack = [start]

        while stack:
            current_node = stack.pop()
            if current_node not in visited:
                visited.add(current_node)
                component.add(current_node)
                stack.extend(neighbor for neighbor in self.graph[current_node] if neighbor not in visited)

        return component

    def connected_components_as_graphs(self):
        connected_components = self.connected_components()
        graphs = [Graph() for _ in range(len(connected_components))]

        for idx, component in enumerate(connected_components):
            for node in component:
                graphs[idx].graph[node] = self.graph[node]

        return graphs

    def enqueue(self, node):
        self.queue[self.rear] = node
        self.rear += 1

    def dequeue(self):
        self.front += 1
        return self.queue[self.front]

    def BFS(self, node):
        for i in range(len(self.graph)):
            self.status.append('?')
            self.src.append('?')
            self.dest.append('?')
        self.queue.append('0')
        self.status[0] = '!'
        self.src[0] = '*'

        while self.front != self.rear:
            node = self.dequeue()
            for i in range(len(self.graph)):
                if self.graph[node][i] == 1 and self.status[i] == '?' and self.dest[i] == '?':
                    self.enqueue(i)
                    self.status[i] = '#'
                    self.src[i] = node

        print("BFS->", self.queue)

class DiGraph(Graph):
    class DiGraph(Graph):
        def __init__(self):
            super().__init__()

        def predecessors(self, node):
            return [i for i in range(len(self.graph)) if self.graph[i][node] == 1]

        def successors(self, node):
            return [i for i in range(len(self.graph)) if self.graph[node][i] == 1]

        def reverse_edges(self):
            reversed_graph = [[0 for _ in range(self.n)] for _ in range(self.n)]
            for i in range(self.n):
                for j in range(self.n):
                    reversed_graph[i][j] = self.graph[j][i]
            return reversed_graph

        def strongly_connected_components(self):
            reversed_graph = self.reverse_edges()
            reversed_components = self.connected_components_as_graphs(reversed_graph)
            strongly_connected_components = []

            for component in reversed_components:
                component_nodes = set(node for node in component.graph if component.graph[node])
                original_component = self._dfs_strongly_connected(component_nodes)
                strongly_connected_components.append(original_component)

            return strongly_connected_components

        def _dfs_strongly_connected(self, start_nodes):
            visited = set()
            component = set()
            stack = list(start_nodes)

            while stack:
                current_node = stack.pop()
                if current_node not in visited:
                    visited.add(current_node)
                    component.add(current_node)
                    stack.extend(neighbor for neighbor in self.graph[current_node] if neighbor not in visited)

            return component

di_graph = DiGraph()

# Edge list
di_graph.edgelistInitialize()
print("Edge List ->", di_graph.el0, di_graph.el1)

# Initialize graph
di_graph.n = max(max(di_graph.el0), max(di_graph.el1)) + 1
di_graph.graph = [[0] * di_graph.n for _ in range(di_graph.n)]

# Graph from edge list
di_graph.graphFromEdgeList()
print("Graph ->", di_graph.graph)

# Predecessors and Successors
node_to_check = 0
print(f"Predecessors of {node_to_check} ->", di_graph.predecessors(node_to_check))
print(f"Successors of {node_to_check} ->", di_graph.successors(node_to_check))

# Reverse edges
reversed_edges = di_graph.reverse_edges()
print("Reversed Edges ->", reversed_edges)

# Strongly Connected Components
strongly_connected_components = di_graph.strongly_connected_components()
print("Strongly Connected Components ->", strongly_connected_components)