from graphsTrees.trees.node import Node
from graphsTrees.exceptions.TreeExceptions import NodeError,NodeKeyError

class Tree:
    
    def __init__(self):
        self._preorder_list = []
        self._inorder_list = []
        self._postorder_list = []
   
    def create_node(self,key):
        try: 
            return Node(int(key))
        except ValueError:
            raise NodeKeyError
    
    def insert(self, node, key):
        if node is None:
            return self.create_node(int(key))
        else:
            node.left = self.insert(node.left, int(key))
        return node
    
    def search_node(self,node,key):
        try: 
            if node is None:
                return "Node {} does not exist".format(int(key))
            if node.key == key:
                return "Node {} exists".format(int(key))
            else:
                return self.search_node(node.left,int(key))
        
        except ValueError:
            raise NodeKeyError
            
    def preorder(self, node):
        try: 
            if node is not None:
                self._preorder_list.append(node.key)
                self.preorder(node.left)
                self.preorder(node.right)
        
        except TypeError:
            raise NodeError
    
    def inorder(self,node):
        try: 
            if node is not None:
                self.inorder(node.left)
                self._inorder_list.append(node.key)
                self.inorder(node.right)
        
        except TypeError:
            raise NodeError
            
    
    def postorder(self, node):
        try: 
            if node is not None: 
                self.postorder(node.left)
                self.postorder(node.right)
                self._postorder_list.append(node.key)
        
        except TypeError:
            raise NodeError    
    
    def get_preorder(self):
        return self._preorder_list
    
    def get_inorder(self):
        return self._inorder_list
    
    def get_postorder(self):
        return self._postorder_list



