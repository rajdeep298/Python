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
