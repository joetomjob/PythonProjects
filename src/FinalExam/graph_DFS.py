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


def pathExists(graph, start, goal):
    return _pathExists(graph, start, goal,set())

def _pathExists(graph, start, goal,visited):
    if goal in graph.vertices[start].neighbor:
        return True

    for nbr in graph.vertices[start].neighbor:
        if nbr not in visited:
            visited.add(start)
            if _pathExists(graph,nbr,goal,visited):
                return True
    return False

def findpath(graph, start, goal):
    return _findPath(graph, start, goal,set())

def _findPath(graph, start, goal,visited):
    if goal in graph.vertices[start].neighbor:
        return [start,goal]

    for nbr in graph.vertices[start].neighbor:
        visited.add(start)
        if nbr not in visited:
            path =  _findPath(graph, nbr, goal,visited)
            if path is not None:
                path = [start]+path
                return path
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

    # for i in g.vertices:
    #     print(g.vertices[i].data)

    print(pathExists(g,'A','H'))
    print(findpath(g,'A','H'))

if __name__ == '__main__':
    main()
