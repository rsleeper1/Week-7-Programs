#Crossing The River
#Ryan Sleeper
#This program produces a solution to the cannibal and missionaries problem.



#The vertex class allows me to add nodes to my graph and put any kind of data on a particular node.
class Vertex:
    def __init__(self, key, state):
        self.id = key
        self.state = state
        self.color = 'white'
        self.connectedTo = {}
        
    def getColor(self):
        return self.color
    
    def setColor(self, color):
        self.color = color

    def addNeighbor(self,nbr,weight=0):
        self.connectedTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])

    def getConnections(self):
        if len(self.connectedTo.keys()) == 0:
            return None
        else:
            return self.connectedTo.keys()

    def getId(self):
        return self.id
    
    def getState(self):
        return self.state

    def getWeight(self,nbr):
        return self.connectedTo[nbr]
    
#The graph class allows me to make a graph that consists of nodes and "edges" that connect the nodes.    
class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self,key, state):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key, state)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self,n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self,n):
        return n in self.vertList

    def addEdge(self,f,t,cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
    
#I use the stack data structure in order to keep track of nodes that I have visited during my search in the graph.    
class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
    
#The findSolution method takes five parameters, an initial starting point, an ending point, an empty list (which will end up being the solution),
#an empty stack, and another empty list which I added at the end to show the state of the problem after every step.
def findSolution(startingPoint, endingPoint, solution, stack, states):
    currentNode = startingPoint
    solution.append(currentNode.getId())
    states.append(currentNode.getState())
    stack.push(currentNode)
    while currentNode.getState() != endingPoint.getState():
        if currentNode.getConnections() == None:
            solution.pop()
            states.pop()
            stack.pop()
        item = stack.pop()
        for node in item.getConnections():
            stack.push(node)
        findSolution(stack.peek(), endingPoint, solution, stack, states)
        break
    return solution, states
        
#In the main method I create a graph by using the information from the problem at hand and then creating
#nodes for all the possible legal states in the problem. I organized a particular state as follows:
#(# of missionaries on left, # of cannibals on left, 0 means boat is on left / 1 means boat is on right, # of missionaries on right, # of cannibals on right)
#For example, my starting point is (3,3,0,0,0) meaning 3 missionaries, 3 cannibals, and the boat are on the left island. Nobody is currently on the right island.
#After I created the graph I call the findSolution method and it prints out a possible solution in both words and states.
def main():
    graph = Graph()
    stack = Stack()
    startingPoint = graph.addVertex('startingPoint', (3,3,0,0,0))
    move1 = graph.addVertex('move1', (3,2,1,0,1))
    move2 = graph.addVertex('move2', (2,2,1,1,1))
    move3 = graph.addVertex('move3', (3,1,1,0,2))
    move4 = graph.addVertex('move4', (3,2,0,0,1))
    move5 = graph.addVertex('move5', (3,0,1,0,3))
    move6 = graph.addVertex('move6', (3,1,0,0,2))
    move7 = graph.addVertex('move7', (1,1,1,2,2))
    move8 = graph.addVertex('move8', (2,2,0,1,1))
    move9 = graph.addVertex('move9', (0,2,1,3,1))
    move10 = graph.addVertex('move10', (0,3,0,3,0))
    move11 = graph.addVertex('move11', (0,1,1,3,2))
    move12 = graph.addVertex('move12', (1,1,0,2,2))
    move13 = graph.addVertex('move13', (0,2,0,3,1))
    endingPoint = graph.addVertex('endingPoint', (0,0,1,3,3))
    graph.addEdge('startingPoint', 'move1')
    graph.addEdge('startingPoint', 'move2')
    graph.addEdge('startingPoint', 'move3')
    graph.addEdge('move2', 'move4')
    graph.addEdge('move3', 'move4')
    graph.addEdge('move4', 'move5')
    graph.addEdge('move5', 'move6')
    graph.addEdge('move6', 'move7')
    graph.addEdge('move7', 'move8')
    graph.addEdge('move8', 'move9')
    graph.addEdge('move9', 'move10')
    graph.addEdge('move10', 'move11')
    graph.addEdge('move11', 'move12')
    graph.addEdge('move11', 'move13')
    graph.addEdge('move12', 'endingPoint')
    graph.addEdge('move13', 'endingPoint')
    
    solution = []
    states = []
    solution, states = findSolution(startingPoint, endingPoint, solution, stack, states)
    print(solution)
    print(states)
        
main()
        