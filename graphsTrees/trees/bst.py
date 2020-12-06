from graphsTrees.trees.node import Node
from graphsTrees.trees.tree import Tree

class BST(Tree):
    
    def create_node(self,key):
        return Node(key)
    
    def insert(self, node, key):
        if node is None:
            return self.create_node(key)
        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        return node
    
    def search_node(self,node,key):
        if node is None:
            return "Node {} does not exist".format(key)
        if node.key == key:
            return "Node {} exists".format(key)
        if node.key<key:
            return self.search_node(node.right,key)
        else:
            return self.search_node(node.left,key)
    
    def delete_node(self,node,key):
        if key < node.key:
            node.left = self.delete_node(node.left,key)
        elif key>node.key:
            node.right = self.delete_node(node.right,key)
        else:
            if node.left is None and node.right is None:
                return None
            elif node.left is None:
                swap = node.right
                del node
                return swap 
            elif node.right is None:
                swap = node.left
                del node
                return swap
        return node
