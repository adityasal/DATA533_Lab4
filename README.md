# DATA533 Lab 4
By Eric Baxter and Adityal Saluja

[![CIGraphsTrees Actions Status](https://github.com/adityasal/DATA533_Lab4/workflows/CI_GraphsTrees/badge.svg)](https://github.com/adityasal/DATA533_Lab4/actions)

## Graphs Subpackage by Eric
This sub-package contains two modules, one for un-weighted graphs and one for weighted graphs. 

### Graphs.py

Contains the Graph class for un-weighted graphs. 
Inputs:
- vertices: A positive integer n representing the number of vertices in the graph. 
- edges: A list of two element lists. Element [i,j] represents an edge from vertex i to vertex j (un-weighted, undirected)

The class implements the following methods:

addEdge
- Input: integers i, j
- adds an edge from vertex i to vertex j. Raises an error if there is no vertex i or j
- Usage: g.addEdge(0,4) adds edge from vertex 0 to vertex 4

addVertex
- Input: Takes no argument
- Adds a vertex n to a graph of size n
- Usage: g.addVertex(). If G has 4 vertices [0,1,2,3] will add vertex labeled 4

rmEdge
- Input: integers i,j
- Removes the edge between vertex i and vertex j
- Usage: g.rmEdge(1,3) removes edge between vertex 1 and vertex 3

adjMatrix
- Input: Takes no argument
- Returns the adjacency matrix of the graph

DFS
- Input: integer i
- Performs a depth first search on the graph starting from vertex i

isConnected
- Input: Takes no argument
- Returns True if the graph is connected, false otherwise

hasCycles
- Input: Takes no argument
- Returns True if the graph has cycles, false otherwise

printGraph
- Input: Takes no argument
- Prints the edge set and vertex set of the graph

### wtGraphs.py

The module contains the wtGraph class for weighted graphs. Inherits from Graph class

Inputs:
- vertices: as in Graph
- edges: as in Graph
- weights: A list of numbers, where weights[i] is the weight of edge edges[i]

Methods:

Inherits all methods from Graph class and adds the following:

adjMatrix
- Input: None
- Modifies adjMatrix function from Graph class to include weights

kruskal
- Input: None
- Performs Kruskal's algorithm for a minimal spanning tree. Returns a list of edges that form this tree

totalWeight
- Input: None
- Gives the sum of all the weights of a graph| g.totalWeight()


## Trees Subpackage by Aditya

This sub-package consists of three modules, node, tree and BST. The package enables the user to implement a generic tree or binary search tree (BST) data structure in Python. 

node.py

This module consists of Node class to be used by both tree and BST classes. The class contains a single constructor method. An object of this class must be instantiated by providing a key value for a node. The value can be of any data type. This class will have three attributes: the node itself and its left and right child. 

tree.py

This module allows a user to implement a generic tree structure. 

Methods:

create_node:

-	Input: key of any datatype 
-	Creates a node for a tree 
-	Output: Node object 
-	Usage: tree.create_node(5)

insert:

-	Input: root_node, key 
-	The method allows the user to add more nodes to the tree structure. If the tree is empty a new root node is created, and any additional nodes are attached to this root node.
-	Usage: tree.insert(root_node, 10)

search_node:

-	Input: root_node, key
-	The method allows the user to search a node. 
-	Output: A string indicating whether a node exists or not 
-	Usage: tree.search_node(root_node, 7)

Methods for tree traversal:

Three methods were included for traversing the tree: inorder, preorder and postorder. 

-	Input: root_node
-	Usage: tree.inorder(root_node)


bst.py

This module inherits all methods from Tree class and overrides the insert and search_node methods. The module also adds a method to delete a node from the tree. 

Methods:

create_node:

Similar to create_node method in tree module 

insert_node:

-	Input: root_node, key
-	The method allows the user to add more nodes to the tree structure. If the tree is empty a new root node is created, and any additional nodes are attached to this root node, such that if the value is lower than the parent node the node is added to the left else to the right. 
-	Usage: bst.insert(root_node, 9)

search_node:
-	Input: root_node, key
-	Similar to search_node method in tree module, however instead of searching the entire tree the method implements binary search algorithm to reduce the time complexity. 
-	Usage: bst.search_node(root_node, 3)

delete_node:
-	Input: root_node, key
-	Deletes a node in bst
-	Usage: bst.delete_node(root_node, 4)

Methods for tree traversal:

Inherited from the ones included in tree module 
