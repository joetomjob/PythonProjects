__author__ = 'Joe Tom Job'
'''
Joe Tom Job (jxj2428) - CSCI 603-01
This program finds the shortest path between 2 people.
'''
#The class node represents each node of the graph
class Node:
    def __init__(self, data):
        self.data = data
        self.children = [] #The children of a node are stored in a list

    #The following functions adds children to the node
    def addChildren(self, name):
        self.children.append(name)

#This class represents the grapgh
class Graph:
    def __init__(self):
        self.nodes = {} #Nodes are svaed in dictionary

    #This function is used to add nodes to graph.Key is the name and value is the node
    def addNode(self, name, node):
        self.nodes[name] = node

#This funtion implements Depth first search algorithm to find the shortest path between the start and goal node.
def shortest_Path(graph, start, end):
    q = []    #This queue maintains the nodes which are not expanded
    parent = {} #The parent dictionary keeps track of parent of each child
    q.append(start)
    parent[start] = None
    while q:
        n = q.pop(0) #In order to maintain the propery of queue(First In Forst Out), first element is picked
        if n == end:
            return create_Path(parent, end) #If we find the goal node, we pass the parent dictionary and the end node to create the path
        if n in graph.nodes:
            for nbr in graph.nodes[n].children:  #If n is not the goal node, we add all the children of the node to queue and keep track of its parent.
                if nbr not in parent:
                    q.append(nbr)  #adding eachneighbor to queue
                    parent[nbr] = n #keeping track of parent of each node

    return None #If the path is not found, we return None

#This function creates the path between the start and end node. The parameters supplied are parent dictionary and goal node.
def create_Path(parent, goal):
    path = [] #we are going to save the path in this list
    path.append(goal) #first we append the end node
    x = goal
    while x is not None:
        path.append(parent[x]) #we append the parent of the current node to list
        x = parent[x] #now we make the parent as current node
    path.remove(None) #we remove None from the list because, we saved the parent of start node as None
    path.reverse() # we reverse the list because we have saved from end to start
    return path # we return the list which contains the path

def friendsOfFriends(f):
    ip = f.strip() #"f" contains file name, start and end node. we extract all the data in next steps
    parts = ip.strip().split(',')

    file = parts[0].strip() #extract file name
    start = parts[1].strip()#extract start node
    end = parts[2].strip()#extract end node

    with open(file) as data:
        vertex = [None]*1000 #initialize a vertex array, so that all vertex can be saved in the array
        cnt = 0
        for x in data:
            x = x.strip()
            partsop = x.strip().split(',')
            vertex[cnt] = Node(partsop[0].strip()) #Store all nodes as a vertex
            for i in range(1,len(partsop)):
                vertex[cnt].addChildren(partsop[i].strip()) #Add children to each of the node
            cnt +=1

        T= Graph() #Initialize a graph
        for i in range(cnt):
            T.addNode(vertex[i].data,vertex[i]) #Store all vertex to grapgh


    return shortest_Path(T,start,end) #This function returns path between start and goal node, if one exists

def main():
    f = input('Enter the input:') #We give the input
    parts = f.strip().split(',')
    file = parts[0].strip() #File name
    start = parts[1].strip()  #Start node
    end = parts[2].strip() #end node

    path = friendsOfFriends(f) #This input is passed to this function and the path is returned if there is any.
    if path is not None:
        print(path) #If path exists, print the path
    else:
        print("There is no path from " + start + " to " + end + " in " + file) #If path does not exixst, then print "there is no path".


if __name__ == '__main__':
    main()