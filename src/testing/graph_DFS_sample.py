class vertex:
    def __init__(self, data):
        self.data = data
        self.neighbor = {}

    def add_neighbor(self, name, weight=0):
        self.neighbor[name] = weight


class graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, name, vertex):
        self.vertices[name] = vertex


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


def find_path(g, start, goal):
    return _find_path(g, start, goal, set())


def _find_path(g, start, goal, visited):
    if goal in g.vertices[start].neighbor:
        return [start, goal]
    for nbr in g.vertices[start].neighbor:
        if nbr not in visited:
            visited.add(start)
            path = _find_path(g, nbr, goal, visited)
            if path is not None:
                return [start] + path


def main():
    vertexA = vertex('A')
    vertexB = vertex('B')
    vertexC = vertex('C')
    vertexD = vertex('D')
    vertexE = vertex('E')
    vertexF = vertex('F')
    vertexG = vertex('G')
    vertexH = vertex('H')
    vertexI = vertex('I')
    vertexJ = vertex('J')

    vertexA.add_neighbor('B', 3)
    vertexA.add_neighbor('C', 4)
    vertexB.add_neighbor('D', 4)
    vertexB.add_neighbor('E', 4)
    vertexB.add_neighbor('F', 4)
    vertexD.add_neighbor('G', 4)
    vertexD.add_neighbor('H', 4)
    vertexE.add_neighbor('I', 4)
    vertexE.add_neighbor('J', 4)

    g = graph()
    g.add_vertex('A', vertexA)
    g.add_vertex('B', vertexB)
    g.add_vertex('C', vertexC)
    g.add_vertex('D', vertexD)
    g.add_vertex('E', vertexE)
    g.add_vertex('F', vertexF)
    g.add_vertex('G', vertexG)
    g.add_vertex('H', vertexH)
    g.add_vertex('I', vertexI)
    g.add_vertex('J', vertexJ)

    print(path_Exists(g, 'A', 'H'))
    print(find_path(g, 'A', 'H'))


if __name__ == '__main__':
    main()
