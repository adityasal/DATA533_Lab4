from graphsTrees.trees.node import Node
from graphsTrees.trees.tree import Tree
from graphsTrees.exceptions.TreeExceptions import NodeError
from graphsTrees.exceptions.TreeExceptions import NodeKeyError

class BST(Tree):
    
    def create_node(self,key):
        try: 
            return Node(int(key))
        except ValueError:
            raise NodeKeyError
    
    def insert(self, node, key):
        if node is None:
            return self.create_node(key)
        if key < node.key:
            node.left = self.insert(node.left, key)
        elif key > node.key:
            node.right = self.insert(node.right, key)
        return node
    
    def search_node(self,node,key):
        try: 
            if node is None:
                return "Node {} does not exist".format(int(key))
            if node.key == int(key):
                return "Node {} exists".format(int(key))
            if node.key<int(key):
                return self.search_node(node.right,int(key))
            else:
                return self.search_node(node.left,int(key))
        except ValueError:
            raise NodeKeyError
    
    def delete_node(self,node,key):
        try: 
            if int(key) < node.key:
                node.left = self.delete_node(node.left,int(key))
            elif int(key)>node.key:
                node.right = self.delete_node(node.right,int(key))
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
        except ValueError:
            raise NodeKeyError


