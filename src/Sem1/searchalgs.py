"""
CSCI-603: Graphs
Authors:  (11/16/2016) Adam Purtee @ RIT CS
                       -- added hasPath, pathFinder, and findDJI
          (Original Version) Sean Strout @ RIT CS

This is the implementation of the three search algorithms used:
    1. canReachDFS: Can start reach end using recursive DSF (yes or no)?
    2. findPathDFS: Find any path from start to end, if one exists,
        using recursive DFS.
    3. findShortestPath:  Find the shortest path from start to end,
        if one exists, iteratively using BFS and a queue.
"""
import heap   # needs to support decrease key
import queue  # needs to support push/pop
import stack

from graph import *
def __canReachDFS(current, visited):
    """
    Private recursive helper function for canReachDFS.  It traverses all
    reachable nodes in the graph, recursively.
    :param current (Vertex): the current Vertex object
    :param visited (set of Vertex): the vertices already visited
    :return: None
    """
    for neighbor in current.getConnections():
        # this check prevents cycles from infinitely looping
        if neighbor not in visited:
            visited.add(neighbor)
            __canReachDFS(neighbor, visited)

def canReachDFS(start, end):
    """
    A boolean functions that indicates whether a start vertex is able
    to reach an end vertex by recursively traversing neighbors.
    :param start (Vertex): the starting vertex
    :param end (Vertex): the ending vertex
    :return: True if there is a path, False otherwise
    """
    visited = set()
    visited.add(start)
    __canReachDFS(start, visited)
    # a path exists if the end node was visited, otherwise the graph is
    # disconnected and no path exists from start to end
    return end in visited

def __findPathDFS(current, end, visited):
    """
    Private recursive helper function that finds the path, if one exists,
    from the current vertex to the end vertex
    :param current (Vertex): The current vertex in the traversal
    :param end (Vertex): The destination vertex
    :param visited (set of Vertex): the vertices already visited
    :return: A list of Vertex objects from start to end, if a path exists,
        otherwise None
    """

    # A successful base case is when we traverse to the end vertex.  In this
    # case, wrap it in a list and return it to the caller to construct the
    # full path
    if current == end:
        return [current]
    for neighbor in current.getConnections():
        if neighbor not in visited:
            visited.add(neighbor)
            path = __findPathDFS(neighbor, end, visited)
            # If the path is not None, current is part of the solution path,
            # so add it to the front of the path list and return it
            if path != None:
                path.insert(0, current)
                return path
    # No path was found, so pass back None
    return None

def findPathDFS(start, end):
    """
    Find a path, if one exists, from a start to end vertex.
    :param start (Vertex): the start vertex
    :param end (Vertex): the destination vertex
    :return: A list of Vertex objects from start to end, if a path exists,
        otherwise None
    """
    visited = set()
    visited.add(start)
    return __findPathDFS(start, end, visited)

def findShortestPath(start, end):
    """
    Find the shortest path, if one exists, between a start and end vertex
    :param start (Vertex): the start vertex
    :param end (Vertex): the destination vertex
    :return: A list of Vertex objects from start to end, if a path exists,
        otherwise None
    """
    # Using a queue as the dispenser type will result in a breadth first
    # search
    queue = []
    queue.append(start)         # prime the queue with the start vertex

    # The predecessor dictionary maps the current Vertex object to its
    # immediate predecessor.  This collection serves as both a visited
    # construct, as well as a way to find the path
    predecessors = {}
    predecessors[start] = None  # add the start vertex with no predecessor

    # Loop until either the queue is empty, or the end vertex is encountered
    while len(queue) > 0:
        current = queue.pop(0)
        if current == end:
            break
        for neighbor in current.getConnections():
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

def hasPath(startVert, endVert, sequencer):
    """
    A generic graph search algorithm.   Yields DFS when sequencer
    is a stack, and yields BFS when sequencer is a queue.

    :param startVert:  the vertex object to start the search from
    :param endVert:   the vertex object to search for
    :param sequencer: a data structure to sequence the nodes to visit
    :return : a boolean
    """
    visited = set()
    sequencer.push(startVert)
    while (not sequencer.empty()):
        current = sequencer.pop()
        visited.add(current)
        print("Visting " + str(current.id))
        for n in current.getConnections():
            if n == endVert:
                return True
            if n not in visited:
                sequencer.push(n)
    return False

def pathFinder(startVert, endVert, sequencer):
    """
    A generic graph search algorithm.   Yields DFS when sequencer
    is a stack, and yields BFS when sequencer is a queue.
    :param startVert:  the vertex object to start the search from
    :param endVert:   the vertex object to search for
    :param sequencer: a data structure to sequence the nodes to visit
    :return : a list of vertex objects corresponding to the path if found,
              if no path exists, returns None
    """
    sequencer.push(startVert)
    prevVertex = {}
    prevVertex[startVert] = None
    while (not sequencer.empty()):
        current = sequencer.pop()
        for n in current.getConnections():
            if (n not in prevVertex):
                prevVertex[n] = current
                if n == endVert:
                    return backtrack(startVert, n, prevVertex)
                sequencer.push(n)
    return None

def backtrack(start, current, prev):
    """
    Helper function to follow backpointers and build a path list.
    :param start:    The source vertex.
    :param current:  An intermediate vertex in the path.
    :param prev:     A dictionary from vertices to previous vertices.
    :return:         A list of vertex objects.
    """
    if current != start:
        v = prev[current]
        return backtrack(start, v, prev) + [current]
    else:
        return [start]


def findDJI(startVert, endVert):
    """
    An implementation of Djikstra's algorithm for computing
    shortest paths.   Given a binomial heap supporting decreaseKey
    in O(log N) time, the run time of this algorithm is O((V + E)*log(V)).

    Note that this does not work with negative cost edges.
    
    :param startVert:  the source vertex object
    :param endVert:    the destination vertex object
    :return:           A list of vertex objects corresponding to the
                       shortest weighted path if a path exists.  Otherwise,
                       returns None.
    """                       

    dist = {}
    dist[startVert] = 0
    prev = {}
    prev[startVert] = None
    q = heap.Heap()
    q.insert(startVert, dist[startVert])
    while (q):
        # current is the next unvisited, closest node to start
        current = q.pop()
        
        # check to see if we found a better path to any
        # of current's neighbors
        for n in current.getConnections():
            if n not in dist:
                # we found a new node
                dist[n] = dist[current] + current.getWeight(n)
                prev[n] = current
                q.insert(n, dist[n])
            if dist[current] + current.getWeight(n) < dist[n]:
                # we found a better path
                dist[n] = dist[current] + current.getWeight(n)
                prev[n] = current
                q.decreaseKey(n, dist[n])
    if endVert in dist:
        return backtrack(startVert, endVert, prev)
    else:
        return None


def buildTestGraph():
    g = Graph()
    g.addEdge("A", "B")
    g.addEdge("B", "A")
    g.addEdge("B", "C")
    g.addEdge("C", "D")
    g.addEdge("A", "C")

    for source, dest in [("A", "D"), ("B", "D")]:
        
        sv = g.getVertex(source)
        dv = g.getVertex(dest)
        print("DFS (" + source + "->" + dest + "): " + str([x.id for x in pathFinder(sv, dv, stack.Stack())]))
        print("BFS (" + source + "->" + dest + "): " + str([x.id for x in pathFinder(sv, dv, queue.Queue())]))
        print("DJI (" + source + "->" + dest + "): " + str([x.id for x in findDJI(sv, dv)]))
        print("FSP (" + source + "->" + dest + "): " + str([x.id for x in findShortestPath(sv, dv)]))
    return g

def buildG1():
    # Builds the following graph:
    #
    #       A - B - C     J-K
    #      / \      |
    #     D   E     F
    #      \ /      |
    #       G - H - I
    # 
    # Note that the graph class is directed,
    # so we add bidirectional edges with uniform
    # positive cost.

    g = Graph()

    for source, dest in [("A", "B"), ("B", "C"), ("A", "D"), ("A", "E"), ("D", "G"), ("E", "G"), ("G", "H"), ("H", "I"), ("C", "F"), ("I", "F"), ("J", "K")]:
        g.addEdge(source, dest, 1)
        g.addEdge(dest, source, 1)
    return g

if __name__ == '__main__':
    buildTestGraph()


