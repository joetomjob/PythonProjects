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


def findShortestPath(graph,start, end):

    queue = []
    queue.append(start)         # prime the queue with the start vertex

    predecessors = {}
    predecessors[start] = None  # add the start vertex with no predecessor

    # Loop until either the queue is empty, or the end vertex is encountered
    while len(queue) > 0:
        current = queue.pop(0)
        if current == end:
            break
        for neighbor in graph.vertices[current].neighbor:
            if neighbor not in predecessors:        # if neighbor unvisited
                predecessors[neighbor] = current    # map neighbor to current
                queue.append(neighbor)              # enqueue the neighbor

    # If the end vertex is in predecessors a path was found
    if end in predecessors:
        path = []
        current = end
        while current != start:              # loop backwards from end to start
            path.insert(0, current)          # prepend current to the path list
            current = predecessors[current]  # move to the predecessor
        path.insert(0, start)
        return path
    else:
        return None


def main():
    filename = input('Please enter the filename: ')
    # filename = "test1.txt"
    try:
        with open(filename) as data:
            first_line = data.readline().strip().split(' ')
            no_of_columns = int(first_line[0])
            no_of_rows = int(first_line[1])
            escape_row = int(first_line[2])
            templist = []

            for item in data:
                parts = item.strip().split(' ')
                templist.append(parts)

            list = deepcopy(templist)
            for i in range(no_of_rows):
                for j in range(no_of_columns):
                    list[j][i] = templist[i][j]

            g = Graph()
            row_block = []
            col_block = []
            vertex = []
            for i in range(no_of_rows):
                tempvertex = []
                tempblock = []
                for j in range(no_of_columns):
                    v = Vertex("(" + str(i) + "," + str(j) + ")")
                    tempvertex.append(v)
                    g.addVertex("(" + str(i) + "," + str(j) + ")", v)
                    if list[i][j] == '*':
                        # block.append("(" + str(i) + "," + str(j) + ")")
                        row_block.append(i)
                        col_block.append(j)

                vertex.append(tempvertex)

            for i in range(no_of_rows):
                k = 0
                for j in range(no_of_columns):
                    if list[i][j] == '.':
                        #   up
                        k = i
                        while (k >= 0):
                            if k != 0 and list[k][j] == '.':
                                k = k - 1
                            elif list[k][j] == '*':
                                if k + 1 != i:
                                    vertex[i][j].add_neighbor(vertex[k + 1][j].data, 1)
                                break;
                            elif k == 0:
                                if k != i:
                                    vertex[i][j].add_neighbor(vertex[k][j].data, 1)
                                k -= 1

                        # down
                        k = i
                        while (k <= no_of_rows - 1):
                            if k != no_of_rows - 1 and list[k][j] == '.':
                                k = k + 1
                            elif list[k][j] == '*':
                                if k - 1 != i:
                                    vertex[i][j].add_neighbor(vertex[k - 1][j].data, 1)
                                break
                            elif k == no_of_rows - 1:
                                if k != i:
                                    vertex[i][j].add_neighbor(vertex[k][j].data, 1)
                                k += 1

                        # left
                        k = j
                        while (k >= 0):
                            if k != 0 and list[i][k] == '.':
                                k = k - 1
                            elif list[i][k] == '*':
                                if k + 1 != j:
                                    vertex[i][j].add_neighbor(vertex[i][k + 1].data, 1)
                                break
                            elif k == 0:
                                if k != j:
                                    vertex[i][j].add_neighbor(vertex[i][k].data, 1)
                                k -= 1

                        # right
                        k = j
                        while (k <= no_of_columns - 1):
                            if k != no_of_columns - 1 and list[i][k] == '.':
                                k = k + 1
                            elif list[i][k] == '*':
                                if k - 1 != j:
                                    vertex[i][j].add_neighbor(vertex[i][k - 1].data, 1)
                                break
                            elif k == no_of_columns - 1:
                                if k != j:
                                    vertex[i][j].add_neighbor(vertex[i][k].data, 1)
                                k += 1

            final_list = [None] * no_of_columns*no_of_rows
            none_list = []
            for i in range(no_of_rows):
                for j in range(no_of_columns):
                    if list[i][j] == '.':
                        path = findShortestPath(g, vertex[i][j].data, vertex[no_of_columns - 1][escape_row].data)
                        if path is not None:
                            if len(path)in (1,2):
                                if final_list[1] is None:
                                    final_list[1] = []
                                    final_list[1].append(vertex[i][j].data)
                                else:
                                    final_list[1].append(vertex[i][j].data)
                            else:
                                if final_list[len(path)-1] is None:
                                    final_list[len(path)-1] = []
                                    final_list[len(path)-1].append(vertex[i][j].data)
                                else:
                                    final_list[len(path)-1].append(vertex[i][j].data)
                        else:
                            none_list.append(vertex[i][j].data)


            for i in range(len(final_list)):
                if final_list[i] is not None:
                    print(str(i) + " : "+ str(final_list[i]))
            if len(none_list) >0:
                print("No path : " + str(none_list))
    except(FileNotFoundError):
        print("The file does not exist. Please enter other filename")


if __name__ == '__main__':
    main()
