import numpy as np
import pandas as pd

#Input must be of form vertex: integer. edges: list of lists of two elements of vertex set.

# I wanted to implement graphs in a way that wasn't adjacency matrices or adjacency lists
# To show that I didn't plagiarize from teh internet... Because no competent programmer would
# Have ever used this horrible methodology

class Graph:
    
    # This parameter will change first time user runs hasCycles method, or DFS on a cyclic vertex
    __cycles = False #Want these to be hidden
    __connected = None
    
    def __init__(self, vertices, edges):
        try:
            self.vertices = np.arange(vertices)
        except TypeError:
            raise TypeError('Vertices is an integer, determining number of vertices')
        self.edges = edges
        for edge in edges:
            if len(edge) != 2 or type(edge) != list:
                raise ValueError('Edges must be two element lists')
            if edge[0] not in self.vertices or edge[1] not in self.vertices:
                raise ValueError('Edge connects non-existant vertex')
    
    def addEdge(self, v1, v2):
        if (v1 in self.vertices and v2 in self.vertices):
            if [v1, v2] not in self.edges and [v2, v1] not in self.edges:
                self.edges.append([v1, v2])
            else:
                print('Edge already in edge set')
        else:
            print('Input valid vertices')
            
    def addVertex(self):
        self.vertices = np.arange(len(self.vertices) + 1)
        print(f'Vertex {len(self.vertices)-1} added')
            
    def rmEdge(self, v1, v2):
        if [v1, v2] in self.edges:
            self.edges.remove([v1, v2])
        elif [v2, v1] in self.edges:
            self.edges.remove([v2, v1])
        else:
            print('Edge not in edge set')
            
    #This function broke my indexing for other functions and it was too much hassle to alter the indexes
#     def rmVertex(self, vertex):
#         if vertex in self.vertices:
#             self.vertices.remove(vertex)
#             for edge in self.edges:
#                 if vertex in edge:
#                     self.edges.remove(edge)
#         else:
#             print('Not in vertex set')
    
    def printGraph(self):
        print(f'Vertex set: {self.vertices}\nEdge set: {self.edges}')
        
    def adjMatrix(self): # Gives the adjacency matrix of the graph. Used in other functions
        #Make an n by n zero matrix
        matrix = np.zeros(len(self.vertices)*len(self.vertices)).reshape(len(self.vertices), len(self.vertices))
        for edge in self.edges:
            matrix[edge[0]][edge[1]] = 1 #Graph is undirected and unweighted, so both transposes are set to 1
            matrix[edge[1]][edge[0]] = 1
        return matrix
        
        
    # I got some help from here https://www.geeksforgeeks.org/implementation-of-dfs-using-adjacency-matrix/
    # because my dumb brain can't handle recursion
    
    # I had visited = {} as default and all my code was broken until I 
    # changed it to None. Python is confusing!
    
    # showSteps parameter allows me to not print the DFS steps when the function is called by hasCycles, isConnected, kruskal
    def DFS(self, start, visited = None, previous = None, showSteps = True):
        toPrint = showSteps # Need to pass this in to make it work with recursion
        verts = self.vertices
        hasCycles = False #Used in the hasCycles method
        matrix = self.adjMatrix() # I could only figure out how to make this work for adjacency matrices
        if showSteps == True: #We want to block print when DFS called from other functions
            print(f'Visit {start} from {previous}')
        if visited == None:
            visited = {start}
        else:
            visited.add(start)
        for i in verts:
            if matrix[start][i] != 0:
                if i in visited and i != previous:
                    self.__cycles = True
                elif i not in visited:
                    self.DFS(i, visited, previous = start, showSteps = toPrint)
        self.__connected = visited #We need these in the following two functions
        
    def isConnected(self):
        self.DFS(0, showSteps= False)
        # Start doesn't matter, since we can reach any other vertex iff connected. Choose 0 since its in any size graph
        if len(self.__connected) == len(self.vertices):
            return True
        else:
            return False
    
    def hasCycles(self):
        for i in self.vertices:
            self.DFS(i, showSteps = False)
        return self.__cycles
