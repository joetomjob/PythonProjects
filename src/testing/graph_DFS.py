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

    def addneighbor(self, name, weight=0):
        self.neighbor[name] = weight


class Graph:
    __slots__ = ('vertices')

    def __init__(self):
        self.vertices = {}

    def addVertex(self, name, v):
        self.vertices[name] = v


def path_Exists(graph, start, goal):
    return _path_Exists(graph, start, goal, set())


def _path_Exists(graph, start, goal, visited):
    if goal in graph.vertices[start].neighbor:
        return True
    for nbr in graph.vertices[start].neighbor:
        if nbr not in visited:
            visited.add(start)
            if _path_Exists(graph, nbr, goal, visited):
                return True
    return False


def find_Path(graph, start, goal):
    return _find_Path(graph, start, goal, set())


def _find_Path(graph, start, goal, visited):
    if goal in graph.vertices[start].neighbor:
        return [start, goal]
    for nbr in graph.vertices[start].neighbor:
        if nbr not in visited:
            visited.add(start)
            path = _find_Path(graph, nbr, goal, visited)
            if path is not None:
                return [start] + path


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

    print(path_Exists(g, 'A', 'H'))
    print(find_Path(g, 'A', 'H'))


if __name__ == '__main__':
    main()
