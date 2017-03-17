class Vertex:
    def __init__(self,data):
        self.data = data
        self.neighbor = {}

    def addNeighbor(self,name,weight):
        self.neighbor[name] = weight

class graph:
    def __init__(self):
        self.vertices = {}

    def addVertex(self,name,vertex):
        self.vertices[name] = vertex

def shortest_path_exists(graph,start,goal):
    q = []
    visited = set()
    q.append(start)
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

def shortest_path(graph,start,goal):
    q = []
    parent = {}
    q.append(start)
    parent[start] = None
    while q:
        n = q.pop(0)
        if n == goal:
            return construct_path(parent,goal)
        for nbr in graph.vertices[n].neighbor:
            if nbr not in parent:
                q.append(nbr)
                parent[nbr] = n

    return None

def construct_path(parent,goal):
    path = []
    path.append(goal)
    x = goal
    while x is not None:
        path.append(parent[x])
        x = parent[x]
    path.remove(None)
    path.reverse()
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

    vertexA.addNeighbor('B', 3)
    vertexA.addNeighbor('C', 4)
    vertexB.addNeighbor('D', 4)
    vertexB.addNeighbor('E', 4)
    vertexB.addNeighbor('F', 4)
    vertexD.addNeighbor('G', 4)
    vertexD.addNeighbor('H', 4)
    vertexE.addNeighbor('I', 4)
    vertexE.addNeighbor('J', 4)

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

    print(shortest_path_exists(g,'A','H'))
    print(shortest_path(g,'A','H'))


if __name__ == '__main__':
    main()


