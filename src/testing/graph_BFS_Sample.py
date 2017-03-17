class Vertex:
    def __init__(self,item):
        self.data = item
        self.neighbor = {}

    def addneighbor(self,name,wt = 0):
        self.neighbor[name] = wt

class graph:
    def __init__(self):
        self.vertices = {}

    def addVertex(self,name,item):
        self.vertices[name] = item

def shortest_path_Exists(graph, start, goal):
    q =[]
    q.append(start)
    visited = set()
    visited.add(start)
    while q:
        n = q.pop(0)
        if n == goal:
            return True
        for nbr in graph.vertices[n].neighbor:
            if nbr not in visited:
                q.append(nbr)
                visited.add(nbr)
    return False


def shortest_path(graph, start, goal):
    q =[]
    q.append(start)
    parent = {}
    parent[start] = None
    while q:
        n = q.pop(0)
        if n == goal:
            return make_path(parent,goal)
        for nbr in graph.vertices[n].neighbor:
            if nbr not in parent:
                q.append(nbr)
                parent[nbr] = n

    return None

def make_path(parent,goal):
    path = []
    path.append(goal)
    current = goal
    while current is not None:
        current = parent[current]
        path.append(current)

    path.reverse()
    path.remove(None)
    return path


def main():
    vertexA = Vertex('A')
    vertexB = Vertex('B')
    vertexC = Vertex('C')
    vertexD = Vertex('D')
    vertexE = Vertex('E')
    vertexF = Vertex('F')
    vertexG = Vertex('G')
    vertexH = Vertex('H')
    vertexI = Vertex('I')
    vertexJ = Vertex('J')
    vertexA.addneighbor('B', 3)
    vertexA.addneighbor('C', 4)
    vertexB.addneighbor('D', 4)
    vertexB.addneighbor('E', 4)
    vertexB.addneighbor('F', 4)
    vertexD.addneighbor('G', 4)
    vertexD.addneighbor('H', 4)
    vertexE.addneighbor('I', 4)
    vertexE.addneighbor('J', 4)

    for x in vertexA.neighbor:
        print(x)

    g = graph()
    g.addVertex('A', vertexA)
    g.addVertex('B', vertexB)
    g.addVertex('C', vertexC)
    g.addVertex('D', vertexD)
    g.addVertex('E', vertexE)
    g.addVertex('F', vertexF)
    g.addVertex('G', vertexG)
    g.addVertex('H', vertexH)
    g.addVertex('I', vertexI)
    g.addVertex('J', vertexJ)

    print(shortest_path_Exists(g, 'A', 'H'))
    print(shortest_path(g, 'A', 'H'))

if __name__ == '__main__':
    main()
