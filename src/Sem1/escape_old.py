from copy import deepcopy

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


def shortest_Path_Exists(graph, start, goal):
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
    count = 0
    path.append(goal)
    current = goal
    while current is not None:
        current = parents[current]
        path.append(current)
    path.reverse()
    # path.remove(None)
    # for item in path:
    #     x = item.strip('(').strip(')').split(',')
    #     print(1)
    return path


def main():
    # filename = input('Please enter the filename: ')
    filename = "test1.txt"
    with open(filename) as data:
        first_line = data.readline().strip().split(' ')
        no_of_rows = int(first_line[0])
        no_of_columns = int(first_line[1])
        escape_row = int(first_line[2])
        templist = []
        final_list = []
        for item in data:
            parts = item.strip().split(' ')
            templist.append(parts)

        list = deepcopy(templist)
        for i in range(no_of_rows):
            for j in range(no_of_columns):
                list[j][i] = templist[i][j]

        g = Graph()
        vertex = []
        for i in range(no_of_rows):
            tempvertex = []
            for j in range(no_of_columns):
                v = Vertex("(" + str(i) + "," + str(j) + ")")
                tempvertex.append(v)
                g.addVertex("(" + str(i) + "," + str(j) + ")", v)
            vertex.append(tempvertex)

        for i in range(no_of_rows):
            for j in range(no_of_columns):
                if i < no_of_rows - 1 and j < no_of_columns - 1:
                    if list[i][j] == '.' and list[i + 1][j] == '.':
                        vertex[i][j].add_neighbor(vertex[i + 1][j].data, 1)
                        vertex[i + 1][j].add_neighbor(vertex[i][j].data, 1)
                    if list[i][j] == '.' and list[i][j + 1] == '.':
                        vertex[i][j].add_neighbor(vertex[i][j + 1].data, 1)
                        vertex[i][j + 1].add_neighbor(vertex[i][j].data, 1)
                if i == no_of_rows - 1 and j < no_of_columns - 1:
                    if list[i][j] == '.' and list[i][j + 1] == '.':
                        vertex[i][j].add_neighbor(vertex[i][j + 1].data, 1)
                        vertex[i][j + 1].add_neighbor(vertex[i][j].data, 1)
                if j == no_of_columns - 1 and i < no_of_rows - 1:
                    if list[i][j] == '.' and list[i + 1][j] == '.':
                        vertex[i][j].add_neighbor(vertex[i + 1][j].data, 1)
                        vertex[i + 1][j].add_neighbor(vertex[i][j].data, 1)

        for i in range(no_of_rows):
            for j in range(no_of_columns):
                if list[i][j] == '.':
                    if(shortest_Path_Exists(g, vertex[i][j].data, vertex[no_of_columns-1][escape_row].data)):
                        print(shortest_Path(g, vertex[i][j].data, vertex[no_of_columns-1][escape_row].data))


        print(1)


if __name__ == '__main__':
    main()
