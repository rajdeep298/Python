class Graph:
    n = 0
    graph = []
    src = []
    dest = []
    status = []
    cost = []

    def __init__(self, g):
        self.graph = g
        self.n = len(g)

    def floyd(self):
        temp = self.graph
        for i in range(self.n):
            for j in range(self.n):
                if temp[i][j] == 0 and i != j:
                    temp[i][j] = 99

        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    temp[i][j] = min(temp[i][j], self.graph[i][k] + self.graph[k][j])
        self.display(temp)

    def djikstraInit(self, v):
        for i in range(self.n):
            self.src.append(v)
            self.dest.append(i)
            self.status.append('?')
            if self.graph[v][i] == 0:
                self.cost.append(999)
            else:
                self.cost.append(self.graph[v][i])
        self.status[v] = '!'
        self.cost[v] = 0
        self.src[v] = '*'

    def djikstraMinpos(self, v):
        minPos = -1
        i = 0
        for i in range(self.n):
            if self.status[i] == '?':
                minPos = i
                break

        for j in range(i + 1, self.n):
            if self.status[j] == '?' and self.cost[j] < self.cost[minPos]:
                minPos = j

        return minPos

    def djikstraUpdate(self, v):
        self.status[v] = '!'
        for i in range(self.n):
            if self.graph[v][i] != 0 and self.status[i] == '?':
                if self.cost[v] + self.graph[v][i] < self.cost[i]:
                    self.cost[i] = self.cost[v] + self.graph[v][i]
                    self.src[i] = v

    def djikstra(self, v):
        self.djikstraInit(v)
        while 1:
            minPos = self.djikstraMinpos(v)
            if minPos == -1:
                break
            self.djikstraUpdate(minPos)
        self.displayDjikstra()

    def display(self, g):
        for i in range(self.n):
            for j in range(self.n):
                print(g[i][j], end='\t')
            print()
        print()

    def displayDjikstra(self):
        k = 0
        djikstra = []
        final = int(input("Enter the destination vertex: "))
        final -= 1
        start = int(input("Enter the source vertex: "))
        start -= 1
        while (1):
            for i in range(self.n):
                if self.dest[i] == final:
                    if k == 0:
                        djikstra.append(final + 1)
                        k += 1
                    djikstra.append(self.src[i])
                    djikstra[k] += 1
                    if k - 1 == start:
                        print("Path from {} to {} is: ".format(start + 1, final + 1), end=' ')
                        print("Path: ", djikstra)
                        exit(0)
                    final = self.src[i]
                    break


n = int(input("Enter the dimension of the graph matrix: "))

print("Enter the graph matrix: ")

graph = [
    [int(input("Enter the weight of the edge from vertex {} to vertex {}: ".format(i + 1, j + 1))) if i != j else 0 for
     j in range(n)]
    for i in range(n)]

g = Graph(graph)
g.display(graph)
g.floyd()
g.djikstra(0)
