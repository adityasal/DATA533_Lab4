#Vertices and edges as above. weights must be a list of numbers of same length as edge set, and applies 
#Weights to edges in index-wise fashion
import numpy as np
import pandas as pd
import copy

import graphsTrees.graphs.graphs as gr
from graphsTrees.exceptions.EricExceptions import weightError
from graphsTrees.exceptions.EricExceptions import vertexError
from graphsTrees.exceptions.EricExceptions import edgeError

class wtGraph(gr.Graph):
    def __init__(self, vertices, edges, weights):
        gr.Graph.__init__(self, vertices, edges)
        self.weights = weights
                #Adding this condition breaks the kruskal algorithm 
#         if len(edges) != len(weights):
#             raise IndexError("Edge and weight sets must be same length")
        for i in weights:
            try:
                float(i)
            except:
                raise weightError('Weights must be numbers')
                
    #Alter addEdge method to accept a weight argument
    def addEdge(self, v1, v2, weight):
        try:
            int(weight)
        except ValueError:
            raise weightError("Weight must be a number")
        else:
            if type(v1) != int or type(v2) != int:
                raise vertexError('Vertices are integers')
            elif (v1 in self.vertices and v2 in self.vertices):
                if [v1, v2] not in self.edges and [v2, v1] not in self.edges:
                    self.edges.append([v1, v2])
                    self.weights.append(weight)
                else:
                    return('Edge already in edge set')
            else:
                return('Input valid vertices')
            
     #Alter method to remove weight as well
    def rmEdge(self, v1, v2):
        if type(v1) != int or type(v2) != int:
            raise vertexError("Vertices are integers")
        else:
            if [v1, v2] in self.edges:
                self.weights.remove(self.weights[self.edges.index([v1,v2])])
                self.edges.remove([v1, v2])
            elif [v2, v1] in self.edges:
                self.weights.remove(self.weights[self.edges.index([v2,v1])])
                self.edges.remove([v2, v1])
            else:
                return('Edge not in edge set')
            
    #Alter method to print weights as well        
    def printGraph(self):
        return(f'Vertex set: {self.vertices}\nEdge set: {self.edges}\nWeights:{self.weights}')
        
    #Adjust the adjMatrix function to incorperate weights
    def adjMatrix(self): # Gives the adjacency matrix of the graph. Used in other functions
        #Make an n by n zero matrix
        matrix = np.zeros(len(self.vertices)*len(self.vertices)).reshape(len(self.vertices), len(self.vertices))
        for edge in self.edges:
            matrix[edge[0]][edge[1]] = self.weights[self.edges.index(edge)] #Graph is undirected and weighted
            matrix[edge[1]][edge[0]] = self.weights[self.edges.index(edge)]
        return matrix
    

    def kruskal(self):
        kruskVertices = copy.copy(self.vertices)
        # Python pointers strike again! Code was broken for like a day before I remembered copy.copy
        kruskEdges = copy.copy(self.edges)
        kruskWeights = copy.copy(self.weights)
        tree = []
        if self.isConnected() == True:
            while len(tree) < len(kruskVertices) - 2:
                #This is a horrible way of  using the index from the weights list in the edges list
                #If adding the edge makes a cycle, just remove it. else, add to tree
                if wtGraph(len(kruskVertices), tree + [kruskEdges[kruskWeights.index(min(kruskWeights))]], kruskWeights).hasCycles():
                    kruskEdges.remove(kruskEdges[kruskWeights.index(min(kruskWeights))])
                    kruskWeights.remove(min(kruskWeights))
                else:
                    tree.append(kruskEdges[kruskWeights.index(min(kruskWeights))])
                    kruskEdges.remove(kruskEdges[kruskWeights.index(min(kruskWeights))])
                    kruskWeights.remove(min(kruskWeights))
            #This adds the last edge
            tree.append(kruskEdges[kruskWeights.index(min(kruskWeights))])
            return tree
        else:
            return('Graph is disconnected, and there is no spanning tree')
    

    def totalWeight(self):
        return sum(self.weights)