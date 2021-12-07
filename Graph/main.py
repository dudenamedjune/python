'''
   You have to use the following template to submit to Revel.
   Note: To test the code using the CheckExerciseTool, you will submit entire code.
   To submit your code to Revel, you must only submit the code enclosed between
     # BEGIN REVEL SUBMISSION

     # END REVEL SUBMISSION
'''

# Exercise22_01Extra
# Please search for WRITE YOUR CODE in this template to implement the main function

class LinkedList:
    def __init__(self):
        self.__head = None
        self.__tail = None
        self.__size = 0

    # Return the head element in the list 
    def getFirst(self):
        if self.__size == 0:
            return None
        else:
            return self.__head.element
    
    # Return the last element in the list 
    def getLast(self):
        if self.__size == 0:
            return None
        else:
            return self.__tail.element

    # Add an element to the beginning of the list 
    def addFirst(self, e):
        newNode = Node(e) # Create a new node
        newNode.next = self.__head # link the new node with the head
        self.__head = newNode # head points to the new node
        self.__size += 1 # Increase list size

        if self.__tail == None: # the new node is the only node in list
            self.__tail = self.__head

    # Add an element to the end of the list 
    def addLast(self, e):
        newNode = Node(e) # Create a new node for e
    
        if self.__tail == None:
            self.__head = self.__tail = newNode # The only node in list
        else:
            self.__tail.next = newNode # Link the new with the last node
            self.__tail = self.__tail.next # tail now points to the last node
    
        self.__size += 1 # Increase size

    # Same as addLast 
    def add(self, e):
        self.addLast(e)

    # Insert a new element at the specified index in this list
    # The index of the head element is 0 
    def insert(self, index, e):
        if index == 0:
            self.addFirst(e) # Insert first
        elif index >= self.__size:
            self.addLast(e) # Insert last
        else: # Insert in the middle
            current = self.__head
            for i in range(1, index):
                current = current.next
            temp = current.next
            current.next = Node(e)
            (current.next).next = temp
            self.__size += 1

    # Remove the head node and
    #  return the object that is contained in the removed node. 
    def removeFirst(self):
        if self.__size == 0:
            return None # Nothing to delete
        else:
            temp = self.__head # Keep the first node temporarily
            self.__head = self.__head.next # Move head to point the next node
            self.__size -= 1 # Reduce size by 1
            if self.__head == None: 
                self.__tail = None # List becomes empty 
            return temp.element # Return the deleted element

    # Remove the last node and
    # return the object that is contained in the removed node
    def removeLast(self):
        if self.__size == 0:
            return None # Nothing to remove
        elif self.__size == 1: # Only one element in the list
            temp = self.__head
            self.__head = self.__tail = None  # list becomes empty
            self.__size = 0
            return temp.element
        else:
            current = self.__head
        
            for i in range(self.__size - 2):
                current = current.next
        
            temp = self.__tail
            self.__tail = current
            self.__tail.next = None
            self.__size -= 1
            return temp.element

    # Remove the element at the specified position in this list.
    #  Return the element that was removed from the list. 
    def removeAt(self, index):
        if index < 0 or index >= self.__size:
            return None # Out of range
        elif index == 0:
            return self.removeFirst() # Remove first 
        elif index == self.__size - 1:
            return self.removeLast() # Remove last
        else:
            previous = self.__head
    
            for i in range(1, index):
                previous = previous.next
        
            current = previous.next
            previous.next = current.next
            self.__size -= 1
            return current.element

    # Return true if the list is empty
    def isEmpty(self):
        return self.__size == 0
    
    # Return the size of the list
    def getSize(self):
        return self.__size

    def __str__(self):
        result = "["

        current = self.__head
        for i in range(self.__size):
            result += str(current.element)
            current = current.next
            if current != None:
                result += ", " # Separate two elements with a comma
            else:
                result += "]" # Insert the closing ] in the string

        return result

    # Clear the list */
    def clear(self):
        self.__head = self.__tail = None

    # Return true if this list contains the element o 
    def contains(self, e):
        print("Implementation left as an exercise")
        return True

    # Remove the element and return true if the element is in the list 
    def remove(self, e):
        print("Implementation left as an exercise")
        return True

    # Return the element from this list at the specified index 
    def get(self, index):
        print("Implementation left as an exercise")
        return None

    # Return the index of the head matching element in this list.
    # Return -1 if no match.
    def indexOf(self, e):
        print("Implementation left as an exercise")
        return 0

    # Return the index of the last matching element in this list
    #  Return -1 if no match. 
    def lastIndexOf(self, e):
        print("Implementation left as an exercise")
        return 0

    # Replace the element at the specified position in this list
    #  with the specified element. */
    def set(self, index, e):
        print("Implementation left as an exercise")
        return None
    
    # Return elements via indexer
    def __getitem__(self, index):
        return self.get(index)

    # Return an iterator for a linked list
    def __iter__(self):
        return LinkedListIterator(self.__head)
    
# The Node class
class Node:
    def __init__(self, e):
        self.element = e
        self.next = None

class LinkedListIterator: 
    def __init__(self, head):
        self.current = head
        
    def __next__(self):
        if self.current == None:
            raise StopIteration
        else:
            element = self.current.element
            self.current = self.current.next
            return element    
        
class Queue:
    def __init__(self):
        self.__elements = LinkedList()

    # Adds an element to this queue
    def enqueue(self, e):
        self.__elements.add(e)
    
    # Removes an element from this queue
    def dequeue(self):
        if self.getSize() == 0:
            return None
        else:
            return self.__elements.removeAt(0)
    
    # Return the size of the queue
    def getSize(self):
        return self.__elements.getSize()
    
    # Returns a string representation of the queue
    def __str__(self):
        return self.__elements.__str__()

    # Return true if queue is empty 
    def isEmpty(self):
        return self.getSize() == 0

class Graph:
    def __init__(self, vertices = [], edges = []):
        self.vertices = vertices
        self.neighbors = self.getAdjacnecyLists(edges)

    # Return a list of adjacency lists for edges 
    def getAdjacnecyLists(self, edges):
        neighbors = []
        for i in range(len(self.vertices)):
            neighbors.append([]) # Each element is another list
            
        for i in range(len(edges)):
            u = edges[i][0]
            v = edges[i][1]
            neighbors[u].append(Edge(u, v)) # Insert an edge (u, v)

        return neighbors
    
    # Return the number of vertices in the graph 
    def getSize(self):
        return len(self.vertices)

    # Return the vertices in the graph 
    def getVertices(self):
        return self.vertices

    # Return the vertex at the specified index
    def getVertex(self, index):
        return self.vertices[index]

    # Return the index for the specified vertex 
    def getIndex(self, v):
        return self.vertices.index(v)

    # Return the neighbors of vertex with the specified index 
    def getNeighbors(self, index):
        return self.neighbors[index]
    
    # Return the degree for a specified vertex 
    def getDegree(self, v):
        return len(self.neighbors[self.getIndex(v)])

    # Print the edges 
    def printEdges(self):
        for u in range(0, len(self.neighbors)):
            print(str(self.getVertex(u)) + " (" + str(u), end = "): ")
            for j in range(len(self.neighbors[u])):
                print("(" + str(u) + ", " + 
                      str(self.neighbors[u][j].v), end = ") ")
            print()

    # Clear graph 
    def clear(self):
        vertices = []
        neighbors = []
  
    # Add a vertex to the graph   
    def addVertex(self, vertex):
        if not (vertex in self.vertices):
            self.vertices.append(vertex)
            self.neighbors.append([]) # add a new empty adjacency list
        
    # Add an undirected edge to the graph   
    def addEdge(self, u, v):
        if u in self.vertices and v in self.vertices:
            indexU = self.getIndex(u)
            indexV = self.getIndex(v)
            # Add an edge (u, v) to the graph
            self.neighbors[indexU].append(Edge(indexU, indexV))
  
    # Obtain a DFS tree starting from vertex u 
    # To be discussed in Section 22.6 
    def dfs(self, v):
        searchOrders = []
        parent = len(self.vertices) * [-1] # Initialize parent[i] to -1

        # Mark visited vertices
        isVisited = len(self.vertices) * [False]

        # Recursively search
        self.dfsHelper(v, parent, searchOrders, isVisited)

        # Return a search tree
        return Tree(v, parent, searchOrders, self.vertices)

    # Recursive method for DFS search 
    def dfsHelper(self, v, parent, searchOrders, isVisited):
        # Store the visited vertex
        searchOrders.append(v)
        isVisited[v] = True # Vertex v visited

        for e in self.neighbors[v]:
            w = e.v # e.v is w in Listing 22.6
            if not isVisited[w]:
                parent[w] = v # The parent of vertex w is v
                # Recursive search
                self.dfsHelper(w, parent, searchOrders, isVisited) 

    # Starting bfs search from vertex v 
    # To be discussed in Section 22.7 
    def bfs(self, v):
        searchOrders = []
        parent = len(self.vertices) * [-1] # Initialize parent[i] to -1

        queue = Queue() # the Queue class is defined in Chapter 18
        isVisited = len(self.vertices) * [False]
        queue.enqueue(v) # Enqueue v
        isVisited[v] = True # Mark it visited

        while not queue.isEmpty():
            u = queue.dequeue() # Dequeue to u
            searchOrders.append(u) # u searched
            for e in self.neighbors[u]:
                w = e.v # e.v is w in Listing 22.9
                if not isVisited[w]:
                    queue.enqueue(w) # Enqueue w
                    parent[w] = u # The parent of w is u
                    isVisited[w] = True # Mark it visited

        return Tree(v, parent, searchOrders, self.vertices)

# Tree  class will be discussed in Section 22.5 
class Tree:
    def __init__(self, root, parent, searchOrders, vertices):
        self.root = root # The root of the tree
        # Store the parent of each vertex in a list
        self.parent = parent 
        # Store the search order in a list
        self.searchOrders = searchOrders 
        self.vertices = vertices # vertices of the graph

    # Return the root of the tree 
    def getRoot(self):
      return self.root

    # Return the parent of vertex v 
    def getParent(self, index):
        return self.parent[index]

    # Return an array representing search order 
    def getSearchOrders(self):
        return self.searchOrders

    # Return number of vertices found 
    def getNumberOfVerticesFound(self):
        return len(self.searchOrders)
    
    # Return the path of vertices from a vertex index to the root 
    def getPath(self, index):
        path = []

        while index != -1:
            path.append(self.vertices[index])
            index = self.parent[index]

        return path

    # Print a path from the root to vertex v 
    def printPath(self, index):
        path = self.getPath(index)
        print("A path from " + str(self.vertices[self.root]) + " to " 
              + str(self.vertices[index]), end = ": ")
        for i in range(len(path) - 1, -1, -1):
            print(path[i], end = " ")

    # Print the whole tree 
    def printTree(self):
        print("Root is: " + str(self.vertices[self.root]))
        print("Edges: ", end = "")
        for i in range(len(self.parent)):
            if self.parent[i] != -1:
                # Display an edge
                print("(" + str(self.vertices[self.parent[i]]) 
                      + ", " + str(self.vertices[i]), end = ") ")

        print()
        
# The Edge class for defining an edge from u to v        
class Edge:
    def __init__(self, u, v):
        self.u = u
        self.v = v

# BEGIN REVEL SUBMISSION
def main():
    # prompt to enter number of vertices
    numVertices = int(input("Enter number of vertices: "))
    # prompt to enter the edges line by line
    edges = [] 
    # create graph
    graph = Graph(numVertices, edges)
    # is the graph connected?
    if graph.isConnected():
        print("The graph is connected")

main()