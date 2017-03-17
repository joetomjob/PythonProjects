'''
             A
            / \
           B   C
         / | \
        D   E  F
       /|   |\
      G H   I J
'''

from queue import PriorityQueue

class Vertex:
    __slots__ = ('data', 'neighbor')

    def __init__(self, data):
        self.data = data
        self.neighbor = {}

    def addneighbor(self, name, weight=0):
        self.neighbor[name] = weight


class Graph:
    __slots__ = ('vertices')

    def __init__(self):
        self.vertices = {}

    def addVertex(self, name, v):
        self.vertices[name] = v


def make_Path(parents, goal):
    path = []
    path.append(goal)
    current = goal
    while current is not None:
        current = parents[current]
        path.append(current)

    path.reverse()
    return path


def dijkstra(graph,start,goal):
    q = PriorityQueue()
    q.put((0,start))
    parents = {}
    costs = {}
    costs[start] = 0
    parents[start] = None
    while q:
        cost,n = q.get()
        if n == goal:
            return make_Path(parents,goal),costs
        for nbr in graph.vertices[n].neighbor:
            newcost = cost+graph.vertices[n].neighbor[nbr]
            if nbr not in parents or newcost < costs[nbr]:
                parents[nbr] = n
                costs[nbr] = newcost
                q.put((newcost,nbr))
    return None


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

    # print(path_Exists(g, 'A', 'H'))
    print(dijkstra(g, 'A', 'H'))


if __name__ == '__main__':
    main()

