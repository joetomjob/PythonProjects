'''
             A
            / \
           B   C
         / | \
        D   E  F
       /|   |\
      G H   I J
'''

class Vertex:
    __slots__ = ('data', 'neighbor')

    def __init__(self, data):
        self.data = data
        self.neighbor = {}

    def add_neighbor(self, name, weight=0):
        self.neighbor[name] = weight


class Graph:
    __slots__ = ('vertices')

    def __init__(self):
        self.vertices = {}

    def addVertex(self, name, v):
        self.vertices[name] = v

def shortest_Path_Exists(graph,start,goal):
    q = []
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

def shortest_Path(graph,start,goal):
    q =[]
    q.append(start)
    parents = {}
    parents[start] = None
    while q:
        n = q.pop()
        if n == goal:
            return make_Path(parents,goal)
        for nbr in graph.vertices[n].neighbor:
            if nbr not in parents:
                q.append(nbr)
                parents[nbr] = n
    return None

def make_Path(parents, goal):
    path = []
    path.append(goal)
    current = goal
    while current is not None:
        current = parents[current]
        path.append(current)

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
    vertexA.add_neighbor('B', 3)
    vertexA.add_neighbor('C', 4)
    vertexB.add_neighbor('D', 4)
    vertexB.add_neighbor('E', 4)
    vertexB.add_neighbor('F', 4)
    vertexD.add_neighbor('G', 4)
    vertexD.add_neighbor('H', 4)
    vertexE.add_neighbor('I', 4)
    vertexE.add_neighbor('J', 4)

    for x in vertexA.neighbor:
        print(x)

    g = Graph()
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

    print(shortest_Path_Exists(g, 'A', 'J'))
    print(shortest_Path(g, 'A', 'J'))


if __name__ == '__main__':
    main()
