class Graph:
    src = []
    dest = []
    status = []
    front = rear = -1
    queue = []
    n=0
    graph = []

    def graphFromEdgeList(self, el):
        self.graph = []
        for i in range(len(el)):
            self.graph[el[0][i]][el[1][i]] = 1

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
        self.status[0]='!'
        self.src[0]='*'

        while self.front != self.rear:
            node = self.dequeue()
            for i in range(len(self.graph)):
                if self.graph[node][i] == 1 and self.status[i] == '?' and self.dest[i] == '?':
                    self.enqueue(i)
                    self.status[i] = '#'
                    self.src[i] = node

        print("BFS->", self.queue)

graph=Graph()
edge_list = [[0, 0, 1, 2, 3, 3, 4, 4, 4, 5, 5],[1, 2, 2, 3, 4, 5, 5, 6, 7, 6, 7]]

#Graph from edge list
graph.graphFromEdgeList(edge_list)
print("Graph->",graph.graph)

#Add node
graph.nodeAdd(8)
print("Graph->",graph.graph)

#Add edge
graph.edgeAdd(8,9)
print("Graph->",graph.graph)

#Remove node
graph.nodeRemove(8)
print("Graph->",graph.graph)

#Remove edge
graph.edgeRemove(8,9)

#Print node edges
graph.printNodeEdges()

#Degree Distribution
print("Degree Distribution->",graph.degree_distribution())

#Clustering Coefficient
print("Clustering Coefficient->",graph.clustering_coefficient())

#Connected Components
print("Connected Components->",graph.connected_components())

#Connected Components as Graphs
print("Connected Components as Graphs->",graph.connected_components_as_graphs())

#BFS
graph.BFS(0)
